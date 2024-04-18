from bandymai import get_joke


x = input("Ar nori isgirsti anekdota?")
if x == "taip":
    get_joke()
else:
    print("Gaila")

print(__name__)
