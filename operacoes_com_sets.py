#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 03/12/2021
#Término: /12/2021
#Atividade009 - exercicio c

#Limpar o terminal
import os


os.system('cls')

#Título
print('-'*70)
print('Operações matemáticas com SETS')
print('='*70)

#Declaração
set1 = {1, 2, 3, 4, 5, 6}
set2 = {15, 20, 8, 5, 10}
set3 = {'PC', 'Xbox One', 10,}
set4 = {'Xbox One', 'PC', 50}

print('Antes:')
print(f'Set1: {set1}, Set2: {set2}, Set3: {set3}, Set:4 {set4}', end=' | ')
print()
print()

#Pergunta se o usuário deseja adicionar itens nos sets
pergunta = str(input(f'Deseja adicionar algo no 1° SET? (s/n): ')).lower()
if(pergunta == 's'):
    adicione = str(input('Adicione: '))
    set1.add(adicione)
pergunta2 = str(input(f'Deseja adicionar algo no 2° SET? (s/n): ')).lower()
if(pergunta2 == 's'):
    adicione2 = str(input('Adicione: '))
    set2.add(adicione2)
pergunta3 = str(input(f'Deseja adicionar algo no 3° SET? (s/n): ')).lower()
if(pergunta3 == 's'):
    adicione3 = str(input('Adicione: '))
    set3.add(adicione3)
pergunta4 = str(input(f'Deseja adicionar algo no 4° SET? (s/n): ')).lower()
if(pergunta4 == 's'):
    adicione4 = str(input('Adicione: '))
    set4.add(adicione4)

#Sets depois do usuário ter adicionado elementos
print()
print('Depois:')
print(f'Set1: {set1}, Set2: {set2}, Set3: {set3}, Set:4 {set4}', end=' | ')
print()
print()

#O método união juntas os elementos sem repeti-los
print('UNIÃO')
uniao = set1.union(set3)
print(f'União do SET1 com SET3: {uniao}')
print()

#Na Interseção ( & ), apenas os elementos que estiverem nos dois sets restarão.
print('INTERSEÇÃO')
intersecao = set1 & set2
print(f'Interseção do SET1 com SET2: {intersecao}')
print()

#Na diferença ( - ), restarão apenas os elementos que estiverem no primeiro set, mas não no segundo.
print('DIFERENÇA')
diferenca = set2 - set3
print(f'Diferença do SET2 com SET3: {diferenca}')
print()

#O método symmetric_difference() manterá os elementos que não estão presentes em ambos conjuntos:
print('DIFERENÇA SIMÉTRICA')
diferencaSimetrica = set3 ^ set4
print(f'Diferenaça simétrica SET3 com SET4: {diferencaSimetrica}')