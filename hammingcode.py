
##Buscamos las posiciones de los datos de paridad y lo sustitumos por "*"
def buscar_paridad(cadena):
    ##Convertir a lista
    cadena = list(cadena)

    posicion = 0
    x = 0

    while (posicion < len(cadena)):
        posicion = 2 ** x
        if posicion < len(cadena):
            cadena.insert(posicion-1, "*")
        else:
                break
        x = x + 1
        cadena = "".join(cadena)
        return cadena

##Calcular paridades individuales
def calcular_paridad(cadena, salto):
    cadenaTemporal = ""
    cadenaOriginal = cadena
    
    cadena = cadena[salto-1:]

    n = "N"*(salto-1)
    nsalto = salto * 2

    while (len(cadena)>0):
        cadenaTemporal += cadena[:salto]
        cadena = cadena[nsalto:]
        cadenaTemporal += n

    cadenaTemportal = cadenaTemporal[:len(cadenaOriginal)]

    return cadenaTemporal
    

def obtenerFilas(cadena):
    filasParidad = dict()

    totalFilas = cadena.count("*")
    fila = 0

    while totalFilas > fila:
        salto = 2 ** fila
        filasParidad[salto] = calcular_paridad(cadena, salto)
        fila += 1
    return filasParidad


##Busca flas que su suma de bits sea impar
def buscarError(filasParidad):
    erroneas = list()

    for llave, contenido in filasParidad.items():
        sumatoria =0
        for elemento in contenido:
                for caracter in elemento:
                    if caracter != "*" and caracter != "N":
                        sumatoria += int(caracter)
        if (sumatoria %2 != 0):
            error = True
            erroneas.append(llave)
        else:
            error = False
    return erroneas, error

def buscarRelacionErrores(bitsErrores):
    culumnasRelacionadas = list()
    for indice, elementosFilas in enumerate(bitErrores):
        x = False
        for bit in elementosFilas:
            try:
                int(bit)
                x = True
            except:
                x = False
                break
        if x:
            columnasRelacionadas.append(indice)
    return columnasRelacionadas

def buscarColumnasRelacionadas(filasCorrectas, filasErroneas):
    longitud = len(filasCorrectas.values()[0])

    bitsFilasErroneas = list()

    for i in range(longitud):
        bits = ""
        copyFilasErroneas = list(filasErroeas)
        while len(copyFilasErroneas) > 0:
            filaObjetivo = copyFilasErroneas.pop(0)
            for j in filasErroneas:
                if j == filaObjetivo:
                    bits += filasCorrectas[j][i]
        bitsFilasErroneas.append(bits)

    columnasRelacionadas = buscarRelacionErrores(bitsFilasErroneas)
    return columnasRelacionandas

def quitarEspaciosParidad(cadenaAuto):
	return cadenaAuto.replace("*", "")

def hamming():

    cadena = input("Ingrese cadena")
    cadenaAutocompletada = buscar_paridad(cadena)
    cadenaOriginal = cadenaAutocompletada

    
    while(True):
        filas = obtenerFilas(cadenaAutocompletada)
        (filasError, error) = buscarError(filas)
        print("AS")
        if not error:
            break

        print("filas que contienen errores: \n")

        columnasRelacionadas = buscarColumnasRelacionadas(filas, filasError)
        
        

        if i in columnasRelacionadas:
            copyCadenaAuto = cadenaOriginal
            if cadenaAutomatizada[i] == "0":
                cadenaAutomatizada = copyCadenaAuto[:i] + "1" + copyCadenaAuto[i+1:]
                break
            else:
                cadenaAutomatizada = copyCadenaAuto
        for i in columnasRelacionadas:
            copyCadenaAuto = originalCadenaAuto
            if cadenaAutomatizada[i]== "0":
                print("1")
                cadenaAutomatizada = copyCadenaAuto[:i] + "1" + copyCadenaAuto[i+1:]
                break
            else:
                print("2")
                cadenaAuto = copyCadenaAuto[:i] + "0" + copyCadenaAuto[i+1:]
                break

        cadenaSinErrores = quitarEspaciosParidad(cadenaAutomatizada)
        print("Entreada"+cadena)
        print("Salida"+cadenaSinErrores)

hamming()
