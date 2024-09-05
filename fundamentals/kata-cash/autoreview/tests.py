from cash_register import change


def test_easy_change():
    assert change(100_00, 100_00) == {}
    assert change(50_00,  100_00) == {50_00: 1}
    assert change(20_00,  100_00) == {50_00: 1, 20_00: 1, 10_00: 1}


def test_property_change_sums_to_difference():
    for i in range(1000):
        price = 100_00
        payment = 100_00 + 5 * i
        change_dict = change(price, payment)
        assert sum(denom * amount for denom, amount in change_dict.items()) == payment - price