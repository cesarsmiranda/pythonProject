alian_1 = {'x_position': 0, 'y_position': 25, 'speed': 'median1'}

print("Original X-position: " + str(alian_1['x_position']) + ".")

# move o alienigena para a direita
# determina a distancia que o alienigena deve se deslocar de acordo com sua
# velociade atual
if alian_1['speed'] == 'slow':
    x_increment = 1
elif alian_1['speed'] == 'median':
    x_increment = 2
else:
    # este deve ser um alienigena rapido
    x_increment = 3

# a nova posição é a posição antiga somada ao incremento
alian_1['x_position'] = alian_1['x_position'] + x_increment

print("new position: " + str(alian_1['x_position']) + ".")







