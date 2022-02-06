print("LOTTONUMEROGENERAATTORI")
rawnro = input("Montako numeroa haluat? \n")
nroVastaus = int(rawnro)
as_string = str(rawnro)


import random
lottonumerot = random.sample(range(1, 41), nroVastaus)
print("Valitsit " + as_string + " numeroa")
print("Tässä ovat onnennumerosi: \n")

random.shuffle(lottonumerot)
lottonumerot.sort()

print(lottonumerot)