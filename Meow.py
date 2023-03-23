p = int(input())
sf = int(input())
a = int("1" * 185)
ma = [0] * 185
print(ma)
sf -= 1
sf = bin(sf)[2:]
p = int(bin(p)[2:])
sf = int((185 - len(sf)) * "0" + sf)
mask = bin(int(str(a), 2) - int(str(sf), 2))[2:]
print(p)
print(sf)
print(mask)
for i in range(1, 186):
    if ma[185 - i] != mask[185 - i]:
        s += "1"
        ma[-i:(-i + len(mask))] = map(int, list(str(bin(p))))
