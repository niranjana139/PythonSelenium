import pytest


#@pytest.mark.smoke
#@pytest.mark.skip(reason="skip seleniumBasics as it is for demonstration")->Skip the seleniumBasics
#@pytest.mark.timeout(3) ->Add on plugin that can be used to set timeout for each testcase
def test_login(browserinstance):
    driver = browserinstance


#@pytest.mark.xfail => Used to ignore it while adding to reports
#@pytest.mark.skipif(sys.platform == "win32", reason="Doesn't work on Windows") ->
# skipif skips seleniumBasics cases for given conditions.

def test_firstprogram():
    msg="Hello World"
    assert msg=="Hi","Test Failed. Expected and actual output not matching"
#mark as smoke so that it can be run with other smoke seleniumBasics cases
@pytest.mark.smoke
def test_secondprogramCreditCard():
    a=4
    b=6
    assert a+2==b,"Test success. Expected and actual output  matching"