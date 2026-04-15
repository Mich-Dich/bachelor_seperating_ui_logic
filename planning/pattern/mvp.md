---
bibliography: code/refs.bib
---

## Model-View-Presenter (MVP)

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

[@team2023architec] [@stackoverflowblog2023keep] [@mehrotranodateundersta] [@holmströmnodateis] [@duggu2023mvp]