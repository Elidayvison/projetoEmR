
print("\n")
atributos = "Nome","Tamanho","Sexo","Idade","Peso","Qtd Filhos","Qtd casa","Profissao","Escolaridade","Est. civil"




Nome = []
Tamanho=[]
Sexo = []
Est_civil = []
Idade =  []
Peso = []
Qtd_Filhos = []
Qtd_casa = []
olho = []
Escolaridade = []

arquivo = open("projetoEmR","a")



i=0
while i<20:
    x1 = input("informe o Nome[%d]:" %i)
    Nome.append(x1)
    arquivo.writelines(Nome[i] + " ")
    i=i+1

arquivo.writelines("\n")
print("\n")


i=0
while i<20:
    x1 = input("informe o tamanho[%d]:" %i)
    Tamanho.append(x1)
    arquivo.writelines(Tamanho[i] + " ")
    i=i+1


arquivo.writelines("\n")


print("\n")
i=0
while i<20:
    x1 = input("informe o Sexo[%d]:" %i)
    Sexo.append(x1)
    arquivo.writelines(Sexo[i] + " ")
    i=i+1

arquivo.writelines("\n")

print("\n")
i=0
while i<20:
    x1 = input("informe o Est_civil[%d]:" %i)
    Est_civil.append(x1)
    arquivo.writelines(Est_civil[i] + " ")
    i=i+1

arquivo.writelines("\n")

i=0
print("\n")

while i<20:
    x1 = input("informe a Idade[%d]:" %i)
    Idade.append(x1)
    arquivo.writelines(Idade[i] + " ")
    i=i+1

arquivo.writelines("\n")

print("\n")
i=0
while i<20:
    x1 = input("informe o Peso[%d]:" %i)
    Peso.append(x1)
    arquivo.writelines(Peso[i] + " ")
    i=i+1

arquivo.writelines("\n")

print("\n")

i=0
while i<20:
    x1 = input("informe a Qtd_Filhos[%d]:" %i)
    Qtd_Filhos.append(x1)
    arquivo.writelines(Qtd_Filhos[i] + " ")
    i=i+1

arquivo.writelines("\n")

print("\n")    
i=0
while i<20:
    x1 = input("informe a Qtd_casa[%d]:" %i)
    Qtd_casa.append(x1)
    arquivo.writelines(Qtd_casa[i] + " ")
    i=i+1

arquivo.writelines("\n")

print("\n")
i=0
while i<20:
    x1 = input("informe a cor do olho[%d]:" %i)
    olho.append(x1)
    arquivo.writelines(olho[i] + " ")
    i=i+1

arquivo.writelines("\n")

print("\n")
i=0
while i<20:
    x1 = input("informe qual Escolaridade[%d]:" %i)
    Escolaridade.append(x1)
    arquivo.writelines(Escolaridade[i] + " ")
    i=i+1

arquivo.close()

print("Nome","Tamanho", "Sexo", "Est_civil","Idade","Peso","Qtd_Filhos","Qtd_casa","olho","Escolaridade")
print(Nome,Tamanho, Sexo, Est_civil,Idade,Peso,Qtd_Filhos,Qtd_casa,olho,Escolaridade)


arquivo.writelines(Nome, Tamanho)
arquivo.close()
