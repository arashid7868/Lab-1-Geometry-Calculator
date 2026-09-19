# Lab 1 - Geometry Calculator

## Chapter 8 Programming Assignment

This project implements Option 2 of the Chapter 8 Lab 1 assignment: a menu-driven Geometry Calculator using Python functions and separate modules.

### Files

- `Lab1_arashid7868-2.py` - Main menu-driven application.
- `circle.py` - Circle area and circumference functions.
- `rectangle.py` - Rectangle area and perimeter functions.

### Features

- Calculate circle area.
- Calculate circle circumference.
- Calculate rectangle area.
- Calculate rectangle perimeter.
- Validate positive numeric inputs.
- Handle invalid menu choices without crashing.
- Demonstrate importing functions from separate Python modules.
- Use aliases because both `circle.py` and `rectangle.py` contain a `calc_area()` function.

### Running the Program

Make sure all three Python files are in the same folder. From that folder, run:

```text
python Lab1_arashid7868-2.py
```

If `python` is not recognized on Windows, try:

```text
py Lab1_arashid7868-2.py
```

### Testing

The program can be tested with:

- Circle radius: `7`
- Rectangle width: `10`
- Rectangle height: `5`
- Invalid numeric input such as `abc`
- Invalid positive-number input such as `0` or `-5`
- Invalid menu choices such as `9`
- Exit option: `5`
