from main import Team, Group, load_data, wwc2022_groups

def test_load_data():
    assert len(wwc2022_groups) == 0
    load_data()
    assert len(wwc2022_groups) == 8

def test_group_order():
    load_data()
    assert wwc2022_groups["A"].get_first_place().group_points >= wwc2022_groups["A"].get_second_place().group_points
    assert wwc2022_groups["A"].get_first_place().group_points >= wwc2022_groups["A"].get_n_place(3).group_points
    assert wwc2022_groups["A"].get_first_place().group_points >= wwc2022_groups["A"].get_n_place(4).group_points
    assert wwc2022_groups["A"].get_second_place().group_points >= wwc2022_groups["A"].get_n_place(3).group_points
    assert wwc2022_groups["A"].get_second_place().group_points >= wwc2022_groups["A"].get_n_place(4).group_points
    assert wwc2022_groups["A"].get_n_place(3).group_points >= wwc2022_groups["A"].get_n_place(4).group_points
