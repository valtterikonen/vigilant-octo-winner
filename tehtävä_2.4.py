# Tehtävä 2.4

x_str = input("Syötä 1. kokonaisluku: ")
y_str = input("Syötä 2. kokonaisluku: ")
z_str = input("Syötä 3. kokonaisluku: ")

x = float(x_str)
y = float(y_str)
z = float(z_str)

sum = (x+y+z)
prc = (x*y*z)
m_value = (x+y+z)/3

print("Lukujen summa: " +str(sum))
print("Lukujen tulo: " +str(prc))
print("Lukujen keskiarvo: " +str(m_value))

