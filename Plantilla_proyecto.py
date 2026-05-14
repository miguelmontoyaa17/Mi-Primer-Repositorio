nombre_proyecto = 'LocalUp' # nombre de tu proyecto
descripcion = 'es una plataforma web diseñada para conectar usuarios con eventos restaurantes y actividades en su ciudad mediante reseñas y recomendaciones presonalizadas.' # qué problema resuelve
tecnologias = ["JavaScript", "Node.js", "MongoDB"] # ['HTML', 'Python', 'MySQL']
integrantes = ["Sofia", "Estefania", "Miguel"] # ['Nombre 1', 'Nombre 2']
funcionalidades = [] # ['Login', 'Registro', 'Reportes']
def mostrar_info():
    print(f'Proyecto: {nombre_proyecto}')
    print(f'Descripción: {descripcion}')

    print(f'Equipo: {", ".join(integrantes)}')
    print(f'Tecnologías: {", ".join(tecnologias)}')
    print('Funcionalidades:')
for f in funcionalidades:
    print(f' - {f}')
mostrar_info()