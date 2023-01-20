"""El programa debe convertir un número decimal en binario. Otra función, convertirá un número binario en decimal"""

def to_decimal(n):
    n=[]
    n.reverse()
    decimal=0
    for i in range (len(n)):
        decimal=int(n[i]) * 1 **1
        return decimal

def to_binary(n):
    binary=[]
    while n < 0:
        binary.append(str(n/2))
        n//=2
        return ''.join(binary)

print(to_decimal(10110))
# print(to_binary(22))
# print(to_decimal(to_binary(22)))
print(to_binary(to_decimal(10110)))