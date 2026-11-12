import ex2

def test_find_min_max():
    input = ["5", "6", "7"]
    test = (5.0 , 7.0)
    result = ex2.calc_min_max_temperature(input)

    assert(result == test)

def test_calc_average():
    input = ["5", "6", "7"]
    test = (6)
    result = ex2.calc_average_temperature(input)

    assert(result == test)

def test_calc_median_temperature_odd():
    input = [1, 3, 5]
    test = 3
    result = ex2.calc_median_temperature(input)

    assert (result == test)

def test_calc_median_temperature_even():
    input = [1, 2, 3, 4]
    test = 2.5
    result = ex2.calc_median_temperature(input)

    assert (result == test)



