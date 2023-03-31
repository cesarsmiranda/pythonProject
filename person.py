def build_person(first_name, last_name, age=''):
    """Devolve um dicionário com informações sobre uma pessoa"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('cesar', 'miranda', '44')
print(musician)