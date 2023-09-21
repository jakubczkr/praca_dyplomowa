from points_manager import PointsManager


def test_points_manager_get_rectangle():

    expected_result = [[10, 14], [5, 10]]

    points_manager = PointsManager([], [], [], [], [], [])

    points = [[10, 5], [12, 10], [14, 8]]

    actual_result = points_manager.get_rectangle(points)

    assert expected_result == actual_result


def test_points_manager_get_rectangle_one_point():

    expected_result = [[], []]

    points_manager = PointsManager([], [], [], [], [], [])

    points = [[5, 5]]

    actual_result = points_manager.get_rectangle(points)

    assert expected_result == actual_result
