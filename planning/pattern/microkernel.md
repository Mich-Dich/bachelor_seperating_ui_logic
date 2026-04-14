---
bibliography: code/refs.bib
---

## Microkernel Architecture

The microkernel architecture pattern (also known as the plug-in architecture) structures a system into two main parts: a minimal, bare-bones **core system** (the microkernel) and **plug-in modules** (or services) that provide additional functionality. The microkernel contains only the essential, platform-specific services required to make the system operational—such as low-level memory management, process scheduling, and inter-process communication (IPC). Everything else, including device drivers, file systems, network stacks, and user-facing features, runs as separate, isolated components outside the core kernel, typically in user space.

Communication between the microkernel and the plug-in modules happens through well-defined, stable interfaces (often using IPC or message passing). Plug-ins do not communicate directly with each other; they rely on the microkernel to mediate interactions. This design is common in operating systems (e.g., QNX, L4), but also appears in application architectures like web browsers (Chrome, Firefox), IDEs (Eclipse, Visual Studio Code), and ERP systems, where a small core can be extended with optional features.

The pattern emphasizes **modularity**, **extensibility**, and **fault isolation**. Because plug-ins are decoupled from the core and from each other, they can be developed, tested, deployed, and updated independently—without recompiling or restarting the entire system. However, the indirection introduced by IPC and context switches often comes at the cost of performance compared to monolithic designs.

### Pros:

* **Extensibility and Flexibility** – New features can be added as plug-ins without modifying the core system. Different configurations can be assembled for different use cases by simply including or excluding plug-ins.
* **Reliability and Fault Isolation** – A failure in one plug-in (e.g., a device driver or a user-space service) does not crash the whole system. The microkernel remains intact, and the failed component can often be restarted without rebooting.
* **Security** – The minimal core reduces the attack surface. Most services run with lower privileges in user space, so a compromise in one service does not automatically grant control over the entire system.
* **Maintainability and Testability** – Plug-ins can be developed, tested, and debugged in isolation. The clear separation of concerns makes the system easier to understand and evolve over time.
* **Portability** – Because the microkernel is extremely small and abstracts hardware dependencies, porting the system to a new platform requires only changes to the core, leaving most plug-ins untouched.

### Cons:

* **Performance Overhead** – Communication between the microkernel and plug-ins relies on IPC or message passing, which involves context switches and data copying. This indirection is slower than direct function calls in a monolithic kernel, and it can become a bottleneck for performance-sensitive operations.
* **Design and Implementation Complexity** – Defining stable, version-safe interfaces (contracts) between the core and plug-ins is challenging. Changing the core API can break all existing plug-ins, so the interfaces must be carefully designed for backward compatibility.
* **Increased Latency** – The extra layer of indirection makes latency less predictable, especially under heavy resource pressure. Real-time systems can mitigate this with careful tuning, but it remains a concern.
* **Inter-Plug-in Communication** – If plug-ins need to collaborate, they must go through the microkernel (or an indirect broker), which can lead to “chattiness” and further performance degradation. Direct plug-in-to-plug-in communication is typically not allowed.
* **Dependency Management** – Plug-ins may have hidden dependencies on each other or on specific versions of the core. Without proper tooling, managing these dependencies can become complex, especially as the number of plug-ins grows.


### Adaptation for the Present Use Case

After evaluating the classical microkernel pattern against the requirements of the three target applications (desktop, CI/CD, and microcontroller), it became evident that the full dynamic and process-isolated characteristics of the pattern introduce unnecessary complexity. The target environment is a firm-internal system where all executables are built from known source code and deployed in a controlled manner. Runtime discovery of plug-ins, inter-process communication (IPC), and separate process boundaries are therefore superfluous. The core benefits of the microkernel pattern—modularity, maintainability, and separation of concerns—can be retained while eliminating the classical drawbacks by moving to a **statically linked, single-process variant**.

#### Description of the Adapted Pattern

In this variant, the conceptual separation between a core system and plug-in modules is preserved, but the implementation differs fundamentally:

* **Plug-ins as static libraries** – All plug-ins are implemented as statically linked libraries (e.g., `.a` or `.lib`). The selection of which plug-ins to include is made at build time, not at runtime.
* **Single process, direct calls** – All components (core and plug-ins) reside in the same process address space. Communication occurs via ordinary function calls, eliminating context switches, serialisation overhead, and the need for inter-process synchronisation.
* **Multiple binaries from the same core** – Different executable images are produced by linking the identical core code with different combinations of static plug-in libraries. This allows purpose-built binaries for distinct use cases while maintaining a single source base for the core logic.
* **No runtime discovery** – Because all components are linked at build time, there is no plug-in registry, no dynamic lookup, and no failure mode for a missing plug-in. The set of available features is fixed and known at compilation time.

