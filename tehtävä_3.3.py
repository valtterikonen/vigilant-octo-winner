# Tehtävä 3.3

sukup = input("Anna sukupuoli (N/M): ")
hemoglob = int(input("Anna hemoblobiiniarvo:" ))

if sukup == "N":
    if hemoglob>117>175:
        print("Hemoglobiiniarvo normaali")

if sukup == "N":
    if hemoglob>175:
        print("Hemoglobiiniarvo suuri")

if sukup == "N":
    if hemoglob<117:
        print("Hemoglobiiniarvo pieni")

if sukup == "M":
    if hemoglob>134>195:
        print("Hemoglobiini on normaali")

if sukup == "M":
    if hemoglob>195:
        print("Hemoglobiiniarvo suuri")

if sukup == "M":
    if hemoglob<134:
        print("Hemoglobiiniarvo pieni")