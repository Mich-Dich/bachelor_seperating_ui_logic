
## Model-View-Controller (MVC)

MVC achieves a fundamental separation between presentation and business logic, but this separation is not perfect. A significant point of contention is the often tight coupling between the View and the Controller, which can hinder maintainability and reduce the pattern's effectiveness in achieving true separation.

**Pros:**
- **Strong Domain/Presentation Separation**: MVC effectively enforces a clean separation between the domain model and the presentation layer (View + Controller). This allows the core business logic to remain independent of the user interface, improving modularity and making it easier to maintain or replace the UI without affecting the underlying model. [1]
- **Support for Multiple Views**: The pattern supports having multiple views for the same model, allowing data to be presented in different formats (e.g., a bar chart and a data table) without duplicating the underlying business logic. [2]

**Cons:**
- **View-Controller Tight Coupling**: The View and Controller are often tightly coupled, meaning they are highly interdependent and frequently change together. This close relationship hinders the individual reuse of each component and can make the system harder to modify, as a change in one often necessitates a change in the other. [3]
- **Controller "Bloat" and Logic Leakage**: In practice, Controllers frequently accumulate business logic that should reside in the Model. This "controller bloat" violates separation of concerns, making the code harder to test, reuse, and maintain as the Controller becomes a "God Object". [4]
- **Reduced Reusability**: The tight coupling between the View and Controller means they are rarely reused independently. A View is unlikely to be used without its specific Controller, limiting the pattern's flexibility and modularity. [3]

**Score: 5/10**

**Reasoning:**
MVC separates the Model from the View/Controller pair reasonably well, and it supports multiple views of the same model. However, the tight coupling between View and Controller (often they change together) and the frequent leakage of business logic into the Controller (“controller bloat”) significantly weaken the isolation of UI from business logic. Compared to MVP, MVC provides poorer separation because the Controller is less clearly distinct from the View and often ends up mixing presentation logic with domain rules, making testing and replacement harder.




## Applying the Model-View-Controller Pattern
- [1]: https://www.gamedeveloper.com/programming/applying-the-model-view-controller-pattern
| Link | https://www.gamedeveloper.com/programming/applying-the-model-view-controller-pattern |
|-|-|
| Retrieved | 2026-04-09 |
| Quote for [scoring/separation/MVC/pro/Strong Domain/Presentation Separation] | "This pattern isolates "domain logic" from input and presentation, permitting independent development, testing and maintenance of each." |

## Architectural Patterns: MVC, MVP, and MVVM Explained
- [2]: https://appmaster.io/blog/architectural-patterns-mvc-mvp-and-mvvm
| Link | https://appmaster.io/blog/architectural-patterns-mvc-mvp-and-mvvm |
|-|-|
| Retrieved | 2026-04-09 |
| Quote for [scoring/separation/MVC/pro/Support for Multiple Views] | "Views can have multiple visual representations of the same data, enabling greater flexibility and adaptability." |

## Discussion on: JavaScript vs JavaScript. Fight!
- [3]: https://practicaldev-herokuapp-com.global.ssl.fastly.net/peerreynders/comment/1hc4p
| Link | https://practicaldev-herokuapp-com.global.ssl.fastly.net/peerreynders/comment/1hc4p |
|-|-|
| Retrieved | 2026-04-09 |
| Quote for [scoring/separation/MVC/con/View-Controller Tight Coupling] | Citing the book "Pattern-Oriented Software Architecture Vol.1", noting a specific liability of MVC: "Intimate connection between view and controller. Controller and view are separate but closely-related components..." |
| Quote for [scoring/separation/MVC/con/Reduced Reusability] | Citing the book "Pattern-Oriented Software Architecture Vol.1", noting a specific liability of MVC: "It is unlikely that a view would be used without its controller, or vice-versa, with the exception of read-only views that share a controller that ignores all input." |

## Ruby on Rails Controller Patterns and Anti-patterns
- [4]: https://blog.appsignal.com/2021/04/14/ruby-on-rails-controller-patterns-and-anti-patterns.html?hmsr=joyk.com
| Link | https://blog.appsignal.com/2021/04/14/ruby-on-rails-controller-patterns-and-anti-patterns.html?hmsr=joyk.com |
|-|-|
| Retrieved | 2026-04-09 |
| Quote for [scoring/separation/MVC/con/Controller "Bloat" and Logic Leakage] | "The problem with putting too much logic in the controller is that you are starting to violate the Single Responsibility Principle (SRP). This means that we are doing too much work inside the controller." <br> "Here, 'fat' refers to the extensive code contained in the controller files, as well as the logic the controller supports. It is often considered an anti-pattern." |
