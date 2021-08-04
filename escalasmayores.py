#Esteban Cabrera 17781

notas = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

while True:
    notaUsuario = input("Ingrese la nota para sacar su escala mayor:").upper()

    index = 0
    index2 = 0
    for nota in notas:
        if (nota == notaUsuario):
            break
        index = index + 1
    
    index2 = index

    escala = []

    escala.append(notas[index%12])
    for i in range(0, 6):
        if (i == 2):
            index = index + 1
        elif (i == 6):
            index = index + 1
        else:
            index = index + 2
        escala.append(notas[index%12])

    print("Escala: ", escala)

    acordes = []
    for i in range(0, 7):
        index = notas.index(escala[i])
        acorde = notas[index%12] + ": " + notas[index%12] + " - " + notas[(index + 4)%12] + " - " + notas[(index + 7)%12] 
        acordes.append(acorde)
    
    for acorde in acordes:
        print(acorde)






    


    
    
              
    
        
        
        
