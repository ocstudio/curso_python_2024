'''Entender cómo trabajar con las cadenas en Python es fundamental para la manipulación de textos y
datos en muchos proyectos. Desde definir variables hasta aplicar métodos específicos, el uso de 
strings es una habilidad básica pero poderosa que se utiliza en áreas avanzadas como el 
procesamiento del lenguaje natural (NLP).
'''
# ¿Cómo se definen las cadenas en Python?

name = 'Orlando Mario'
last_name = 'Cienfuegos Maldonado'
caracter = "c"
texto = ''' Las comillas triples permiten 

incluir saltos de línea y espacios 

en blanco. '''
print(type(texto))
print(texto)

#longitud de caracteres
print(len(name))
print(len(last_name))
print (len(name + ' '+ last_name))
