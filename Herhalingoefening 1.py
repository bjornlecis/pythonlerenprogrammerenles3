gewicht_in_kilo = float(input("geef het gewicht"))
aantal_km = float(input("geef het aantal km in"))
kost = 2+gewicht_in_kilo*0.15+aantal_km*0.08
print("aantal kilo:\t{}\naantal km\t{}\nkost:\t€ {}".
format(gewicht_in_kilo,aantal_km,round(kost,2)))

