import Lab2.Bmi as BMI

def test_bmi_under_weight():
    expected_result=-1
    result = BMI.calculate_bmi(1.73, 40)
    assert(result==expected_result)

def test_bmi_over_weight():
    expected_result=0
    result = BMI.calculate_bmi(1.73, 90)
    assert(result==expected_result)
    
def test_bmi_normal_weight():
    expected_result=1
    result = BMI.calculate_bmi(1.73, 70)
    assert(result==expected_result)
    