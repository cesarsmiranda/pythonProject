users = {
    'aeinstein': {
        'first': 'albert',
        'lastname': 'silva',
        'location': 'brazil',
        },
    'mcurie': {
        'first': 'marie',
        'lastname': 'curie',
        'location': 'paris',
        },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    fullname = user_info['first'] + " " + user_info['lastname']
    location = user_info['location']

    print("\tFull name: " + fullname.title())
    print("\tLocation: " + location.title())

