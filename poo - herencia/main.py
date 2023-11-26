import clases

programador = clases.Informatico()
programador.setNombre("Ion")
programador.setApellidos("Rock")
programador.experiencia = 5
programador.setLenguajes(["Python", "Java"])
lenguajes = programador.getLenguajes()
print("---"*20)
print(f"{programador.getNombre()} {programador.programar()} en {', '.join(programador.getLenguajes())}")
print("---"*20)
tecnico = clases.Tecnico_Redes()
tecnico.setNombre("Carlos")
print(f"el tecnico {tecnico.getNombre()} {tecnico.auditar()} ahora")
print(tecnico.auditar())
print(tecnico.getLenguajes())