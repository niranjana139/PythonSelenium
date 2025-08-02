import pytest
@pytest.mark.usefixtures("setup")
class Test_fixtureDemo:

    def __init__(self):
        print("Initializing Test_fixtureDemo")

    def test_fixtureDemo(self):
        print("I'll perform Fixture Demo  statements")

    def test_fixtureDemo1(self):
        print("I'll perform Fixture Demo 1 statements")

    def test_fixtureDemo2(self):
        print("I'll perform Fixture Demo 2 statements")

    def test_fixtureDemo3(self):
        print("I'll perform Fixture Demo 3 statements")
