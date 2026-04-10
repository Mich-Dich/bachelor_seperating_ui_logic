# Roadmap

## Phase 1: Foundation & Analysis (Weeks 1-4)

**Week 1: Literature & Pattern Deep Dive**
- [X] Systematic review of classical presentation-separation patterns (e.g., MVC, MVP, MVVM).
- [X] Investigation of domain-centric architectures (e.g., Hexagonal, Onion, Clean Architecture).
- [X] Review of plugin-based and facade-oriented patterns for UI-BL separation.
- [X] Documentation of core characteristics, pros and cons for each pattern.

**Week 2: Definition of Evaluation Framework**
- [X] Identification of evaluation criteria relevant to the thesis objectives (e.g., separation quality, testability, maintainability, deployment flexibility, resource overhead).
- [X] Assignment of relative weights to each criterion based on the project context.
- [X] Definition of a scoring or ranking system for patterns.

**Week 3: Preliminary Pattern Evaluation**
- [ ] Application of the evaluation framework to all identified patterns using publicly available resources (literature, case studies, documentation).
- [ ] Calculation of preliminary scores for each pattern.
- [ ] Selection of the top three patterns for deeper architectural design.

**Week 4: In-Depth Analysis of Top Three Patterns**
- [ ] Refinement of understanding for the three selected patterns, focusing on implementation mechanics.
- [ ] Identification of potential challenges specific to each pattern regarding the three target deployments (desktop GUI, headless, microcontroller).
- [ ] Initial risk assessment for each pattern.

## Phase 2: Core Architecture Design (Weeks 5-7)

**Week 5: Architecture for Third-Best Pattern**
- [ ] Creation of a detailed software architecture diagram and component specification for the third-ranked pattern.
- [ ] Definition of interfaces between Business Logic (BL) and UI layers.
- [ ] Mapping of the pattern to the existing test bench control application context.

**Week 6: Architecture for Second-Best Pattern**
- [ ] Creation of a detailed software architecture diagram and component specification for the second-ranked pattern.
- [ ] Comparison of structural differences against the third-best pattern.
- [ ] Documentation of anticipated effects on deployment variants.

**Week 7: Architecture for Best (Selected) Pattern**
- [ ] Creation of a detailed software architecture diagram and component specification for the highest-ranked pattern.
- [ ] Formal justification for selecting this pattern as the basis for implementation.
- [ ] High-level design of how the selected pattern will accommodate all three deployment variants (desktop GUI, headless, microcontroller).

## Phase 3: Implementation of Three Variants (Weeks 8-15)

**Week 8-10: Implementation – Desktop GUI Variant**
- [ ] Setup of development environment and baseline project structure based on the selected pattern.
- [ ] Implementation of business logic core (processing, calculations, device communication).
- [ ] Implementation of graphical user interface, ensuring BL remains independent.
- [ ] Initial integration testing on desktop platform.

**Week 11-13: Implementation – Headless Variant**
- [ ] Adaptation of the existing BL core for headless operation (no UI framework).
- [ ] Implementation of a command-line interface, scriptable API, or service wrapper.
- [ ] Verification of operation on a build server or automated testing environment.
- [ ] Ensuring identical BL behavior compared to desktop variant.

**Week 14-15: Implementation – Microcontroller Variant**
- [ ] Porting or adapting the BL core to a resource-constrained environment (C, C++, or lightweight Python/Rust as appropriate).
- [ ] Implementation of a minimal UI (if required) or pure headless operation.
- [ ] Optimization for memory, processing, and storage constraints.
- [ ] Integration testing with connected test bench devices.

## Phase 4: Evaluation & Testing (Weeks 16-18)

**Week 16: Evaluation of Separation Quality & Maintainability**
- [ ] Application of quantitative metrics (e.g., coupling/cohesion analysis, layer call counts).
- [ ] Qualitative assessment of how well each variant maintains BL independence from UI frameworks.
- [ ] Comparison of code maintainability (e.g., time to locate a business rule, effort to change UI).

**Week 17: Evaluation of Testability & Automation Suitability**
- [ ] Assessment of unit testing ease for BL in isolation from UI.
- [ ] Demonstration of automated testing workflows using the headless variant.
- [ ] Measurement of test coverage and test execution speed across variants.

**Week 18: Cross-Variant Comparison & Documentation of Findings**
- [ ] Direct comparison of all three variants against the original evaluation criteria.
- [ ] Documentation of trade-offs observed (e.g., desktop GUI ease-of-use vs. microcontroller constraints).
- [ ] Final validation that the selected pattern meets the thesis objectives.

## Phase 5: Writing, Revision, & Submission (Weeks 19-22)

**Week 19: Complete First Draft of Thesis**
- [ ] Integration of all sections: introduction, analysis, evaluation framework, architecture designs, implementation details, evaluation results.
- [ ] Inclusion of diagrams, code excerpts, and comparison tables.

**Week 20: Internal Review & Self-Revision**
- [ ] Checking for logical consistency, clarity, and completeness.
- [ ] Verification that all claims are supported by evidence from earlier phases.
- [ ] Correction of technical errors and formatting.

**Week 21: Second Draft & Feedback Integration**
- [ ] Incorporation of feedback from supervisor (if available) or peer review.
- [ ] Refinement of abstract, conclusion, and future work sections.
- [ ] Final proofreading for language and citation accuracy.

**Week 22: Final Submission & Defense Preparation**
- [ ] Formatting according to institutional guidelines.
- [ ] Generation of final PDF and submission.
- [ ] Preparation of presentation slides and summary of key contributions.

## Milestones & Deliverables

| Week | Milestone |
|------|------------|
| 4 | Evaluation framework documented + top three patterns selected |
| 7 | Final pattern selection + architecture designs for all three candidates |
| 10 | Desktop GUI variant implemented and tested |
| 13 | Headless variant implemented and verified on build server |
| 15 | Microcontroller variant implemented |
| 18 | Evaluation completed, all data collected |
| 20 | First complete draft of thesis |
| 22 | Final submission |

## Critical Dependencies & Risks

- [ ] **Week 2-3:** Weighting of evaluation criteria must remain stable; changes later will invalidate pattern selection.
- [ ] **Week 14-15:** Microcontroller variant may require earlier prototyping if resource constraints are severe.
- [ ] **Week 16-18:** Evaluation requires that all three variants share identical business logic core; deviations must be documented.
- [ ] **Week 20-21:** Writing cannot be deferred until after implementation – continuous documentation is assumed throughout all phases.
