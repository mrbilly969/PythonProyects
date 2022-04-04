EquipoM=["Mauricio","Alejandra", "Dayana", "Quique", "Chavita"]
EquipoD=["Dinora", "Mario", "Evita", "Elizabeth", "Sebastian"]


for a,*b,c in [EquipoM, EquipoD]:
    print("El lider de equipo es:", a)
    print("los integrantes usuales son:",b)
    print("El último en integrarse fue:",c)
    print(len(EquipoM))
