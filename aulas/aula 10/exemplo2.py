#criando lisa simples com 3 pokemons
pokemons  = ["pikachu", "charmander","bulbassaur"]
#exibindo a lista
print ("lista de pokemons", pokemons)

#acessando o primeiro pokemon da lista
print("primeiro pokemon da lista é o", pokemons[0])

#adicionando novo pokemon a lista
pokemons.append ("Squirtle")
print(pokemons) #lista após inlcuir squirtle

#removendo charmander da lista
pokemons.remove("charmander")
print (pokemons)

#exibindo a lista 
print("numero de pokemon na lista", len(pokemons))

