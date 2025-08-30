# Agentic Workflows — 2025 literature summary

Date of report: August 30, 2025
Scope: Recent (2025) papers on building, evaluating, and deploying agentic workflows (LLM-driven multi-agent systems, automated workflow generation, robustness, orchestration, and domain applications).

## Executive summary

In 2025 research on "agentic workflows" has matured from early multi-agent proofs-of-concept into a diverse set of papers that address: automated generation of workflows (AFlow, Flow, MermaidFlow, SwarmAgentic), robustness and vulnerability analysis ("Helpful Agent Meets Deceptive Judge"), performance prediction and resource-aware orchestration (Agentic Predictor, Murakkab), domain-specific adaptation (MedAgent-Pro, economic research workflows), and methods for inducing programmatic skills and episodic control to improve reliability and efficiency. These lines emphasize automation, modularity, verification/safety constraints, and practical deployment trade-offs. citeturn0search0turn0search2turn0search4turn1academia15turn0academia16


## Key papers (selected)

- AFlow: Automating Agentic Workflow Generation — Jiayi Zhang et al. (revised Apr 15, 2025).
  - Contribution: Reformulates workflow optimization as a search over code-represented workflows and applies Monte Carlo Tree Search (MCTS) with iterative code modification and execution feedback to discover and refine agentic workflows. Reports improvements over baselines and cost-efficiency benefits for smaller models. citeturn0search0

- Flow: A Modular Approach to Automated Agentic Workflow Generation — Boye Niu et al. (Jan 14, 2025).
  - Contribution: Models workflows as activity-on-vertex (AOV) graphs and emphasizes dynamic, modular adjustment of task allocations during execution using historical performance to support concurrency and error tolerance. Demonstrates gains in efficiency and robustness for complex tasks. citeturn0search2

- MermaidFlow: Safety-Constrained Evolutionary Programming — Chengqi Zheng et al. (May 29, 2025).
  - Contribution: Uses a human-interpretable intermediate representation (Mermaid graphs) and domain-aware evolutionary operators to evolve verifiable workflows under safety constraints, improving executability and convergence to high-quality plans. Highlights interpretability + static verifiability as a practical defense against fragile LLM-generated plans. citeturn0search4

- SwarmAgentic: Fully Automated Agentic System Generation via Swarm Intelligence — Yao Zhang et al. (Jun 18, 2025).
  - Contribution: Introduces an evolutionary/swarm optimization approach that evolves whole agentic systems (agents + collaboration structure) from scratch, showing large gains on exploratory, open-ended tasks and moving toward end-to-end automation of system design. citeturn1academia15

- Helpful Agent Meets Deceptive Judge: Understanding Vulnerabilities in Agentic Workflows — Yifei Ming et al. (Jun 3, 2025).
  - Contribution: Systematically studies vulnerabilities introduced by feedback/judge components in multi-agent workflows, providing a 2D taxonomy (intent × knowledge) and the WAFER-QA benchmark with retrieved-evidence critiques. Demonstrates that persuasive but factually incorrect critiques can destabilize even strong agents. citeturn0academia16

- Agentic Predictor: Performance Prediction for Agentic Workflows — Patara Trirat et al. (May 26, 2025).
  - Contribution: Proposes a lightweight, multi-view encoder to predict success rates of agentic workflows (architecture, prompts, interaction graphs) to speed up configuration search and reduce expensive evaluations. Shows promise as a design-time tool for workflow selection. citeturn1academia16

- Murakkab: Resource-Efficient Agentic Workflow Orchestration in Cloud Platforms — (Aug 22, 2025 preprint visible in search results).
  - Contribution: (System/ops focus) Presents a declarative abstraction decoupling workflow spec from execution configuration and a profile-guided optimizer that maps workflow components to models/hardware and enforces SLOs, achieving substantial GPU/energy/cost reductions in evaluation. (Note: preprint date Aug 22, 2025). citeturn1academia12

