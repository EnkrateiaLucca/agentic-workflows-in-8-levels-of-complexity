# pip install --upgrade openai
import os
import json
from pathlib import Path
from typing import Dict, Callable

from openai import OpenAI

# --- Client ---
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# --- Safe file helpers (restrict to a base directory) ---
BASE_DIR = Path.cwd()  # change if you want a sandbox like Path("./sandbox").resolve()

def _ensure_under_base(p: Path) -> Path:
    p = (BASE_DIR / p).resolve()
    if not str(p).startswith(str(BASE_DIR)):
        raise ValueError("Path escapes base directory")
    return p

def read_file(file_path: str) -> str:
    """Read UTF-8 text from a file under BASE_DIR."""
    p = _ensure_under_base(Path(file_path))
    return p.read_text(encoding="utf-8")

def write_file(file_path: str, content: str) -> str:
    """Write UTF-8 text to a file under BASE_DIR (create parents)."""
    p = _ensure_under_base(Path(file_path))
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    return f"Wrote {len(content)} chars to {p.relative_to(BASE_DIR)}"

# --- Tool schema for function calling ---
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read text content from a UTF-8 file relative to the working directory.",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Path to the file to read (e.g., 'data/input.txt')."
                    }
                },
                "required": ["file_path"],
                "additionalProperties": False
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Write UTF-8 text content to a file (creates directories if needed).",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Where to write (e.g., 'out/summary.txt')."
                    },
                    "content": {
                        "type": "string",
                        "description": "Text to write into the file."
                    }
                },
                "required": ["file_path", "content"],
                "additionalProperties": False
            },
        },
    },
]

# Map tool names to Python callables
PY_TOOLS: Dict[str, Callable[..., str]] = {
    "read_file": read_file,
    "write_file": write_file,
}

SYSTEM = (
    "You are a careful assistant that can use tools to read and write files.\n"
    "- If a task involves files, call the appropriate tool with precise arguments.\n"
    "- After tool calls, summarize results for the user.\n"
    "- Only write files when explicitly asked or when necessary to complete the task.\n"
    "- If something is ambiguous (e.g., missing path), ask a concise clarifying question."
)

def run_basic_agent(task_prompt: str, *, max_turns: int = 8) -> str:
    """
    Basic function-calling agent loop using OpenAI's Chat Completions:
    - Provides tools (read_file, write_file)
    - Executes any returned tool calls
    - Feeds tool observations back to the model
    - Stops on normal assistant text output
    """
    messages = [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": task_prompt},
    ]

    for turn in range(1, max_turns + 1):
        resp = client.chat.completions.create(
            model="gpt-5-mini",
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
        )

        msg = resp.choices[0].message
        tool_calls = msg.tool_calls or []

        if tool_calls:
            # 1) Append the assistant message (WITH its tool_calls) first
            assistant_msg = {
                "role": "assistant",
                "content": msg.content or "",
                "tool_calls": [
                    {
                        "id": tc.id,
                        "type": "function",
                        "function": {
                            "name": tc.function.name,
                            "arguments": tc.function.arguments,
                        },
                    }
                    for tc in tool_calls
                ],
            }
            messages.append(assistant_msg)

            # 2) Execute each tool call and append a matching 'tool' message
            for tc in tool_calls:
                name = tc.function.name
                try:
                    args = json.loads(tc.function.arguments or "{}")
                except json.JSONDecodeError:
                    args = {}

                fn = PY_TOOLS.get(name)
                if not fn:
                    observation = f"Error: unknown tool '{name}'."
                else:
                    try:
                        observation = fn(**args)
                    except TypeError as e:
                        observation = f"Error calling '{name}' with args {args}: {e}"
                    except Exception as e:
                        observation = f"Tool '{name}' failed: {e}"

                messages.append({
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "name": name,
                    "content": str(observation),
                })

            # 3) Loop so the model can incorporate observations
            continue

        # No tool calls — if the model answered, return it
        if msg.content:
            return msg.content.strip()

        # Fallback nudge
        messages.append({
            "role": "user",
            "content": "Please provide a clear answer or call a tool.",
        })

    return "Stopped: max_turns reached without a final answer."


# --- Example usage ---
if __name__ == "__main__":
    # Prepare a demo file first:
    Path("sample_input.txt").write_text(
        """
        Here’s a short technical essay, concise but with enough depth to show structure and clarity:

        ---

        ## The Role of Embeddings in Modern AI Systems

        At the core of many AI applications lies the concept of **embeddings**—mathematical representations of data in a high-dimensional vector space. Embeddings are powerful because they allow raw, unstructured inputs such as text, images, or even audio to be transformed into numerical formats that capture semantic meaning.

        For natural language, embeddings map words or sentences into vectors such that similar concepts are placed closer together. For example, the vectors for *“king”* and *“queen”* will be nearer than those for *“king”* and *“banana.”* This property enables efficient search, clustering, recommendation, and reasoning tasks.

        Modern models like OpenAI’s GPT or Google’s Gemini rely heavily on embeddings not only for understanding user queries but also for retrieving relevant knowledge from external sources. A widely used technique is **retrieval-augmented generation (RAG)**, where embeddings are used to find semantically related documents that the model can consult when forming its answer.

        Beyond text, multimodal embeddings unify different types of data. An image of a dog, the spoken word “dog,” and the text “dog” can all be mapped into a shared space, enabling systems like CLIP or cross-modal search engines.

        The importance of embeddings lies in their dual role: they are both a **bridge between raw data and machine reasoning** and a **foundation for scalable, semantic applications.** As embedding models become more fine-grained and domain-specific, they will continue to expand the frontiers of AI-driven search, personalization, and knowledge navigation.

        ---

        Do you want me to make this essay more **academic (with citations)**, or more **casual and blog-style**?

        """,
        encoding="utf-8",
    )

    user_task = (
        "Read 'sample_input.txt' and write a concise 2-sentence summary "
        "to 'summary_file.txt'. Then confirm what you did."
    )
    result = run_basic_agent(user_task)
    print("\n--- FINAL ---\n" + result)
