
## Model-View-Presenter (MVP) [1], [2], [3], [4], [5], [6]

MVP is an architectural pattern that addresses some of the drawbacks of the traditional MVC approach. It was first introduced in the 1990s as a specialization of MVC, focusing on improving the separation of concerns between the view and the model. MVP divides the application's components into three main parts:

- Model: Represents the data and business logic of the application, similar to the model in MVC. It is responsible for processing, storing, and managing data and implementing any necessary business rules. The model does not communicate directly with the view or presenter.
- View: Represents the user interface and presentation layer of the application. Like the view in MVC, its primary function is to display data fetched from the model. However, in MVP, the view is more passive and relies on the presenter for updates and user input handling. The view communicates only with the presenter and not with the model.
- Presenter: Acts as a bridge between the model and the view, taking on some of the controller's responsibilities in MVC. The presenter fetches data from the model and updates the view, ensuring the correct data presentation. Unlike the controller, the presenter also handles user input directly from the view and facilitates two-way communication between the view and the model.

The main difference between MVC and MVP lies in the controller and presenter's roles. In MVP, the presenter becomes more involved in user interactions and the flow of data between the view and the model, leaving the view as a passive component. This separation of concerns allows for better testability and modularity, as each component can be isolated and tested independently.

### Pros:
Improved separation of concerns between view and model.
The presenter facilitates better testability and modularity.
Each component can be modified or replaced without affecting others.
Better suited for applications with complex state or interaction requirements.

### Cons:
Increased complexity compared to traditional MVC, due to the presenter's added responsibilities.
Can lead to a larger codebase and the need for more boilerplate code.
Potential for communication overhead between the components.

![MVP](../images/presenter.png)



## Architectural Patterns: MVC, MVP, and MVVM Explained
- [1]: https://appmaster.io/blog/architectural-patterns-mvc-mvp-and-mvvm#model-view-presenter-mvp
| Link | https://appmaster.io/blog/architectural-patterns-mvc-mvp-and-mvvm#model-view-presenter-mvp |
|-|-|
| Retrieved | 2026-04-09 |

## Android Architecture with MVP or MVVM - Tutorial
- [2]: https://www.vogella.com/tutorials/AndroidArchitecture/article.html
| Link | https://www.vogella.com/tutorials/AndroidArchitecture/article.html |
|-|-|
| Retrieved | 2026-04-09 |

## MVP-Architektur – Model-View-Presenter erklärt: Struktur, Vorteile und Einsatzbereiche
- [3]: https://www.it-schulungen.com/wir-ueber-uns/wissensblog/mvp-architektur-model-view-presenter-erklaert-struktur-vorteile-und-einsatzbereiche.html
| Link | https://www.it-schulungen.com/wir-ueber-uns/wissensblog/mvp-architektur-model-view-presenter-erklaert-struktur-vorteile-und-einsatzbereiche.html |
|-|-|
| Retrieved | 2026-04-09 |

## Difference Between MVC and MVP Patterns
- [4]: https://www.baeldung.com/mvc-vs-mvp-pattern
| Link | https://www.baeldung.com/mvc-vs-mvp-pattern |
|-|-|
| Retrieved | 2026-04-09 |

## MVP Architecture
- [5]: https://www.notion.so/essentialbooks/MVP-Architecture-f2c2f7bba0a042dca350f9777169026d
| Link | https://www.notion.so/essentialbooks/MVP-Architecture-f2c2f7bba0a042dca350f9777169026d |
|-|-|
| Retrieved | 2026-04-09 |

## MVC vs MVP vs MVVM
- [6]: https://www.educative.io/answers/mvc-vs-mvp-vs-mvvm
| Link | https://www.educative.io/answers/mvc-vs-mvp-vs-mvvm |
|-|-|
| Retrieved | 2026-04-09 |
