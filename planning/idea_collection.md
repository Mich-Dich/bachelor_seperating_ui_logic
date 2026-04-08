
# Title: Analysis of Software Architecture Patterns and Implementation of a Selected Pattern for User Interface and Business Logic Separation

## Abstract

The primary objective of this bachelor thesis is to analyse software architectural patterns that enforce a clear separation between business logic—the part of the system responsible for core processing, calculations, and device control—and user interface concerns. The focus is on ensuring high-quality boundaries between these two areas, which improves maintainability, clarity of responsibilities, and supports flexible deployment across different environments.

The investigation covers a broad set of architectural styles, organized into classical presentation-separation patterns, domain-centric architectures, and plugin-based or facade-oriented patterns. For each style, the thesis examines how business logic can be designed to remain conceptually independent from UI frameworks, external services, and infrastructure details, while still being operable through UI platforms.

Based on this analysis, the thesis applies a selected architectural pattern to restructure an existing application used to control test benches and communicate with connected devices. The redesign ensures that the business logic is separated from the UI, while remaining accessible through it. The system is implemented to support three deployment variants, each containing the business logic:

* A desktop application with a graphical user interface, suitable for direct human interaction,
* A headless application without a user interface, designed to run on build servers and support automated testing workflows, and
* A lightweight executable for resource-constrained microcontrollers, which may include a minimal user interface if required.

The outcomes include a structured comparison of the architectural alternatives, a justification for selecting the chosen pattern, the implementation of that pattern across the deployment variants, and an evaluation of the implementation in terms of separation quality, maintainability, and its suitability for automated testing of connected systems.




# Targeted Applications

## Desktop Application for Reading, Editing, and Executing Test Configurations
This application is designed to run on a standard desktop computer and serves as the primary user-facing tool within the system. It provides a graphical user interface that enables users to create, modify, and manage test configurations in an intuitive manner.

In addition to editing capabilities, the application supports the execution of test configurations that are loaded dynamically from external sources at runtime. This allows users to validate and run tests without requiring recompilation or redeployment of the application.

The desktop application acts as a comprehensive environment for test development and execution, combining usability with flexibility. It is intended to support the full lifecycle of a test configuration, including creation, inspection, modification, and execution.


## CI/CD-Compatible Application for Reading and Executing Test Configurations
This application is intended to operate in automated environments such as continuous integration and continuous deployment (CI/CD) pipelines, typically on a server or build system.

Unlike the desktop variant, this version does not provide any functionality for editing test configurations. Instead, it focuses exclusively on reliably executing predefined configurations in a non-interactive, headless environment.

The application is designed to integrate seamlessly into automated workflows, enabling repeatable and consistent test execution as part of build and deployment processes. Since it runs in a controlled server environment, it is not subject to strict limitations regarding resource usage or application size. This allows for more extensive logging, diagnostics, and scalability features compared to embedded or constrained environments.


## Microcontroller-Compatible Application for Executing Test Configurations
This application targets resource-constrained embedded systems and is designed to execute previously defined test configurations on a microcontroller. Due to the limited computational power and memory available in such environments, the application must be lightweight and optimized for efficiency.

Two alternative approaches are considered for this use case:
* **Runtime Configuration Execution:**
  In this variant, the application receives test configurations via a communication interface such as UART, serial (COM), or similar protocols. The configuration is transmitted to the microcontroller at runtime and interpreted or executed directly. This approach provides flexibility, as test configurations can be changed without modifying the firmware.

* **Precompiled Configuration Execution:**
  In this optimized variant, the application is specifically tailored to a single test configuration. The configuration is integrated into the application prior to deployment, resulting in a highly efficient executable with minimal runtime overhead. However, this approach requires the firmware to be rebuilt and reflashed whenever the test configuration changes.

Both approaches represent different trade-offs between flexibility and performance, and their suitability depends on the specific constraints and requirements of the embedded environment.



# Evaluation Categories

### 1. Separation
| Description | Measures how well the pattern isolates UI from business logic. |
|-|-|
| Sub-factors | Degree of coupling (tight vs loose) <br> Ease of replacing one module without affecting others <br> Support for multiple UI platforms |
| Metrics | Number of dependencies between layers <br> Lines of code that need to change when modifying logic/UI |

### 2. Testability
| Description | Evaluates how easy it is to test business logic in isolation. |
|-|-|
| Sub-factors | Support for unit testing <br> Support for integration/system testing without UI <br> Availability of mocks/stubs for external dependencies |
| Metrics | Percentage of logic testable without UI <br> Time required to set up automated tests |

### 3. Scalability / Extensibility
| Description | How well the architecture handles growth in features, complexity, or team size. |
|-|-|
| Sub-factors | Ease of adding new modules or features <br> Ability to support multiple users or devices <br> Support for parallel development by multiple teams |
| Metrics | Number of new modules added without changing core <br> Time required to integrate new features |

