#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 03/12/2021
#Término: /12/2021
#Atividade009 - exercicio b

#Limpar o terminal
import os


os.system('cls')

#Título
print('-'*70)
print('Latitude e Longitude')
print('='*70)

while (True):
    #Criando
    coordenadas = ()

    #Entrada de dados
    cidade = str(input('Digite a CIDADE: '))

    latitude = float(input('Digite a LATITUDE: '))
    while (latitude <= -90 or latitude >= 90):
        latitude = float(input('Inválido, digite novamente: '))

    longitude = float(input('Digite a LONGITUDE: '))
    while (longitude <= -180 or longitude >= 180):
        longitude = float(input('Inválido, digite novamente: '))

    #Converter tupla em lista
    listaCoordenadas = list(coordenadas)

    listaCoordenadas.append(latitude)
    listaCoordenadas.append(longitude)

    #Converter lista em tupla
    coordenadas = tuple(listaCoordenadas)

    #Saída
    print()
    print('Coordenadas: ', end=' ')
    for coordenada in coordenadas:
        print(coordenada, end=' ')
    print()
    
    #Condicionais para determinar se a cidade está a norte ou sul e leste ou oste
    if (latitude >=0 ):
        print(f'A cidade {cidade} está a {latitude}° Norte')
    else:
        print(f'A cidade {cidade} está a {latitude}° Sul')

    if (longitude >= 0):
        print(f'A cidade {cidade} está a {longitude}º Leste')
    else:
        print(f'A cidade {cidade} está a {longitude}° Oeste')

    print()

    #Pergunta ao usuário se deseja rodar o programa novamente
    while(True):
        continuar = input('Deseja continuar?: (s/n): ').lower()

        if (continuar != 's') and (continuar != 'n'):
            print('Digite "s" ou "n" ')
        elif (continuar == 's'):
            break
        else:
            print('Fim do programa!')
            exit()