This adapted pattern trades runtime flexibility for compile-time predictability, performance, and simplicity. It is particularly well-suited for internal tooling, embedded systems, and automated pipelines where the configuration is known in advance and changes are managed through version control and the build system rather than through runtime mechanisms.

#### Mapping to the Three Target Applications

The adapted pattern directly addresses the distinct requirements of each application.

**Desktop Application (Reading, Editing, Executing Test Configurations)**
The core system is minimal and provides only orchestration and evaluation logic. All other functionality is implemented as static plug-in libraries: the graphical user interface, project management, configuration editing widgets, and additional features such as different communication methods. The core calls into these plug-in components as needed. The resulting executable links the core with all required plug-ins. Adding a new configuration format, a different communication method, or an alternative UI requires only the addition of a new static library and a rebuild; no dynamic loading mechanisms are needed.

**Microcontroller-Compatible Application (Execution Only)**
This use case benefits most from the adapted pattern, as classical microkernel IPC is prohibitively expensive on resource-constrained hardware. The core system is a minimal execution engine that manages hardware interfaces (UART, GPIO, timers) and invokes configuration-specific logic. Two plug-in variants align with the two described approaches:

* *Runtime configuration execution (flexible variant)* – The plug-in is a generic interpreter that reads configuration data from a communication interface (e.g., UART) and executes it on the fly. The core calls into this plug-in’s execution function directly. The binary is built once and can handle any configuration sent at runtime.

* *Precompiled configuration execution (optimised variant)* – The test configuration is compiled directly into the plug-in as constant data and hardcoded execution logic. The core links against this single, specialised plug-in. The resulting firmware image contains exactly one configuration, with zero parsing overhead at runtime. When the configuration changes, the plug-in source is updated and the firmware is rebuilt.

#### Conclusion of the Adaptation

After analysing the classical microkernel architecture and weighing it against the constraints of the three target applications, this thesis adopts a **statically linked, single-process variant** of the pattern. The adaptation preserves the essential advantages—modularity, separation of concerns, and maintainability—while eliminating the classical drawbacks of runtime overhead, IPC complexity, and dynamic discovery fragility. For a firm-internal system where all deployments are controlled and rebuilds are feasible, this variant offers the best trade-off and will be documented as a pragmatic reinterpretation of the microkernel pattern for resource-aware and closed-environment software systems.





## Microkernel Architecture Pattern in Rust: Principles, Benefits, and Implementation
- [X]: https://softwarepatternslexicon.com/rust/advanced-topics-and-emerging-technologies/the-microkernel-architecture-pattern/
| Link | https://softwarepatternslexicon.com/rust/advanced-topics-and-emerging-technologies/the-microkernel-architecture-pattern/ |
|-|-|
| Retrieved | 2026-04-13 |

## Microkernel Architecture Pattern - System Design
- [X]: https://www.geeksforgeeks.org/system-design/microkernel-architecture-pattern-system-design/
| Link | https://www.geeksforgeeks.org/system-design/microkernel-architecture-pattern-system-design/ |
|-|-|
| Retrieved | 2026-04-13 |

## Microkernels for Medical Devices: Security Benefits and Tradeoffs
- [X]: https://bluegoatcyber.com/blog/microkernels-medical-device-cybersecurity/
| Link | https://bluegoatcyber.com/blog/microkernels-medical-device-cybersecurity/ |
|-|-|
| Retrieved | 2026-04-13 |

## Operating System Architecture: Monolithic vs Microkernel Design Patterns
- [X]: https://codelucky.com/operating-system-architecture-monolithic-microkernel/#Advantages_of_Microkernels
| Link | https://codelucky.com/operating-system-architecture-monolithic-microkernel/#Advantages_of_Microkernels |
|-|-|
| Retrieved | 2026-04-13 |

## Microkernel Software Architecture
- [X]: https://bluetoaster.io/posts/microkernel-software-architecture/
| Link | https://bluetoaster.io/posts/microkernel-software-architecture/ |
|-|-|
| Retrieved | 2026-04-13 |

## Microkernel
- [X]: https://metapatterns.io/implementation-metapatterns/microkernel/
| Link | https://metapatterns.io/implementation-metapatterns/microkernel/ |
|-|-|
| Retrieved | 2026-04-13 |
