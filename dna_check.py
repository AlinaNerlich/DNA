hair_colour = {"black": "CCAGCAATCGC", "brown": "GCCAGTGCCG", "blonde": "TTAGCTATCGC"}
facial_shape = {"square": "GCCACGG", "round": "ACCACAA", "oval": "AGGCCTCA"}
eye_color = {"blue": "TTGTGGTGGC", "green": "GGGAGGTGGC", "brown": "AAGTAGTGAC"}
gender = {"female": "TGAAGGACCTTC", "male": "TGCAGGAACTTC"}

suspects = {"Eva": ["blonde", "oval", "blue", "female"],
            "Larisa": ["brown", "oval", "brown", "female"],
            "Matej": ["black", "oval", "blue", "male"],
            "Miha": ["brown", "square", "green", "male"]}

with open("dna.txt", "r") as dna_string:
    dna = dna_string.read()

dna_ice_cream_lover = []

for x in hair_colour:
    if hair_colour[x] in dna:
        dna_ice_cream_lover.append(x)
for x in facial_shape:
    if facial_shape[x] in dna:
        dna_ice_cream_lover.append(x)
for x in eye_color:
    if eye_color[x] in dna:
        dna_ice_cream_lover.append(x)
for x in gender:
    if gender[x] in dna:
        dna_ice_cream_lover.append(x)
print(dna_ice_cream_lover)

for x in suspects:
    if suspects[x] == dna_ice_cream_lover:
        print("The ice cream lover is " + str(suspects[x]))
