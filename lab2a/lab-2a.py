#1
print("Перша константа 'false'-", False)
print("Друга константа 'true'-", True)
print("None константа -", None)
#2
print(abs(-4.8), f"дорівнює {abs(4.8)}")
print(chr(7894))
print(oct(18))
#3
a = 20
if a >= 20:
    print("A >= 20")
else:
    print("A < 19 ")
for d in 'Denys':
    print(d*3)
b = 5
while b <= 40:
    print(b, '')
    b += 5
#4
try:
    c = int ("hello")
except ValueError:
    print ("Це не число")
finally:
    print("Це всеодно працює")
#5
with open("README.md", "w") as f:
   f.write("test text")
#6
add = lambda x, y: x + y
print (add ('Denys', ' Balazh'))
