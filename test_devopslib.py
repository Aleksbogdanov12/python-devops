from devopslib.randomfruit import fruit
from hello import meal


def test_fruit():
    fruit_choice = fruit()
    assert fruit_choice in ["apple", "cherry", "strawberry"]


def test_meal():
    result = meal("milk")
    assert "milk" in result
