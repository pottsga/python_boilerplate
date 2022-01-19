from python_boilerplate.src import calculator

class TestCalculatorAdd:
    def test_basic_add(self):
        result = calculator.add([1, 2])
        assert result == 3

    def test_add_with_more_numbers(self):
        result = calculator.add([1, 2, 3, 4, 5, 6])
        assert result == 21
    
    def test_add_with_negative_number(self):
        result1 = calculator.add([1, -1])
        assert result1 == 0

        result2 = calculator.add([1, 2, 3, -4])
        assert result2 == 2

    def test_add_with_float(self):
        result = calculator.add([1.0, 2.3])
        assert result == 3.3
