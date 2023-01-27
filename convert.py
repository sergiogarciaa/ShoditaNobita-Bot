# PASAR ARRAY STRING A NUEVO ARRAY TIPO INT CON Bucle For
abrirArchivo = open('./asd.txt')

cargaArchivo = abrirArchivo.readlines()
archivoInt = [eval(i) for i in cargaArchivo]
print("Modified list is: ", archivoInt)