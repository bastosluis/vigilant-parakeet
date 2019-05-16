

n = int(input())
v = input().split()

for i in range(0, len(v)):
  v[i] = int(v[i])

menor = v[0]
pos = 0
for i in range(1, len(v)):
  if v[i] < menor:
    menor = v[i]
    pos = i

print('Menor valor: '+ str(menor))
print('Posicao: '+ str(pos))
