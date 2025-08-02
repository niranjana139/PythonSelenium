import pytest

from pythonSeleniumBasics.conftest import dataLoad


@pytest.mark.usefixtures("dataLoad")
class Test_fixtureData:

    #Return the data of fixture
    def test_editProfile(self,dataLoad):
        print("User profile data is edited")
        print(dataLoad)

        '''print(dataLoad[0])
        print(dataLoad[1])
        print(dataLoad[2])'''