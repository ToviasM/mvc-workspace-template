# Python PySide5 MVC Workspace Template

This repository contains a Python Model-View-Controller (MVC) template using PySide5. This framework is structured to separate the logic of the application from the user interface, which helps in managing complex applications and improving code reuse.

## Structure

The MVC template is organized as follows:

- `mvc_template/`: Main directory for MVC architecture.
    - `panels/`: Contains panel definitions that act as modular components of the UI.
        - `example1_panel.py`: Example panel implementation.
        - `example2_panel.py`: Another example panel implementation.
        - `example3_panel.py`: Additional example panel implementation.
        - `panel.py`: Base panel class from which all panels inherit.
    - `template_controller.py`: Contains the application logic and handles interaction between the model and view.
    - `template_model.py`: Contains the data structure, including the view state and sockets for responding to view changes or panel/dock updates.
    - `template_view.py`: Manages the display and the user interface of the application.
- `.DS_Store`: File system file created by macOS.
- `main.py`: The entry point of the application that initializes the main window widget and sets up the MVC components.

## Features

- **Dynamic Widget Creation**: The main window widget dynamically creates right, left, and central widgets by selecting the appropriate panel based on the view state defined in the model.
- **Model State Management**: The model contains the current state of the view and has sockets to detect and respond to any changes in the view or the panel/dock.
- **Modular Panels**: Panels can be easily added or modified without affecting the core functionality of the application, facilitating scalability and maintenance.

## Getting Started

To use this MVC template in your application:

1. Clone this repository.
2. Install the requirements using `pip install -r requirements.txt` (ensure you have Python and pip installed).
3. Run `main.py` to start the application.
