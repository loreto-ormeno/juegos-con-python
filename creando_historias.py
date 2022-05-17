#vamos a crear una historia, concatenado cadenas de caracteres.
fstring= "alegria"
print(f"Aprende a programar con {fstring}") #metodo de concatenar con f_String.

print(f"******************************")
print (f"JUGUEMOS A CREAR UNA HISTORIA")
print(f"******************************")

sustantivo = input("Ingrese un sustantivo que indique un lugar: ")
sustantivo2 = input("Ingrese otro sustantivo que indique una cosa o animal: ")
adjetivo = input("Ingrese un adjetivo: ")
emocion = input("Ingrese un verbo que demuestre una emocion: ")
verbo = input("Ingrese un verbo: ")

historia = f"Iba caminado por {sustantivo} y me encontre un {sustantivo2} muy {adjetivo}, por lo mismo senti {emocion} y me dieron ganar de {verbo}"

print(historia)