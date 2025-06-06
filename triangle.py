# triangle.py

def area_triangle(base: float, height: float) -> float:
    """
    Calculate the area of a triangle given base and height.
    Raises ValueError if base <= 0 or height < 0.

    - base must be > 0
    - height must be >= 0   (but we’ll also treat height <= 0 as invalid)
    """
    # Validation: base must be strictly positive
    if base <= 0:
        raise ValueError(f"Base must be > 0. Got base={base!r}")

    # Validation: height must be strictly positive (we do not accept zero or negative)
    if height <= 0:
        raise ValueError(f"Height must be > 0. Got height={height!r}")

    # Standard area formula: (base * height) / 2
    return (base * height) / 2.0


if __name__ == "__main__":
    # If someone runs this file directly, prompt for input:
    try:
        b_input = float(input("Enter base of triangle: "))
        h_input = float(input("Enter height of triangle: "))
        result = area_triangle(b_input, h_input)
        print(f"Area of triangle with base={b_input} and height={h_input} is: {result}")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
