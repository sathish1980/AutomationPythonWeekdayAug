import pytest

@pytest.mark.usefixtures("beforeeacttestcasefirstclass")
class Testfirstclass:

    @pytest.mark.Sanity
    def test_sanity_firttestcase1(self,loaddata):
        #for eachdata in loaddata:
        print("username is :",loaddata[0])
        print("password is :", loaddata[1])
        print("DOB is :", loaddata[2])

    @pytest.mark.Sanity
    def test_SIT_seondtestcase1(self):
        print("second testcase")

    @pytest.mark.Sanity
    def test_regression_thirdtestcase(self):
        print("third testcase")

    @pytest.mark.Sanity
    def test_sanity_regression_fourthtestcase1(self):
        print("fourth testcase")

