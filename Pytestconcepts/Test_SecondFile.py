import pytest


class Test_secondclass:

    @pytest.mark.xfail
    def test_fifthtestcase(self):
        print("Fifth test case")

    @pytest.mark.SIT
    @pytest.mark.Sanity
    @pytest.mark.Regression
    @pytest.mark.run(order=2)
    def test_regression_sixthtestcase(self):
        print("sixth test case")

    @pytest.mark.SIT
    @pytest.mark.run(order=1)
    def test_seventhtestcase(self):
        print("seventh test case")