- MedAgent-Pro: Evidence-based Multi-modal Medical Diagnosis via Reasoning Agentic Workflow — Ziyue Wang et al. (Mar 21, 2025).
  - Contribution: Illustrates domain adaptation of agentic workflows to medical diagnosis by structuring hierarchical, evidence-driven diagnostic steps, integrating VLMs and HITL checkpoints to improve clinical reliability. citeturn0search5

- Agentic Workflows for Economic Research — Herbert Dawid et al. (Apr 13, 2025).
  - Contribution: Describes design patterns and implementation details for end-to-end agentic workflows tailored to economic research, integrating human oversight, role-specialized agents, and reproducibility mechanisms using platforms such as AutoGen. citeturn0search1

- Agentic Workflows for Conversational Human-AI Interaction Design — Arthur Caetano et al. (Jan 29, 2025).
  - Contribution: Explores designer-facing agentic workflows to support conversational human-AI interaction (CHAI), focusing on ambiguity resolution, design probes, and iterative user studies that show how agents can scaffold user goals and prompt generation. citeturn0search3

- Inducing Programmatic Skills for Agentic Tasks — Zora Z. Wang et al. (Apr 9, 2025).
  - Contribution: Treats programs as first-class skill representations for agents, showing that agents can induce, verify, and reuse programmatic skills online to improve success and efficiency in web-based tasks. citeturn1search3

- Agentic Episodic Control — Xidong Yang et al. (Jun 2, 2025).
  - Contribution: Proposes combining LLMs and episodic memory for RL-style episodic control to increase data efficiency and generalization in agentic decision-making. citeturn1search2


## Emerging trends and common techniques

- Automated workflow generation/search: Several works (AFlow, Flow, MermaidFlow, SwarmAgentic) frame workflow construction as an optimization/search problem (MCTS, evolutionary programming, graph evolution, swarm/PSO), reducing manual engineering effort and targeting structural design as part of optimization. citeturn0search0turn0search2turn0search4turn1academia15

- Explicit intermediate representations and modularity: Papers emphasize graph-based or programmatic intermediate representations (AOV graphs, Mermaid, programmatic skills) to allow verification, modular replacement, and parallel execution. This improves interpretability and enables static checks before execution. citeturn0search2turn0search4turn1search3

- Safety, verification, and robustness: Researchers are explicitly addressing failure modes introduced by judges/critics and by unconstrained LLM-generated plans. Work includes adversarial/benchmark studies (WAFER-QA) and safety-constrained evolution to produce verifiable, executable workflows. citeturn0academia16turn0search4

- Design-time prediction and orchestration: Agentic Predictor and systems-focused work like Murakkab indicate a maturing stack—tools to predict workflow success and to map workflows efficiently onto compute/hardware to meet SLOs and cost constraints. These reduce trial-and-error and make deployment practical. citeturn1academia16turn1academia12

- Domain specialization and HITL checkpoints: Medical, economic, and CHAI-focused papers show a trend of embedding domain constraints, structured evidence pipelines, and strategic human-in-the-loop checks to ensure correctness and ethical compliance. citeturn0search5turn0search1turn0search3


## Evaluation practices and benchmarks

- New benchmarks and adversarial evaluation (e.g., WAFER-QA) are emerging to test judge/critic reliability and resilience to deceptive feedback. Several papers also use task suites spanning planning, web navigation, and domain-specific tasks for empirical comparison. citeturn0academia16turn1academia15

- Metrics vary: success rate, cost-efficiency (inference cost), convergence speed, executability (static verifiability), and resource usage (GPU/energy/cost) are all used depending on whether the paper emphasizes algorithmic generation, safety, or systems deployment. citeturn0search0turn0search4turn1academia12


## Open challenges identified across the literature

1. Robustness to adversarial/misleading feedback: Feedback/judge components can introduce failures even when base agents are strong — more defenses, judge calibration, and evidence-grounding are needed. citeturn0academia16

2. Balancing automation with human oversight: Fully automated generation (SwarmAgentic, AFlow) shows promise, but domain papers stress the need for HITL checkpoints in high-stakes settings. Determining where to place checks remains an open design problem. citeturn1academia15turn0search5

3. Verifiability and executability: LLMs can produce syntactically plausible but unexecutable plans; intermediate representations and static verification (Mermaid/graphs/program-based skills) are partial solutions but require richer domain models and tooling. citeturn0search4turn1search3

