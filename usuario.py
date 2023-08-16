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
                print(f"[X] {tarea.obtenerNombre()}" )
<<<<<<< HEAD
                print(f"La tarea {tarea.obtenerNombre()} no está lista")
=======
>>>>>>> 8ae9edbcd8cc0f1dfd5350ab9409b68dcb1b4178
