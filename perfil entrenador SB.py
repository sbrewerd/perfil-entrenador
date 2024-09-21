
sexo = input("ingresa tu sexo (mujer/hombre): ").lower()
    
region = input("cual es tu region?: ")
    
print("elige tu Pokemon preferido:")
print("1. Pikachu")
print("2. Charmander")
print("3. Bulbasaur")
    
while True:
    opcion = str(input("ingresa el numero de tu opcion: "))
        
    if opcion == '1':
            pokemon_preferido = "Pikachu"
            break
    elif opcion == '2':
            pokemon_preferido = "Charmander"
            break
    elif opcion == '3':
            pokemon_preferido = "Bulbasaur"
            break
    else:
            print("no entiendo, por favor, elige 1, 2 o 3.")
    
if sexo == "mujer":
        mensaje = f"hola entrenadora, eres de la región {region} y tu Pokémon preferido es {pokemon_preferido}."
else:
        mensaje = f"hola entrenador, eres de la región {region} y tu Pokémon preferido es {pokemon_preferido}."
print(mensaje)