
# Evaluation Categories

## 1. Separation
| Description | Measures how well the pattern isolates UI from business logic. |
|-|-|
| Sub-factors | Degree of coupling (tight vs loose) <br> Ease of replacing one module without affecting others <br> Support for multiple UI platforms |
| Metrics | Number of dependencies between layers <br> Lines of code that need to change when modifying logic/UI |

## 2. Scalability
| Description | How well the architecture handles growth in features, complexity. |
|-|-|
| Sub-factors | Ease of adding new modules or features <br> Ability to support multiple users or devices |
| Metrics | Number of new modules added without changing core <br> Time required to integrate new features |

## 3. Extensibility
| Description | How well the architecture accommodates changes in team size (e.g., scaling from a single developer to multiple parallel teams) and onboarding time of new members. |
|-|-|
| Sub-factors | Degree of modularity for independent task assignment<br>Learning curve for new developers<br>Support for concurrent development on different features without merge conflicts<br>Ability to split the system into sub‑teams working on isolated components |
| Metrics | Number of independent modules / components <br> Average time (or lines of code) a new developer needs to understand before making a safe change <br> Number of team members that can work in parallel on different modules without coordination overhead |

## 4. Deployment Flexibility
| Description | Ability to deploy the system across different environments (desktop, embedded, headless server/container). |
|-|-|
| Sub-factors | Multi-platform support <br> Ability to produce different binaries from the same core <br> Remote vs local execution capability |
| Metrics | Number of supported platforms <br> Ease of cross-compilation for embedded targets |

## 5. Performance / Efficiency
| Description | Runtime performance and memory usage, critical for constrained environments. |
|-|-|
| Sub-factors | Execution speed <br> Memory footprint <br> Overhead from layers/abstraction |
| Metrics | Binary size for embedded targets <br> Latency introduced by additional layers (virtual function call vs REST call) |

## 6. Tooling and Language Support
| Description | How well the architecture fits the language, compiler, and development tools. |
|-|-|
| Sub-factors | IDE/framework support for pattern <br> Compiler/linker support for optimizations (dead code elimination, function sections) <br> Build automation support |
| Metrics | Number of tools/frameworks supporting the pattern <br> Complexity of build scripts |

<!-- Scales with Separation
## 7. Reusability
| Description | Ability to reuse business logic or UI components across projects. |
|-|-|
| Sub-factors | Portability across projects or products <br> Independence from specific UI or deployment platform <br> Ease of adapting components for new requirements |
| Metrics | Percentage of code reused across projects <br> Time to adapt for a new platform or project |
## 2. Testability
| Description | Evaluates how easy it is to test business logic in isolation. |
|-|-|
| Sub-factors | Support for unit testing <br> Support for integration/system testing without UI <br> Availability of mocks/stubs for external dependencies |
| Metrics | Percentage of logic testable without UI <br> Time required to set up automated tests |
-->


# Category Priority

The priority is based on how critical each criterion is to achieving the primary goal: **separating UI and business logic to enable multiple deployment targets (Desktop, headless server, Embedded).**

| Name | Priority | Justification (Based on Thesis Text) |
|-|-|-|
| **Separation** | **1.00** | **Fundamental Prerequisite.** The entire thesis premise is distinctly separating business logic from user interface concerns. Without high Separation, it is impossible to create a core testing engine (business logic) made fully independent. A score of 1.0 is assigned because this is the non-negotiable foundation for supporting the three distinct deployment environments (Desktop GUI, Headless CI, Embedded). |
| **Scalability** | **0.50** | **Moderate Relevance.** While the thesis focuses on *deployment* diversity rather than user-load diversity, extensibility is relevant for future-proofing. The ability to add new modules or features to the core logic without breaking the three front-ends is a natural consequence of good separation. However, handling multiple users is not a stated requirement for the embedded or CI variants, lowering its score slightly compared to the others. |
| **Extensibility** | **0.50** | **Moderate Relevance**. The thesis does not explicitly require scaling to large or parallel teams. However, the ability to accommodate changes in team size becomes relevant when the architecture is used in real‑world projects beyond the thesis scope. Thus, Extensibility supports future‑proofing but is not a make‑or‑break criterion. |
| **Deployment Flexibility** | **1.00** | **Primary Success Metric.** The thesis explicitly lists three radically different environments: a desktop application, a CI-compatible headless server app, and a lightweight microcontroller version. The ability to produce different binaries from the same core is the main deliverable. This criterion directly measures the success of the architectural separation against the stated goal. |
| **Performance / Efficiency** | **1.00** | **Critical for Embedded Viability.** The microcontroller version is explicitly described as resource-constrained, requiring lightweight and optimized for efficiency. The thesis also discusses Precompiled Configuration Execution to minimize overhead. Therefore, metrics like binary size, memory footprint, and abstraction overhead are highly relevant; a pattern that adds too much overhead (e.g., heavy reflection or extensive runtime binding) would fail the embedded use case. |
| **Tooling** | **0.25** | **Context Dependent.** The score here reflects a balance. Tooling is vital for the embedded target (cross-compilation support, linker script control for dead code elimination) and the desktop target (IDE support). However, the architectural pattern itself is often abstract enough to be implemented in any language. While important for execution, it is slightly less of a *theoretical* evaluation criterion than the others listed, as the thesis allows for selecting the pattern *based on* toolchain constraints. |
<!-- | **Testability** | **1.00** | **Critical for CI/CD Viability.** The thesis specifically calls for a CI‑compatible command‑line or headless application. For this to run on a build server, the business logic must be testable without a UI. Furthermore, the ability to run automated tests (unit/integration) on the core logic before deployment to embedded devices is essential for reliability in an automated pipeline. | -->
<!-- | **Reusability** | **0.50** | **Core Value Proposition.** The goal is to reuse business logic across three distinct applications. The thesis emphasizes that the core testing engine should be independent of the UI platform. High reusability ensures that the investment in developing the test configuration logic is leveraged across the Desktop GUI, the CI server, and the Microcontroller without rewriting the core algorithms. | -->




# For Text
Testability and Reusability were a concern but were not included in the Evaluation Categories as separate categories because they scale very closely with Separation


To Seriously evaluate the different Arcetecture pattern would require a Software arcetecture for every pattern. That would take too much time for this bachelor thesis, so it was decided to create a preliminary evaluation based on publicly available resources and only create a deeper Software arcetecture for each candidate pattern, not to comprehensive, just enough to compare.


