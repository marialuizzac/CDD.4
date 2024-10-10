notas =["","","","",""]
tam=len (notas)
soma=0
cont=0
for x in range(tam):
    notas[x]=float(input("Digite a nota: "))
for y in range(tam):

for i in range(tam):
   if notas [i]>=media:
       cont+=1


print (f"Temos {cont} alunos com nota maior que a media {media}")