### 4. Deployment Flexibility
| Description | Ability to deploy the system across different environments (desktop, embedded, headless server/container). |
|-|-|
| Sub-factors | Multi-platform support <br> Ability to produce different binaries from the same core <br> Remote vs local execution capability |
| Metrics | Number of supported platforms <br> Ease of cross-compilation for embedded targets |

### 5. Performance / Efficiency
| Description | Runtime performance and memory usage, critical for constrained environments. |
|-|-|
| Sub-factors | Execution speed <br> Memory footprint <br> Overhead from layers/abstraction |
| Metrics | CPU cycles for core operations <br> Binary size for embedded targets <br> Latency introduced by additional layers (MVC, MVP, MVVM) |

### 6. Tooling and Language Support
| Description | How well the architecture fits the language, compiler, and development tools. |
|-|-|
| Sub-factors | IDE/framework support for pattern <br> Compiler/linker support for optimizations (dead code elimination, function sections) <br> Build automation support |
| Metrics | Number of tools/frameworks supporting the pattern <br> Complexity of build scripts |

### 7. Reusability
| Description | Ability to reuse business logic or UI components across projects. |
|-|-|
| Sub-factors | Portability across projects or products <br> Independence from specific UI or deployment platform <br> Ease of adapting components for new requirements |
| Metrics | Percentage of code reused across projects <br> Time to adapt for a new platform or project |


# Category Priority

The priority is based on how critical each criterion is to achieving the primary goal: **separating UI and business logic to enable multiple deployment targets (Desktop, headless server, Embedded).**

| Name | Priority | Justification (Based on Thesis Text) |
|-|-|-|
| **Separation** | **1.00** | **Fundamental Prerequisite.** The entire thesis premise is distinctly separating business logic from user interface concerns. Without high Separation, it is impossible to create a core testing engine (business logic) made fully independent. A score of 1.0 is assigned because this is the non-negotiable foundation for supporting the three distinct deployment environments (Desktop GUI, Headless CI, Embedded). |
| **Testability** | **0.95** | **Critical for CI/CD Viability.** The thesis specifically calls for a CI‑compatible command‑line or headless application. For this to run on a build server, the business logic must be testable without a UI. Furthermore, the ability to run automated tests (unit/integration) on the core logic before deployment to embedded devices is essential for reliability in an automated pipeline. |
| **Scalability / Extensibility** | **0.60** | **Moderate Relevance.** While the thesis focuses on *deployment* diversity rather than user-load diversity, extensibility is relevant for future-proofing. The ability to add new modules or features to the core logic without breaking the three front-ends is a natural consequence of good separation. However, handling multiple users is not a stated requirement for the embedded or CI variants, lowering its score slightly compared to the others. |
| **Deployment Flexibility** | **1.00** | **Primary Success Metric.** The thesis explicitly lists three radically different environments: a desktop application, a CI-compatible headless server app, and a lightweight microcontroller version. The ability to produce different binaries from the same core is the main deliverable. This criterion directly measures the success of the architectural separation against the stated goal. |
| **Performance / Efficiency** | **1.00** | **Critical for Embedded Viability.** The microcontroller version is explicitly described as resource-constrained, requiring lightweight and optimized for efficiency. The thesis also discusses Precompiled Configuration Execution to minimize overhead. Therefore, metrics like binary size, memory footprint, and abstraction overhead are highly relevant; a pattern that adds too much overhead (e.g., heavy reflection or extensive runtime binding) would fail the embedded use case. |
| **Tooling** | **0.50** | **Context Dependent.** The score here reflects a balance. Tooling is vital for the embedded target (cross-compilation support, linker script control for dead code elimination) and the desktop target (IDE support). However, the architectural pattern itself is often abstract enough to be implemented in any language. While important for execution, it is slightly less of a *theoretical* evaluation criterion than the others listed, as the thesis allows for selecting the pattern *based on* toolchain constraints. |
| **Reusability** | **0.90** | **Core Value Proposition.** The goal is to reuse business logic across three distinct applications. The thesis emphasizes that the core testing engine should be independent of the UI platform. High reusability ensures that the investment in developing the test configuration logic is leveraged across the Desktop GUI, the CI server, and the Microcontroller without rewriting the core algorithms. |





# random thoughts:
I write an application for my firm. The application allows one to manipulate test benches by communicating with connected devices.
The main Focus of this bachelor thesis is the separation between engine and UI.
Identifying 3 widely used patterns for separations and comparing them (with focus on what the Firm want for the future).
Then applying one of the patterns in a hand-on example.
The bachelor should not be firm specific. it should be about the work, leaving any mention of a firm out of the title/abstract