4. Efficient deployment and cost-awareness: Orchestration, resource mapping, and prediction are nascent; real-world deployment requires end-to-end systems that manage latency, cost, and energy in production SLOs. citeturn1academia12turn1academia16

5. Standardized benchmarks and cross-domain generalization: The field needs broader, well-adopted benchmarks that cover safety, executability, and real-world constraints to make progress comparable and cumulative. Several papers introduce benchmarks, but adoption is still early. citeturn0academia16turn1academia15


## Practical takeaways / recommendations for practitioners

- Use explicit, verifiable intermediate representations (graphs/programs) for workflows when possible to allow static checks and human review. citeturn0search4turn1search3

- Incorporate performance predictors and profiling early in pipeline design to avoid costly brute-force searches over workflow designs. Agentic Predictor-like models speed iteration. citeturn1academia16

- Add strategic HITL pauses for high-risk steps (decision points, evidence synthesis) rather than continuous oversight; design escalation pathways so humans see concise, actionable context. Domain papers show this improves reliability and adoption. citeturn0search5turn0search1

- Harden judge/critic components by grounding critiques in retrieval/evidence and by testing against adversarial critique suites (e.g., WAFER-QA) before deploying feedback-driven loops. citeturn0academia16

- When deploying at scale, decouple workflow specification from execution configuration (Murakkab-style) to enable cross-layer optimization of models, hardware, and SLOs. citeturn1academia12


## Short bibliography (selected 2025 preprints)

- Ming, Y., Ke, Z., Nguyen, X.-P., Wang, J., & Joty, S. (2025-06-03). Helpful Agent Meets Deceptive Judge: Understanding Vulnerabilities in Agentic Workflows. arXiv. citeturn0academia16
- Zhang, J. et al. (2024->2025 rev. 2025-04-15). AFlow: Automating Agentic Workflow Generation. arXiv. citeturn0search0
- Niu, B. et al. (2025-01-14). Flow: A Modular Approach to Automated Agentic Workflow Generation. arXiv. citeturn0search2
- Zheng, C. et al. (2025-05-29). MermaidFlow: Safety-Constrained Evolutionary Programming. arXiv. citeturn0search4
- Zhang, Y. et al. (2025-06-18). SwarmAgentic: Towards Fully Automated Agentic System Generation via Swarm Intelligence. arXiv. citeturn1academia15
- Trirat, P., Jeong, W., & Hwang, S. J. (2025-05-26). Agentic Predictor: Performance Prediction for Agentic Workflows. arXiv. citeturn1academia16
- (System) Murakkab (2025-08-22). Murakkab: Resource-Efficient Agentic Workflow Orchestration in Cloud Platforms. arXiv (preprint). citeturn1academia12
- Wang, Z. et al. (2025-03-21). MedAgent-Pro: Evidence-based Multi-modal Medical Diagnosis via Reasoning Agentic Workflow. arXiv. citeturn0search5
- Dawid, H. et al. (2025-04-13). Agentic Workflows for Economic Research: Design and Implementation. arXiv. citeturn0search1
- Caetano, A. et al. (2025-01-29). Agentic Workflows for Conversational Human-AI Interaction Design. arXiv. citeturn0search3
- Wang, Z. Z., Gandhi, A., Neubig, G., & Fried, D. (2025-04-09). Inducing Programmatic Skills for Agentic Tasks. arXiv. citeturn1search3
- Yang, X. et al. (2025-06-02). Agentic Episodic Control. arXiv. citeturn1search2


---
Notes: I focused on arXiv preprints and research-oriented system papers from 2025 (Jan–Aug 2025) that explicitly address construction, evaluation, safety, or deployment of agentic workflows. If you want, I can:
- Expand this into an annotated bibliography with short one-paragraph summaries and direct PDF links for each paper.
- Pull code repositories and run brief reproduction checks for a subset (AFlow, SwarmAgentic, MermaidFlow).
- Produce a slide deck (5–10 slides) summarizing trends and recommended next steps for a team.

