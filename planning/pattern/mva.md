
## Model-View-Adapter (MVA) [1] [2] [3] [4] [5]

The Model-View-Adapter pattern is a strict variation of Model-View-Controller (MVC) that enforces complete decoupling between the Model and the View. Instead of the View observing the Model directly, an **Adapter** (sometimes called a **Controller** in this variant) acts as the sole intermediary. The Adapter handles all user input, translates it into Model operations, and then explicitly updates the View with data retrieved from the Model.

Unlike classic MVC where the View can subscribe to Model events, MVA mandates that **the View and Model never communicate directly** – all interactions pass through the Adapter. This makes the pattern a pure implementation of the **Mediator** pattern. The Adapter holds references to both the Model and the View, and both components remain completely unaware of each other. As a result, the View can be built from generic, off‑the‑shelf widgets (e.g., buttons, lists) without any application‑specific logic, and the Model has no knowledge of how it is displayed.

### Pros:
- **Complete separation of concerns** – The Model, View, and Adapter each have well‑defined roles, improving maintainability.
- **Model obliviousness** – The Model does not need to know about the View or Adapter, making it highly reusable across different interfaces.
- **Increased flexibility** – Multiple views (even radically different ones) can be attached to the same Model because the Adapter coordinates all updates.
- **Simplified debugging** – All communication flows through a single mediator (the Adapter), so the data flow is linear and easier to trace.
- **View simplicity** – The View can be composed of generic UI components without any application‑specific logic, reducing duplication.

### Cons:
- **Additional complexity** – For small or simple applications, the strict separation introduces unnecessary boilerplate code.
- **Risk of “adapter bloat”** – As the application grows, the Adapter can accumulate too many responsibilities, becoming a large, hard‑to‑maintain class.
- **More upfront design** – Requires careful architectural planning; it is not a pattern you can adopt incrementally.
- **Performance overhead** – Every interaction must pass through the Adapter, potentially adding extra method calls and indirection.
- **Not suitable for trivial UI** – If the View and Model are tightly coupled by nature (e.g., a simple settings dialog), MVA can feel over‑engineered.




## Model–view–adapter
- [1]: https://en.wikipedia.org/w/index.php?title=Model%E2%80%93view%E2%80%93adapter&oldid=882794684
| Link | https://en.wikipedia.org/w/index.php?title=Model%E2%80%93view%E2%80%93adapter&oldid=882794684 |
|-|-|
| Retrieved | 2026-04-10 |

## 2.5.1 Model-View-Adapter (MVA, Mediated MVC, Model-Mediator-View)
- [2]: https://stefanoborini.com/book-modelviewcontroller/02-mvc-variations/05-variations-on-the-triad/01-model-view-adapter.html
| Link | https://stefanoborini.com/book-modelviewcontroller/02-mvc-variations/05-variations-on-the-triad/01-model-view-adapter.html |
|-|-|
| Retrieved | 2026-04-10 |

## Model View Adapter
- [3]: https://www.bookstack.cn/read/modelviewcontroller-src/02_mvc_variations-variations_on_the_triad-10_model_view_adapter.md
| Link | https://www.bookstack.cn/read/modelviewcontroller-src/02_mvc_variations-variations_on_the_triad-10_model_view_adapter.md |
|-|-|
| Retrieved | 2026-04-10 |

## Model–view–adapter
- [4]: https://handwiki.org/wiki/Model%E2%80%93view%E2%80%93adapter
| Link | https://handwiki.org/wiki/Model%E2%80%93view%E2%80%93adapter |
|-|-|
| Retrieved | 2026-04-10 |

## Module 0259: The Model-View-Adapter architecture
- [5]: https://power.arc.losrios.edu/~auyeunt/teaches/modules/0259/module.html
| Link | https://power.arc.losrios.edu/~auyeunt/teaches/modules/0259/module.html |
|-|-|
| Retrieved | 2026-04-10 |
