# Tehtävä 3.1

kuha = float(input("Ilmoita kuhan pituus (cm): "))
if kuha<=37:
    print("Laske kuha takaisin järveen")
    print("Kuha on",str(37-kuha), "senttimetriä alimittainen")

if kuha>=37:
    print("Voit nostaa kuhan.")