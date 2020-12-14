n=int(input())
tot=0
for i in range(n):
    fig = input()
    if fig=='Tetrahedron':
        tot=tot+4
    if fig=='Icosahedron':
        tot=tot+20
    if fig=='Dodecahedron':
        tot=tot+12
    if fig=='Octahedron':
        tot=tot+8
    if fig=='Cube':
        tot=tot+6
print(tot)
