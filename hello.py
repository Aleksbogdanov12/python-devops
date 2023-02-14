from devopslib.randomfruit import fruit
import fire

def meal(beverage):
    my_fruit = fruit()
    print(f"My {my_fruit} and {beverage}")
    if my_fruit == "cherry":
        complete_meal = f"Your meal is my fruit {my_fruit} and {beverage}"
        return complete_meal
    alternate_meal = f"Your meal is a steak and {beverage}"
    return alternate_meal

if __name__ == "__main__":
    fire.Fire(meal)