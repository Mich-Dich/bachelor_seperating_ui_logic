
# Title: Analysis of different software architecture patterns for User-interface and Business-logic separation

## Abstract:
The primary objective of this bachelor thesis is to **analyze and compare software architectural patterns that distinctly separate business logic from user interface concerns**, with the goal of improving modularity, testability, and deployability across different execution environments. This work investigates well‑known design patterns such as **Model‑View‑Controller (MVC)**, **Model‑View‑Presenter (MVP)**, and **Model‑View‑ViewModel (MVVM)**, as well as additional architectural approaches such as layered/service‑oriented and component‑based structures, in order to identify their strengths and limitations for decoupling core functionality from presentation logic. [Source](https://appmaster.io/blog/architectural-patterns-mvc-mvp-and-mvvm#model-view-presenter-mvp)

The thesis applies these patterns to a practical case study: restructuring an existing application used to manipulate test benches and communicate with connected devices, so that the core testing engine (business logic) is made fully independent of any specific UI platform. The redesigned system will support:

* A traditional desktop application interface,
* A CI‑compatible command‑line or headless application capable of running on a build server, and
* A lightweight executable version suitable for deployment and execution on embedded microcontrollers.

The outcomes include both a theoretical evaluation of architectural alternatives and an empirical assessment of the chosen pattern in terms of modularity, scalability, and cross‑platform deployment. [Source](https://appmaster.io/blog/architectural-patterns-mvc-mvp-and-mvvm#model-view-presenter-mvp)




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

### 1. Modularity / Separation of Concerns
|Description | Measures how well the pattern isolates UI from business logic. |
|-|-|
|Sub-factors | Degree of coupling (tight vs loose) <br> Ease of replacing one module without affecting others <br> Support for multiple UI platforms |
|Metrics     | Number of dependencies between layers <br> Lines of code that need to change when modifying logic/UI |


### 2. Testability
|Description | Evaluates how easy it is to test business logic in isolation. |
|-|-|
|Sub-factors | Support for unit testing <br> Support for integration/system testing without UI <br> Availability of mocks/stubs for external dependencies |
|Metrics     | Percentage of logic testable without UI <br> Time required to set up automated tests |


### 3. Scalability / Extensibility
|Description | How well the architecture handles growth in features, complexity, or team size. |
|-|-|
|Sub-factors | Ease of adding new modules or features <br> Ability to support multiple users or devices <br> Support for parallel development by multiple teams |
|Metrics     | Number of new modules added without changing core <br> Time required to integrate new features |


### 4. Deployment Flexibility
|Description | Ability to deploy the system across different environments (desktop, embedded, CI/CD). |
|-|-|
|Sub-factors | Multi-platform support <br> Ability to produce different binaries from the same core <br> Remote vs local execution capability |
|Metrics     | Number of supported platforms <br> Ease of cross-compilation for embedded targets |


### 5. Performance / Efficiency
|Description | Runtime efficiency and memory usage, critical for constrained environments. |
|-|-|
|Sub-factors | Execution speed <br> Memory footprint <br> Overhead from layers/abstraction |
|Metrics     | CPU cycles for core operations <br>  Binary size for embedded targets <br>  Latency introduced by additional layers (MVC, MVP, MVVM) |


### 6. Complexity / Learning Curve
|Description | Measures how easy it is for developers to understand and maintain the pattern. |
|-|-|
|Sub-factors | Number of concepts to learn <br>  Code readability and maintainability <br>  Framework or tooling dependencies |
|Metrics     | Estimated onboarding time for new developer <br>  Number of design constructs needed for implementation |


### 7. Tooling and Language Support
|Description | How well the architecture fits the chosen language, compiler, and development tools. |
|-|-|
|Sub-factors | IDE/framework support for pattern <br>  Compiler/linker support for optimizations (dead code elimination, function sections) <br>  Build automation support |
|Metrics     | Number of tools/frameworks supporting the pattern <br>  Complexity of build scripts |


### 8. Reusability
|Description | Ability to reuse business logic or UI components across projects. |
|-|-|
|Sub-factors | Portability across projects or products <br> Independence from specific UI or deployment platform <br> Ease of adapting components for new requirements |
|Metrics     | Percentage of code reused across projects <br> Time to adapt for a new platform or project |



# Criteria Scoring

The scoring is based on how critical each criterion is to achieving the primary goal: **separating business logic to enable multiple deployment targets (Desktop, CI/CD, Embedded).**

| Name | Importance | Justification (Based on Thesis Text) |
|-|-|-|
| **Modularity** | **1.0** | **Fundamental Prerequisite.** The entire thesis premise is "distinctly separating business logic from user interface concerns." Without high modularity, it is impossible to create a "core testing engine (business logic) made fully independent." A score of 1.0 is assigned because this is the non-negotiable foundation for supporting the three distinct deployment environments (Desktop GUI, Headless CI, Embedded). |
| **Testability** | **0.95** | **Critical for CI/CD Viability.** The thesis specifically calls for a "CI‑compatible command‑line or headless application." For this to run on a build server, the business logic must be testable without a UI. Furthermore, the ability to run automated tests (unit/integration) on the core logic before deployment to embedded devices is essential for reliability in an automated pipeline. |
| **Scalability / Extensibility** | **0.6** | **Moderate Relevance.** While the thesis focuses on *deployment* diversity rather than user-load diversity, extensibility is relevant for future-proofing. The ability to "add new modules" or features to the core logic without breaking the three front-ends is a natural consequence of good separation. However, handling "multiple users" is not a stated requirement for the embedded or CI variants, lowering its score slightly compared to the others. |
| **Deployment Flexibility** | **1.0** | **Primary Success Metric.** The thesis explicitly lists three radically different environments: a desktop application, a CI-compatible headless server app, and a lightweight microcontroller version. The ability to "produce different binaries from the same core" is the main deliverable. This criterion directly measures the success of the architectural separation against the stated goal. |
| **Performance / Efficiency** | **0.9** | **Critical for Embedded Viability.** The microcontroller version is explicitly described as "resource-constrained," requiring "lightweight and optimized for efficiency." The thesis also discusses "Precompiled Configuration Execution" to minimize overhead. Therefore, metrics like binary size, memory footprint, and abstraction overhead are highly relevant; a pattern that adds too much overhead (e.g., heavy reflection or extensive runtime binding) would fail the embedded use case. |
| **Complexity** | **0.7** | **Practical Implementation Constraint.** While separation is the goal, the thesis must consider the "Learning Curve" and "Maintainability." The embedded environment (C/C++ typically) often lacks the complex frameworks (like data binding in MVVM) that desktop environments (C#/Java) enjoy. If the architectural pattern introduces complexity that makes cross-compilation or debugging on the microcontroller difficult, it becomes a barrier to implementation. |
| **Tooling** | **0.5** | **Context Dependent.** The score here reflects a balance. Tooling is vital for the embedded target (cross-compilation support, linker script control for dead code elimination) and the desktop target (IDE support). However, the architectural pattern itself is often abstract enough to be implemented in any language. While important for execution, it is slightly less of a *theoretical* evaluation criterion than the others listed, as the thesis allows for selecting the pattern *based on* toolchain constraints. |
| **Reusability** | **0.9** | **Core Value Proposition.** The goal is to "reuse business logic" across three distinct applications. The thesis emphasizes that the core testing engine should be independent of the UI platform. High reusability ensures that the investment in developing the test configuration logic is leveraged across the Desktop GUI, the CI server, and the Microcontroller without rewriting the core algorithms. |





# random thoughts:
I write an application for my firm. The application allows one to manipulate test benches by communicating with connected devices.
The main Focus of this bachelor thesis is the separation between engine and UI.
Identifying 3 widely used patterns for separations and comparing them (with focus on what the Firm want for the future).
Then applying one of the patterns in a hand-on example.

The bachelor should not be firm specific. it should be about the work, leaving any mention of a firm out of the title/abstract

## use Static Lib:
The business logic is developed and stored as a **static library**. One or multiple executable are then build that use this lib, such as a general purpose application for PC development and a smaller application that can run on a microprocessor and only executes a predefined test-case/test-suite





# Static Library Structure and Linking

A static library should contain many small object files because of how linking works:
- **Archive Level**: The linker scans the static library for specific `object files` containing symbols referenced by the executable. Only those object files are pulled in-unreferenced object files are discarded.
- **Object Level**: Once an object file is included, `its entire contents` are linked into the final binary. This is why library designers are advised to place one function per source file: it gives the linker finer granularity to avoid including unused code.

There are way to control the linking and exclude unused code but it relies on the compiler used:
- **Function Level (with optimizations)**: Even after an object file is included, unused code within it can be eliminated using `Dead Code Elimination`. Compiler flags like `-ffunction-sections` (GCC/Clang) place each function in its own section, and the linker flag `-Wl,--gc-sections` garbage-collects unused sections, discarding individual functions that are never called.






