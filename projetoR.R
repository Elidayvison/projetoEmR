install.packages('tidyverse')

atributos = data.frame(Nome = c('José','Eli','Maria','Carlos',"Eliene","May","Nay","Lucas","Henrique","Joab","Alan","Antonio","Fabi",'Duda','Marcedo','Ana','Antonio','Juliana','jhonata','Elisa'),
                       Tamanho = c(1.58,1.70,1.55,1.68,1.69,1.71,1.70,1.62,1.68,1.70,1.60,1.50,1.74,1.62,1.80,1.90,1.98,1.77,1.55,1.58),
                       Sexo = c('M','M','F','M','F','F','F','M','M','M','M','M','F','F','M','F','M','F','M','F'),
                       Est_civil = c('S','S','S','S','C','S','C','S','S','S','C','S','S','S','C','S','C','C','C','S'),
                       Idade = c(28,21,22,24,29,33,30,45,23,22,50,43,42,43,33,30,24,33,33,29),
                       Peso = c(56,72,100,73,84,85,85,75,74,75,77,59,89,74,80,80,74,80,74,84),
                       Qtd_Filhos = c(0,2,0,0,0,0,2,1,1,4,1,1,1,3,1,0,3,4,2,0),
                       Qtd_casa = c(1,1,1,1,1,1,1,2,3,0,0,0,0,3,3,2,2,1,1,0),
                       Olho = c('V','V','V','V','C','C','C','A','P','A','P','P','A','P','P','A','P','A','P','P'),
                       Escolaridade = c('M','M','M','S','M','S','M','S','S','M','S','S','M','M','S','M','M','S','S','S'))

#PORCETAGEM DO DADOS QUALITATIVOS

sexoF=sum(lengths(regmatches(atributos$Sexo, gregexpr('F', atributos$Sexo))))
sexoM=sum(lengths(regmatches(atributos$Sexo, gregexpr('M', atributos$Sexo))))
FreqM= sexoM/20
FreqF= sexoF/20

civilC = sum(lengths(regmatches(atributos$Est_civil, gregexpr('C', atributos$Est_civil))))/20
civilS= sum(lengths(regmatches(atributos$Est_civil, gregexpr('S', atributos$Est_civil))))/20

cor_olhoV= sum(lengths(regmatches(atributos$Olho, gregexpr('V', atributos$Olho))))/20
cor_olhoC= sum(lengths(regmatches(atributos$Olho, gregexpr('C', atributos$Olho))))/20
cor_olhoA= sum(lengths(regmatches(atributos$Olho, gregexpr('A', atributos$Olho))))/20
cor_olhoP= sum(lengths(regmatches(atributos$Olho, gregexpr('P', atributos$Olho))))/20

#Calculo de Media

media = data.frame(mediaTam = mean(atributos$Tamanho),
                    mediaIda = mean(atributos$Idade),
                    mediaPeso = mean(atributos$Peso),
                    mediaFilho = mean(atributos$Qtd_Filhos),
                    mediaCasa = mean(atributos$Qtd_casa))

#Calculo de Mediana

mediana = data.frame(medianaTam = median(atributos$Tamanho),
                      medianaIda = median(atributos$Idade),
                      medianaPeso = median(atributos$Peso),
                      medianaFilho = median(atributos$Qtd_Filhos),
                      medianaCasa = median(atributos$Qtd_casa))

#Calculo de Q1

q1 = data.frame(q1Tam = quantile(atributos$Tamanho,0.25),
                q1Ida = quantile(atributos$Idade,0.25),
                q1Peso = quantile(atributos$Peso,0.25),
                q1Filho = quantile(atributos$Qtd_Filhos,0.25),
                q1Casa = quantile(atributos$Qtd_casa,0.25))

#Calculo de Q3

q3 = data.frame(q3Tam = quantile(atributos$Tamanho,0.75),
                q3Ida = quantile(atributos$Idade,0.75),
                q3Peso = quantile(atributos$Peso,0.75),
                q3Filho = quantile(atributos$Qtd_Filhos,0.75),
                q3Casa = quantile(atributos$Qtd_casa,0.75))

#Calculo de variancia

variancia = data.frame(varTam = var(atributos$Tamanho),
                        varIda = var(atributos$Idade),
                        varPeso = var(atributos$Peso),
                        varFilho = var(atributos$Qtd_Filhos),
                        varCasa = var(atributos$Qtd_casa))

#Calculo do desvio padrao

desvio = data.frame(desvioTam = sqrt(varTam),
                    desvioIda = sqrt(varIda),
                    desvioPeso = sqrt(varPeso),
                    desvioFilho = sqrt(varFilho),
                    desviocasa = sqrt(varCasa))

#graficos

hist(atributos$Idade)

qqnorm(atributos$Peso)
qqline(atributos$Peso)

barplot(table(atributos$Qtd_Filhos))

qtd =c(sexoF, sexoM)
pie(atributos$Idade,atributos$Sexo,main="Cor dos olhos",col=rainbow(length(atributos$Idade)))

boxplot(atributos$Tamanho,atributos$Idade,atributos$Peso,atributos$Qtd_Filhos,atributos$Qtd_casa)


#gráfico de barras, pizza, histograma, box-plot e gráfico de dispersão




