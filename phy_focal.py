l = []
s = 0

n = int(input("Enter number of values: "))
for i in range(n):
    u = float(input('Enter u: '))
    v = float(input('Enter v: '))
    f = round(u*v/(u+v),2)
    l.append((u, v, f))
    s += f

print("Object distance\tImage distance\tFocal length")
for u, v, f in l:
    print(f"{u}\t\t{v}\t\t{f}")
print("Mean focal length:", round(f/n,2))