# começa com os usuários que precisam ser verificados,
# e com uma lista vazia para armazenar os usuários confirmados

unconfirmed_users = ['aline','brian','candace']
confirmed_users = []

# verifica cada usuário até que não haja mais usuários não confirmados
# transfere cada usuário verificado para a lista de usuários confirmados

while unconfirmed_users:
    currente_user = unconfirmed_users.pop()

    print("Verifying user: " + currente_user.title())
    confirmed_users.append(currente_user)

# exibe todos os usuários confirmados
print("\nThe following users have been confirmed:")
for confirmed_users in confirmed_users:
    print(confirmed_users.title())