
# Hexagonal Architecture (Ports and Adapters)

Hexagonal Architecture achieves **strong theoretical separation** between UI and business logic through its ports-and-adapters model. In practice, however, the separation is not absolute, and some issues temper its perfect score.

**Pros:**
- **Loose coupling through ports:** Components are loosely coupled via ports and adapters, avoiding the tight coupling typical of traditional layered architectures. [1] [2]
- **UI independence:** The business logic has no dependencies on UIs, making it possible to change the technology stack over time with limited or no impact on business logic. [3]
- **Multiple UI support:** Multiple UI implementations (e.g., website, native apps, CLI, test scripts) can share the same core business logic without modification. [4]
- **Testability:** Isolating UI from logic allows unit testing of business logic using in-memory adapter stubs and mocks without requiring a real UI or external systems. [5]

**Cons:**
- **Shared UI model across adapters:** Even when several UIs exist, the core typically contains a single UI model that all adapters must share, which can be problematic when different UI implementations have different data or filtering needs. [6]
- **Potential for tight coupling:** If ports are not designed with technology-agnostic abstractions, the intended loose coupling can degrade into a tighter coupling than anticipated. [7]
- **Domain logic leak risk:** Business logic can still seep into UI adapters if discipline is not maintained, partially defeating the separation goal. [8]
- **Additional maintenance overhead:** The extra adapter code required to maintain the separation is justified only when the application genuinely needs multiple input sources or technology replacements; otherwise, it becomes unnecessary maintenance overhead. [1]

**Score: 8/10**





## Hexagonal architecture pattern
- [1]: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/hexagonal-architecture.html#hexagonal-architecture-intent
| Link | https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/hexagonal-architecture.html#hexagonal-architecture-intent |
|-|-|
| Retrieved | 2026-04-08 |
| Quote for [Loose coupling through ports] | "It aims to create loosely coupled architectures where application components can be tested independently, with no dependencies on data stores or user interfaces (UIs). This pattern helps prevent technology lock-in of data stores and UIs. This makes it easier to change the technology stack over time, with limited or no impact to business logic. In this loosely coupled architecture, the application communicates with external components over interfaces called ports, and uses adapters to translate the technical exchanges with these components." |
| Quote for [UI independence] | "This pattern helps prevent technology lock-in of data stores and UIs. This makes it easier to change the technology stack over time, with limited or no impact to business logic." |
| Quote for [Multiple UI support] | "Multiple types of clients can use the same domain logic." |
| Quote for [Additional maintenance overhead] | "Maintenance overhead: The additional adapter code that makes the architecture pluggable is justified only if the application component requires several input sources and output destinations to write to, or when the inputs and output data store has to change over time. Otherwise, the adapter becomes another additional layer to maintain, which introduces maintenance overhead." |

## Beginner’s Guide to Hexagonal Architecture Diagram (Data Flow)
- [2]: https://blog.visual-paradigm.com/beginners-guide-to-hexagonal-architecture-diagram-data-flow/
| Link | https://blog.visual-paradigm.com/beginners-guide-to-hexagonal-architecture-diagram-data-flow/ |
|-|-|
| Retrieved | 2026-04-08 |
| Quote for [Loose coupling through ports] | The Hexagonal Architecture divides a software system into loosely coupled and interchangeable components. These components include the application core, database, user interface, test scripts, and interfaces with other systems |

## serodriguez68 / clean-architecture -> Part V - 2 - Architecture
- [3]: https://github.com/serodriguez68/clean-architecture/blob/master/part-5-2-architecture.md
| Link | https://github.com/serodriguez68/clean-architecture/blob/master/part-5-2-architecture.md |
|-|-|
| Retrieved | 2026-04-08 |
| Quote for [UI independence] | "Independent of the UI: The UI can change easily with no impact to the business rules. The UI can easily be replaced." |


## marc-gil / hexagonal-architecture -> Hexagonal Architecture
- [4]: https://github.com/marc-gil/hexagonal-architecture
| Link | https://github.com/marc-gil/hexagonal-architecture |
|-|-|
| Retrieved | 2026-04-08 |
| Quote for [Multiple UI support] | "This allows the same core logic to be used with different technologies in a seamless way" |

## Quality by design
- [5]: https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/improve-software-quality.html
| Link | https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/improve-software-quality.html |
|-|-|
| Retrieved | 2026-04-08 |
| Quote for [Testability] | "In hexagonal architecture, you test business logic in isolation, and use integration tests to test secondary adapters. You can use mock or fake adapters in your business logic tests." |

## Who does what and who lives where?
- [6]: https://softwareengineering.stackexchange.com/questions/405905/who-does-what-and-who-lives-where/405907#405907
| Link | https://softwareengineering.stackexchange.com/questions/405905/who-does-what-and-who-lives-where/405907#405907 |
|-|-|
| Retrieved | 2026-04-08 |
| Quote for [Shared UI model across adapters] | "But even if you have several UIs (e.g. website and native apps), you still have one UI model in the core. Filtering data or UI implementation specific calculations are a problem for the adapters or maybe the actual UI" |

## Hexagonal Architecture
- [7]: https://itnext.io/hexagonal-architecture-fe1250fb52be
| Link | https://itnext.io/hexagonal-architecture-fe1250fb52be |
|-|-|
| Retrieved | 2026-04-08 |
| Quote for [Potential for tight coupling] | "There is also a high risk to design a leaky abstraction — an SPI which looks generic but its contract matches that of the vendor used at the start of the project, making it much harder than expected to change the vendor." |

## Building Hexagonal Architecture for Scalable Solutions
- [8]: https://blog.dtdl.in/building-hexagonal-architecture-for-scalable-solutions-b20b4993a71b
| Link | https://blog.dtdl.in/building-hexagonal-architecture-for-scalable-solutions-b20b4993a71b |
|-|-|
| Retrieved | 2026-04-08 |
| Quote for [Domain logic leak risk] | "Front-end Challenges: The application’s business logic tends to seep into the user interface in the front end, leading to challenging testing due to its tight coupling with the UI" |
