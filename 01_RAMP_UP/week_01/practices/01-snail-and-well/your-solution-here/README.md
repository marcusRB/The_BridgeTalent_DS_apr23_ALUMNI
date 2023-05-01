# YOUR SOLUTION HERE

Instrucciones para las prácticas

## MAIN TASK
- Actualiza tu repositorio remoto *upstream/master* sincronizado con el *original/master* que hiciste el fork
- Actualiza tu repositorio local o en caso que sea CLONE ya viene actualizado
- crea tu código o ficheros en la misma carpeta <your-code> o <your-solution-here> con Visual Studio Code u otro editor (Jupyter)
- es aconsejable crear una rama DEV, sucesivamente sube el contenido (sin modificar el resto de carpetas)
- realizar un **MERGE** con tu rama *master*
- solicita un **PULL REQUEST** al principal y deja un comentario

## EVALUATION

La práctica será verificada y se dejará un feedback. Finalmente se enviará una notificación de:

- ACEPTADA
- REQUEST CHANGES
- COMMENTS
- APPROVE 0REVIEW

según la situación que sea no se aceptará una **PULL REQUEST** para no alterar la estructura del repositorio original, por lo tanto se procederá con el cierre!
 
pozo = 125  # profundidad del pozo en cm
resbala = 20   # cantidad de cm que resbala cada noche
progreso = 0 # cantidad de cm que ha avanzado el caracol

avance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
dias = 0     # contador de días
while progreso < pozo:
    dias += 1
    progreso += avance_cm[dias-1]
    if progreso >= pozo:
        break
    else:
        progreso -= resbala

print("El caracol tardó", dias, "días en escapar del pozo.")
