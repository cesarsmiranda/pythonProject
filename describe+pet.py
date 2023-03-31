def describe_pet(animal_type, pet_name):
    """Exibe informações sobre um animal de estimação"""
    print("\nI have a " + animal_type + ".")
    print("n\My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster' , 'harry')
describe_pet('dog' , 'willie')