
# Glossary

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
