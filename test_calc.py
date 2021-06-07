import calculator


class TestCase:
    def test_add_l(self):
        assert 5 == calculator.add(1, 4)

    def test_sub_l(self):
        assert 5 == calculator.sub(6, 1)

    def test_mul_l(self):
        assert 5 == calculator.mul(1, 5)

    def test_div_l(self):
        assert 5 == calculator.div(25, 5)
