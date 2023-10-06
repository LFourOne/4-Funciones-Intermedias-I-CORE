x = [ [5,2,3], [10,8,9] ]
x[1][0] = 15
print(x)

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

estudiantes[0]['last_name'] = 'Bryant'                                      # Actualiza valores en diccionarios y listas
print(estudiantes)


directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}

directorio_deportes['fútbol'][0] = 'Andres'
print(directorio_deportes)


z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)



estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(estudiantes):                                                     # Iterar a través de una lista de diccionarios
    for i in estudiantes:
        print(f"first_name - {i['first_name']}, last_name - {i['last_name']}")

iterateDictionary(estudiantes) 

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(name, estudiantes):
    
    for i in estudiantes:                                                               # Obtener valores de una lista de diccionarios
        print(i[name])
    
iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes)



dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    print(len(dojo['ubicaciones']), "UBICACIONES")
    for i in dojo['ubicaciones']:
        print(i)                                                                       # Iterar a través de un diccionarios con valores de lista
    print("")
    print(len(dojo['instructores']), "INSTRUCTORES")
    for i in dojo['instructores']:
        print(i)
printInfo(dojo)