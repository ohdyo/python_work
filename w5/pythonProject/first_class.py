from prettytable import PrettyTable

table = PrettyTable()

table.add_column("number",["1","2","3","4","5","6","7","8","9","10"])
table.add_column("Name",["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie"])
table.add_column("Type",["Grass","Grass","Grass","Fire","Fire","Fire","Water","Water","Water","Bug"])

print(table)

