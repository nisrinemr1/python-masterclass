import csv


with open("sf.csv") as data_file:
    data_file.readline()## NOTE  pour ne pas lire la première ligne
    data_csv = csv.reader(data_file,delimiter=";") 
    
    data_height = []
    height_avg = 0

    for line in data_csv:
        name = line[0]
        height = float(line[2])
        height_avg += height
        data_height.append([height, name])

height_avg /= len(data_height)

for data in data_height:
    data.append(data[0])
    data[0] = abs(data[0] - height_avg)

closer_to_avg = min(data_height)

message = f"la taille moyenne est de {height_avg: .2f} cm"  #.2f format moi ce float a 2 point après la ,
message += f"et ma persone s'en rapprochant le plus est {closer_to_avg[1]}"
message += f"avec {closer_to_avg[2]} cm"

print(message)
      

#print(taller)
#print(lighter)

print("-------")



