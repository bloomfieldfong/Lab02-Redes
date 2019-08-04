##Buscamos paridad y cambiamos por *
def buscar_paridad(codigo):
    cadena = list(codigo)
    posicion = 0
    x = 0
    while (posicion < len(cadena)):

        posicion = 2 ** x
        if(posicion> len(cadena)):
                return(cadena)		
        cadena.insert(posicion-1, "*")
        x = x + 1
        

def identificar(codigo, secuencia):
    codigo = buscar_paridad(codigo)
    codigo_temportal = ''
    
    while(len(codigo) < vueltas):
        
        