
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from TestData import FBLoginData
from TestData.FBLoginData import FBLogindata


@pytest.fixture()
def beforeeacttestcase():
    print("beforeeach test case")

@pytest.fixture(scope="class")
def beforeeacttestcasefirstclass():
    print("open the browser")
    yield
    print("close the browser")

@pytest.fixture()
def loaddata():
    return["sathish","password","110590"]

@pytest.fixture()
def baseUrl():
    return "https://www.facebook.com"

@pytest.fixture(scope="class")
def browserlaunch(request):
    web = webdriver.ChromeOptions()
    web.add_argument("--start-maximized")
    web.add_argument("--incognito")
    web.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(params=FBLogindata.credentials)
def FbTestData(request):
    return request.param

@pytest.fixture(params=FBLogindata.credentialsMultipleValue)
def FbTestData(request):
    return request.param

@pytest.fixture(params=FBLogindata.CredentialwithExcelData)
def FbTestDatawithExcel(request):
    return request.param
