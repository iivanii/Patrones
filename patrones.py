from typing import NamedTuple, List

Patron = NamedTuple('Patron', [
        ('longitud_secuencia', int),
        ('secuencia', str)
])

#389 111 465 111 342 111 798

def encuentra_patron(secuencia:str)->str:
    patron=""
    primer_iteracion=True
    for inumero in range(len(secuencia)):
        if primer_iteracion:
            patron=patron + secuencia[inumero]
            primer_iteracion=False
            continue
        if patron == secuencia[inumero:len(secuencia)][0:len(patron)]:
            return patron
        else:
            patron=patron + secuencia[inumero]
        
    return patron



def valida_secuencia(secuencia_s:List[Patron]|Patron)->str:
    if type(secuencia_s) == list:
        patrones_a_estudiar=len(secuencia_s)
        print('Patrones a estudiar: ',patrones_a_estudiar)
        for i in secuencia_s:
            print('Secuencia: ', i.longitud_secuencia)
            secuencia=i.secuencia.strip()
            print('El patron es: ', encuentra_patron(secuencia))
    else:
        print('Secuencia: ', secuencia_s.secuencia)
        secuencia=secuencia_s.secuencia.strip()
        print('El patron es: ', encuentra_patron(secuencia))



p1=Patron('12', '123145123145' )

p2= Patron('20','1234567891012345678910')

p3= Patron('283','31415926535897932384626433832793141592653589793238462643383279314159265358979323846264338327931415926535897932384626433832793141592653589793238462643383279314159265358979323846264338327931415926535897932384626433832793141592653589793238462643383279314159265358979323846264338327931415926535897932384626433832793141592653589793238462643383279314159265358979323846264338327931415926535897932384626433832793141592653589793238462643383279314159265358979323846264338327931415926535897932384626433832793141592653589793238462643383279314159265358979323846264338327931415926535897932384626433832793141592653589793238462643383279')
valida_secuencia(p3)



# 1 2 3 1 4 5 | 1 2 3 1 4 5