## Glossary
| Term | Definition |
|------|-------------|
| **User Interface (UI)** | The part of an application that handles user interaction and presentation. In this thesis, UI is separated from business logic to allow different front‑ends (desktop, headless, embedded). |
| **Business Logic** | The core functionality of the application, independent of any presentation layer. In this case: the test engine that manipulates test benches and communicates with devices. |
| **Test Configuration** | A set of parameters, commands, or scripts that define a specific test case or test suite. Can be loaded dynamically (desktop/CI) or precompiled (embedded). |
| **Static Library** | A collection of object files (`.a` on Linux/macOS, `.lib` on Windows) that is linked directly into an executable at build time. Used to package the business logic for reuse across different applications. |
| **Dead Code Elimination (DCE)** | A compiler/linker optimization that removes functions or data that are never referenced. When combined with `-ffunction-sections` and `-Wl,--gc-sections`, it allows discarding unused code even from within an object file. |
| **Conditional Static Linking** | The technique of including or excluding specific modules (plugins) at compile time using preprocessor directives or build‑system logic, rather than at runtime. Essential for creating a lightweight embedded variant. |
| **Microkernel Architecture** | A pattern that separates a minimal core system from extensible modules (plugins). |
| **Headless Application** | An application that runs without a graphical user interface, typically in a server or CI/CD environment. CI/CD‑compatible variant reads and executes test configurations without editing capabilities. |
| **Embedded / Microcontroller Target** | A resource‑constrained environment (limited RAM, flash, CPU speed) where the test‑execution application must be lightweight. Two approaches: runtime configuration reception (flexible) or precompiled configuration (efficient). |
| **Cross‑compilation** | The process of compiling source code on one platform (e.g., x86 desktop) to produce an executable for another platform (e.g., ARM microcontroller). Relevant for building the embedded variant from the same codebase. |
| **Plugin** | An independent, replaceable module that extends the core system without modifying it. In a microkernel architecture, UI and optional features are implemented as plugins. |
| **LTO (Link‑Time Optimization)** | A compiler optimization that analyses the whole program during linking, enabling inlining and cross‑module dead code elimination. Particularly useful when statically linking many small object files. |
| **Service Provider Interface (SPI)** | A contract (interface) defined by the microkernel that plugins must implement to integrate with the core. Ensures loose coupling and testability. |
| **CI/CD Pipeline** | Continuous Integration / Continuous Deployment – an automated build, test, and deployment process. CI/CD‑compatible application is designed to run as a step in such a pipeline. |




#






















Judge the Onion Architecture pattern by:
### 1. Separation
| Description | Measures how well the pattern isolates UI from business logic. |
|-|-|
| Sub-factors | Degree of coupling (tight vs loose) <br> Ease of replacing one module without affecting others <br> Support for multiple UI platforms |
| Metrics | Number of dependencies between layers <br> Lines of code that need to change when modifying logic/UI |


Be realistic and very slightly pesimistic (dont invent problems, only if you find them in a web site, then you can lower the score).
- show your sources. what webside did you use for what argument.
- For every pro and contra point I NEED THE SOURCE WEBSITE.
- give me the used sources as a complete list at the end
- Use this style:

    short explanation text, a descrption of the evaluation

    **Pros:**
    - pro point [1]
    - pro point [2]

    **Con:**
    - con point [3]
    - con point [4]

    **Score: XX/10**

    [1]: [www.xxxxxxxxxx.com](www.xxxxxxxxxx.com)
    [2]: [www.yyyyyyyyyy.com](www.yyyyyyyyyy.com)
    [3]: [www.zzzzzzzzzz.com](www.zzzzzzzzzz.com)
    [4]: [www.aaaaaaaaaa.com](www.aaaaaaaaaa.com)



## Onion Architecture [Source](https://www.clarity-ventures.com/articles/onion-based-software-architecture)
Onion Architecture is closely related to Clean Architecture and organizes the system into **concentric layers centered around the domain model**, emphasizing that the **core business logic is completely isolated from infrastructure and UI concerns**.
* **Core Idea:** The domain model sits at the center, surrounded by layers like services, infrastructure, and UI. ([Clarity Ventures][2])
* **Dependency Rule:** All dependencies point inward toward the domain.
* **Layers:**
  * Domain (core logic)
  * Application services
  * Infrastructure (DB, APIs)
  * Presentation (UI)
* **Goal:** Protect the domain logic from external changes.








# Revision Count

|                      | Separ. | Testab. | Scalab. | Deploy. Flexib. | Perf. | Tooling and Lang. Supp. | Reusab. |
|----------------------|--------|---------|---------|-----------------|-------|-------------------------|---------|
| MVC                  |        |         |         |                 |       |                         |         |
| MVP                  |        |         |         |                 |       |                         |         |
| MVVM                 |        |         |         |                 |       |                         |         |
| Hexagonal            |        |         |         |                 |       |                         |         |
| Onion                |      1 |         |         |                 |       |                         |         |
| Front Controller     |        |         |         |                 |       |                         |         |
| Backend-for-Frontend |        |         |         |                 |       |                         |         |
| Model-View-Adapter   |        |         |         |                 |       |                         |         |
| Microkernel          |        |         |         |                 |       |                         |         |

