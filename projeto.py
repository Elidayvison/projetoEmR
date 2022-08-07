
print("\n")
atributos = "Nome","Tamanho","Sexo","Idade","Peso","Qtd Filhos","Qtd casa","Profissao","Escolaridade","Est. civil"

''''print(atributos)'''
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
while i<2:
    x1 = input("informe o Nome[%d]:" %i)
    Nome.append(x1)
    
    i=i+1
arquivo.writelines(Nome)
print("\n")


i=0
while i<2:
    x1 = input("informe o tamanho[%d]:" %i)
    Tamanho.append(x1)
   
    i=i+1
arquivo.writelines(Tamanho)
'''
try:
    nome_arquivo = input('Nome do arquivo a ser editado:')
    arquivo = open(nome_arquivo, 'r+')
except FileNotFoundError:
    arquivo = open(nome_arquivo, 'w+')
    arquivo.writelines(u'Arquivo criado pois nao existia')
arquivo.close()
'''

arquivo.close()

'''
print("\n")
i=0
while i<20:
    x1 = input("informe o Sexo[%d]:" %i)
    Sexo.append(x1)
    
    i=i+1

print("\n")
i=0
while i<20:
    x1 = input("informe o Est_civil[%d]:" %i)
    Est_civil.append(x1)
    
    i=i+1

i=0
print("\n")

while i<20:
    x1 = input("informe a Idade[%d]:" %i)
    Idade.append(x1)
    
    i=i+1

print("\n")
i=0
while i<20:
    x1 = input("informe o Peso[%d]:" %i)
    Peso.append(x1)
    
    i=i+1

print("\n")

i=0
while i<20:
    x1 = input("informe a Qtd_Filhos[%d]:" %i)
    Qtd_Filhos.append(x1)
    
    i=i+1

print("\n")    
i=0
while i<20:
    x1 = input("informe a Qtd_casa[%d]:" %i)
    Qtd_casa.append(x1)
    
    i=i+1

print("\n")
i=0
while i<20:
    x1 = input("informe a cor do olho[%d]:" %i)
    olho.append(x1)
    
    i=i+1

print("\n")
i=0
while i<20:
    x1 = input("informe qual Escolaridade[%d]:" %i)
    Escolaridade.append(x1)
    
    i=i+1

print("Nome","Tamanho", "Sexo", "Est_civil","Idade","Peso","Qtd_Filhos","Qtd_casa","olho","Escolaridade")
print(Nome,Tamanho, Sexo, Est_civil,Idade,Peso,Qtd_Filhos,Qtd_casa,olho,Escolaridade)

for i in Nome, Tamanho:
    print (Nome,Tamanho)

i=0
for i in Tamanho:
    print (i)
print("\n\n")

'''
arquivo.writelines(Nome, Tamanho)
arquivo.close()