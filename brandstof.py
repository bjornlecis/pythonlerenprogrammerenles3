aantal_litter = float(input("geef aantal litter"))
brandstof = input("B of D")
if brandstof.lower() == "b":
    print(aantal_litter*1.75)
elif brandstof.lower() == "d":
    print(aantal_litter*1.92)
else:
    print("fout ingave")
