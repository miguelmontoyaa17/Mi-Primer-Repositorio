# tareas.py · Seguimiento de tareas del equipo
tareas_pendientes = [
# Agregá las tareas reales que tiene el equipo ahora
'Ejemplo: implementar login de usuario',
'Ejemplo: diseñar pantalla de inicio',
]
tareas_completadas = [
# Agregá lo que ya terminaron
'Ejemplo: diseño de base de datos',]
print('=== TAREAS PENDIENTES ===')
for t in tareas_pendientes:
    print(f' {t}') 
print('=== TAREAS COMPLETADAS ===')
for t in tareas_completadas:
    print(f' {t}')