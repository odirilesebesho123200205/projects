from mastermind import compare_codes


def test_correct_codes():
    megacode = "1293847102937485"
    for i in range(1, len(megacode)):
        assert compare_codes(megacode[:i], megacode[:i]) == (i, 0)


def test_simple_incorrect():
    assert compare_codes("1234", "5678") == (0, 0)


def test_rearrange_no_duplicates():
    assert compare_codes("1234", "4321") == (0, 4)


def test_complex_duplicates():
    assert compare_codes("1122", "2111") == (1, 2)