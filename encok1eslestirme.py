import random
N = 100
kac_dizi = 100

dizi = []
for i in range(N):
	dizi.append([])
	for j in range(100):
		dizi[i].append(random.choice([0, 1]))

eslesmeler = []

for x1 in range(100):
	for x2 in range(100):
		if (x1 == x2):
			continue # kendisiyle karsilastirma

		sayac = 0
		for y in range(N):
			if (dizi[x1][y] == 1 and dizi[x2][y] == 1):
				sayac = sayac + 1

		pos = 0
		while pos < len(eslesmeler) and eslesmeler[pos][0] > sayac:
			pos = pos + 1

		eslesmeler.insert(pos, [sayac, x1, x2])

print("En cok eslesen ilk 10 kolon: ")
for i in range(N):
	print(str(i+1) + ") " + str(eslesmeler[i][1]) + " ve " + str(eslesmeler[i][2]) + " Eslesme sayisi: " + str(eslesmeler[i][0]))