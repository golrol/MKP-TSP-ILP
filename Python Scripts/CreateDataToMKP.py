import json
from os import sep

f = open("Catalog.json")

cat = json.load(f)

numOfItems = 0
Capacity = [20, 20, 20, 300]
NumOfVehicles = 4
weightArray = []
valueArray = []

for pac in cat:
    weightArray.append(pac["weight"])
    valueArray.append(pac["value"])
    numOfItems += 1

with open("myKnapsack\myKnapsack.dat", "w") as outf:
   outf.write(f'NumOfVehicles = {NumOfVehicles};\n\n')
   outf.write(f'Capacity = {Capacity};\n\n')
   outf.write(f'NumOfItems = {numOfItems};\n\n')
   outf.write(f'Value = {valueArray};\n\n')
   outf.write(f'Weight = {weightArray};')
