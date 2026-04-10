
## Model-View-Controller (MVC) [Source](https://appmaster.io/blog/architectural-patterns-mvc-mvp-and-mvvm#model-view-presenter-mvp)

MVC is one of the software industry's most widely known and adopted architectural patterns. It was first introduced in the late 1970s by Trygve Reenskaug, a Norwegian computer scientist, and has since become a staple in application architecture. The pattern facilitates the separation of concerns by dividing the application into three main components:

- Model: Represents the data and business logic of the application. It is responsible for processing, storing, and managing data and implementing any necessary business rules. The model is independent of the user interface and does not directly communicate with the view or controller.
- View: Represents the application's user interface (UI) and presentation layer. The view's primary function is to display the data fetched from the model. It does not directly access the model but instead receives updates through the controller. Views can have multiple visual representations of the same data, enabling greater flexibility and adaptability.
- Controller: Acts as the intermediary between the model and the view. The controller receives user input from the view, processes it, and updates the model. Once the model is updated, it notifies the controller, which then refreshes the view with new data. The controller's primary responsibility is to manage application flow and keep the model and view in sync. MVC architecture promotes loosely coupled components, improving application maintainability and testing.

Since the model, view, and controller are independent, each component can be modified or replaced without affecting others. This separation of concerns also promotes code reuse and modular development, as components can be easily rearranged and combined to create new functionality. In an MVC application, communication between components primarily follows the observer pattern. The view registers with the controller as an observer, while the model registers with the controller as a subject. When the model changes, it notifies the controller, which then updates the view accordingly.

### Pros:
Separation of concerns improves code maintainability and reusability.
Loose coupling between components allows easy modification and replacement.
Supports multiple visual representations of the same data.
Promotes modular development and code reuse.

### Cons:
The controller can become a bottleneck for complex applications with many user interactions.
Can be difficult to implement for applications with complicated state or interaction requirements.

![MVC](../images/controller.png)





## Architectural Patterns: MVC, MVP, and MVVM Explained
- [1]: https://appmaster.io/blog/architectural-patterns-mvc-mvp-and-mvvm#model-view-presenter-mvp
| Link | https://appmaster.io/blog/architectural-patterns-mvc-mvp-and-mvvm#model-view-presenter-mvp |
|-|-|
| Retrieved | 2026-04-09 |

## Difference Between MVC and MVP Patterns
- [2]: [www.XXXXXXXXX.com](https://www.baeldung.com/mvc-vs-mvp-pattern)
| Link | https://www.baeldung.com/mvc-vs-mvp-pattern |
|-|-|
| Retrieved | 2026-04-09 |

## MVC vs MVP vs MVVM
- [3]: https://www.educative.io/answers/mvc-vs-mvp-vs-mvvm
| Link | https://www.educative.io/answers/mvc-vs-mvp-vs-mvvm |
|-|-|
| Retrieved | 2026-04-09 |
