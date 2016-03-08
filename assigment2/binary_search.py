import random

def binarySearch(liste, aranan):
	baslangic = 0
	bitis = len(liste) - 1
	denemeSayisi = 0
	while (baslangic <= bitis):
		denemeSayisi = denemeSayisi + 1

		orta = (baslangic + bitis) // 2
		bulunan = liste[orta]

		if (bulunan == aranan):
			return denemeSayisi
		elif (bulunan > aranan):
			bitis = orta - 1
		else:
			baslangic = orta + 1
	return -1 # bulunamadi

diziBoyutlari = [1,10,100,1000,10000,100000,1000000,10000000,100000000]

for diziBoyutu in diziBoyutlari:
	kacKereDenenecek = 1000

	dizi = range(diziBoyutu)
	toplamDenemeSayisi = 0

	for i in range(kacKereDenenecek):
		#aranan = random.randint(0, diziBoyutu - 1)
		aranan = -73
		denemeSayisi = binarySearch(dizi, aranan)
		toplamDenemeSayisi = toplamDenemeSayisi + denemeSayisi

	ortalamaDenemeSayisi = toplamDenemeSayisi / (kacKereDenenecek * 1.0)

	print "%12d\t%4.2f" % (diziBoyutu, ortalamaDenemeSayisi)