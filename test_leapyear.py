import pytest
import leapyear


class TestSeeIf4RuleIsWorkingCorrectly:
    def test_0isaleapyear(self):
        assert leapyear.isleapyear(0) == True

    def test_1isnotaleapyear(self):
        assert leapyear.isleapyear(1) == False

    def test_2isnotaleapyear(self):
        assert leapyear.isleapyear(2) == False

    def test_3isnotaleapyear(self):
        assert leapyear.isleapyear(3) == False

    def test_4isnotaleapyear(self):
        assert leapyear.isleapyear(4) == True

    def test_5isnotaleapyear(self):
        assert leapyear.isleapyear(5) == False

    def test_6isnotaleapyear(self):
        assert leapyear.isleapyear(6) == False

    def test_7isnotaleapyear(self):
        assert leapyear.isleapyear(7) == False

    def test_8isnotaleapyear(self):
        assert leapyear.isleapyear(8) == True


class TestSeeIf100RuleIsWorkingCorrectly:
    # this class is to test if the 100 rule is working
    # correctly, this test includes all 100's from
    # 100-2300, except those that are divisible by 400
    # and asserts if they are False
    def test_100isnotaleapyear(self):
        assert leapyear.isleapyear(100) == False

    def test_200isnotaleapyear(self):
        assert leapyear.isleapyear(200) == False

    def test_300isnotaleapyear(self):
        assert leapyear.isleapyear(300) == False

    def test_500isnotaleapyear(self):
        assert leapyear.isleapyear(500) == False

    def test_600isnotaleapyear(self):
        assert leapyear.isleapyear(600) == False

    def test_700isnotaleapyear(self):
        assert leapyear.isleapyear(700) == False

    def test_900isnotaleapyear(self):
        assert leapyear.isleapyear(900) == False

    def test_1000isnotaleapyear(self):
        assert leapyear.isleapyear(1000) == False

    def test_1100isnotaleapyear(self):
        assert leapyear.isleapyear(1100) == False

    def test_1300isnotaleapyear(self):
        assert leapyear.isleapyear(1300) == False

    def test_1400isnotaleapyear(self):
        assert leapyear.isleapyear(1400) == False

    def test_1500isnotaleapyear(self):
        assert leapyear.isleapyear(1500) == False

    def test_1700isnotaleapyear(self):
        assert leapyear.isleapyear(1700) == False

    def test_1800isnotaleapyear(self):
        assert leapyear.isleapyear(1800) == False

    def test_1900isnotaleapyear(self):
        assert leapyear.isleapyear(1900) == False

    def test_2100isnotaleapyear(self):
        assert leapyear.isleapyear(2100) == False

    def test_2200isnotaleapyear(self):
        assert leapyear.isleapyear(2200) == False

    def test_2300isnotaleapyear(self):
        assert leapyear.isleapyear(2300) == False


class TestSeeIf400RuleIsWorkingCorrectly:
    # This test is to assert if the numbers 400, 800
    # 1200, 1600, 2000 is True, as according to the 400 rule.
    def test_400isaleapyear(self):
        assert leapyear.isleapyear(400) == True

    def test_800isaleapyear(self):
        assert leapyear.isleapyear(800) == True

    def test_1200isaleapyear(self):
        assert leapyear.isleapyear(1200) == True

    def test_1600isaleapyear(self):
        assert leapyear.isleapyear(1600) == True

    def test_2000isaleapyear(self):
        assert leapyear.isleapyear(2000) == True