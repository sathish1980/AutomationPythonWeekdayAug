import pytest


class Testfirstclass:

    @pytest.mark.Sanity
    def test_sanity_firttestcase1(self):
        print("first testcase")

    @pytest.mark.Sanity
    def test_SIT_seondtestcase1(self):
        print("second testcase")

    @pytest.mark.Sanity
    def test_regression_thirdtestcase(self):
        print("third testcase")

    @pytest.mark.Sanity
    def test_sanity_regression_fourthtestcase1(self):
        print("fourth testcase")