from coordinate_calculator import CoordinatesCalculator


def test_coordinates_calculator_calculate():

    expected_result = ([7, 20], [0, 25])

    coordinate_calculator = CoordinatesCalculator()

    first_coords = [10, 15, 20]
    second_coords = [5, 15, 30]

    actual_result = coordinate_calculator.calculate(first_coords, second_coords)

    assert expected_result == actual_result


def test_coordinates_calculator_calculate_different_order():

    expected_result = ([0, 25], [7, 20])

    coordinate_calculator = CoordinatesCalculator()

    first_coords = [5, 15, 30]
    second_coords = [10, 15, 20]

    actual_result = coordinate_calculator.calculate(first_coords, second_coords)

    assert expected_result == actual_result


def test_coordinates_calculator_calculate_negative_parameters():
    expected_result = ([], [])

    coordinate_calculator = CoordinatesCalculator()

    first_coords = [5, 15, 20]
    second_coords = [5, 30, 15]

    actual_result = coordinate_calculator.calculate(first_coords, second_coords)

    assert expected_result == actual_result


def test_coordinates_calculator_calculate_not_sorted_parameters():
    expected_result = ([], [])

    coordinate_calculator = CoordinatesCalculator()

    first_coords = [5, 15, 20]
    second_coords = [5, 30, 15]

    actual_result = coordinate_calculator.calculate(first_coords, second_coords)

    assert expected_result == actual_result
