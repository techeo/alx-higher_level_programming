# Python - Almost A Circle

In this project, I utilized Python object-oriented programming to create three classes representing rectangles and squares, accompanied by a custom test suite using `unittest`.

## Tests

* [tests/test_models](./tests/test_models): Contains test files for each class.

## Classes

### Base

* Private class attribute `__nb_objects = 0`.
* Public instance attribute `id`.
* Constructors, static and class methods for JSON and CSV serialization/deserialization.

### Rectangle

* Inherits from `Base`.
* Attributes for width, height, x, and y.
* Methods for area calculation, display, update, and dictionary representation.

### Square

* Inherits from `Rectangle`.
* Constructor with size parameter.
* Methods inherited from `Rectangle`.

