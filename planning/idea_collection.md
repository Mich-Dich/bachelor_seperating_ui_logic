
# Title: Analysis of Software Architecture Patterns and Implementation of a Selected Pattern for User Interface and Business Logic Separation

## Abstract

The primary objective of this bachelor thesis is to analyze software architectural patterns that enforce a clear separation between business logic—the part of the system responsible for core processing, calculations, and device control—and user interface concerns. The focus is on ensuring high-quality boundaries between these two areas, which improves maintainability, clarity of responsibilities, and supports flexible deployment across different environments.

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



# random thoughts:
I write an application for my firm. The application allows one to manipulate test benches by communicating with connected devices.
The main Focus of this bachelor thesis is the separation between engine and UI.
Identifying 3 widely used patterns for separations and comparing them (with focus on what the Firm want for the future).
Then applying one of the patterns in a hand-on example.
The bachelor should not be firm specific. it should be about the work, leaving any mention of a firm out of the title/abstract




TODO:
roadmap
