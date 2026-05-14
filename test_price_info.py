import price_info as PRICE

def test_total_cost_shopping():
    expected_result= 46.75
    result= PRICE.total_cost_shopping()
    assert(result == expected_result)

def test_cost_of_fruit():
    expected_result= 32.50
    result=PRICE.cost_of_fruits('watermelon', 5)
    assert(result == expected_result)