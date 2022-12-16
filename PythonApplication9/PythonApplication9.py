ruta = " "*50
print(ruta,"+-----------------+")
print(ruta,"|                 |")
print(ruta,"|    Uppgift 1    |")
print(ruta,"|                 |")
print(ruta,"|   Theodor O.Y   |")
print(ruta,"|                 |")
print(ruta,"|     16/11-22    |")
print(ruta,"|                 |")
print(ruta,"+-----------------+")

p = int(input("Hur mycket pengar vill du ta ut?"))

a = p//500
b = (p%500)
c = b//200
d = (b%200)
e = d//100
f = d%100

print("You get",a, "femhundra sedlar,", c, "tvahundra sedlar,", e, "hundra sedlar", f,"kr resterar")

