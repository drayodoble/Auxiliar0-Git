class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.tareas = []

    def agregarTarea(self, tarea):
        self.tareas.append(tarea)

    def listarTareas(self):
        for tarea in self.tareas:
            if tarea.estaLista():
<<<<<<< HEAD
                print(f"La tarea {tarea.obtenerNombre()} está lista")
                print(f"La tarea {tarea.obtenerNombre()} no está lista")
=======
                print(f"[X] {tarea.obtenerNombre()}" )
            else:
                print(f"[ ] {tarea.obtenerNombre()}" )
>>>>>>> aba2b3400958584cf56fb723b265ae21e9cfa180
