
## Model-View-Adapter (MVA)
The MVA pattern enforces a strict separation of concerns by mandating that the Model and View never communicate directly, with all interactions passing through an Adapter. This makes it a pure implementation of the Mediator pattern. While this design excels at decoupling UI from business logic, it comes with trade-offs.

**Pros:**
- **Complete Decoupling of UI and Business Logic:** The View and Model have no direct knowledge of each other, preventing any unwanted coupling. This makes it easier to change one without impacting the other. [1]
- **High Reusability and Flexibility of the Model:** The Model is intentionally oblivious to the View, making it highly reusable across multiple, radically different UI platforms (e.g., Qt, GTK+, MFC) using the same or different Adapters. [2]
- **Simple Debugging:** The flow of communication is artificially constrained to pass through a central hub (the Adapter), creating a linear and predictable data flow that is easy to evaluate and debug. [3]

**Cons:**
- **Additional Complexity (Overhead):** The strict separation and need to funnel all communication through an Adapter introduces significant boilerplate code and complexity. [4]
- **Risk of Adapter Bloat:** The Adapter, as the sole intermediary, can accumulate too many responsibilities as the application grows, potentially becoming a large, monolithic, and hard-to-maintain class. The Hacker Read page notes this as a common problem where frameworks like Ruby on Rails see "logic pushed down into the model," but the same risk applies to the Adapter becoming a "fat" mediator. [5]


**Score: 9/10**

**Reasoning:**
MVA achieves **complete decoupling** between UI and business logic — the Model and View have no direct knowledge of each other, and all communication passes through the Adapter. This is theoretically stronger than MVP and MVVM. However, the risk of **Adapter bloat** (the mediator accumulating excessive logic) can, in practice, lead to business logic leaking out of the Model, partially degrading separation. The added complexity and boilerplate do not directly harm separation but prevent a perfect 10.




## 2.5.1 Model-View-Adapter (MVA, Mediated MVC, Model-Mediator-View)
- [1]: https://stefanoborini.com/book-modelviewcontroller/02-mvc-variations/05-variations-on-the-triad/01-model-view-adapter.html
| Link | https://stefanoborini.com/book-modelviewcontroller/02-mvc-variations/05-variations-on-the-triad/01-model-view-adapter.html |
|-|-|
| Retrieved | 2026-04-10 |
| Quote for [scoring/separation/MVA/pro/Complete Decoupling of UI and Business Logic] | "The Model and the View do not hold references to each other, they do not exchange data nor interact directly." |

## Model–view–adapter
- [2]: https://handwiki.org/wiki/Model%E2%80%93view%E2%80%93adapter
| Link | https://handwiki.org/wiki/Model%E2%80%93view%E2%80%93adapter |
|-|-|
| Retrieved | 2026-04-10 |
| Quote for [scoring/separation/MVA/pro/High Reusability and Flexibility of the Model] | "This separation of concerns permits a wide variety of different views to indirectly access the same model either via exactly the same adapter or via the same class of adapters." |

## XXXXXXX
- [3]: https://www.bookstack.cn/read/modelviewcontroller-src/02_mvc_variations-variations_on_the_triad-10_model_view_adapter.md
| Link | https://www.bookstack.cn/read/modelviewcontroller-src/02_mvc_variations-variations_on_the_triad-10_model_view_adapter.md |
|-|-|
| Retrieved | 2026-04-10 |
| Quote for [scoring/separation/MVA/pro/Simple Debugging] | "the communication network is artificially constrained, making it easier to evaluate and debug" |

## Module 0259: The Model-View-Adapter architecture
- [4]: https://power.arc.losrios.edu/~auyeunt/teaches/modules/0259/module.html
| Link | https://power.arc.losrios.edu/~auyeunt/teaches/modules/0259/module.html |
|-|-|
| Retrieved | 2026-04-10 |
| Quote for [scoring/separation/MVA/pro/Additional Complexity (Over-engineering)] | "The MVA architecture needs some overhead" |
