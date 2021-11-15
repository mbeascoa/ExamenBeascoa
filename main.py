from Acciones import Doctor

obj = Doctor()
# ------------------------------MENU PRINCIPAL --------------------------------
quiereIntentarlo=True
letra="S"

while quiereIntentarlo :
    while letra== "S" or letra =="s" :
            print("Gracias por participar : ..... ")
            print( "1.- Alta Doctor ")
            print("2 .- Modificar salario Doctor ")
            print("3 .- Eliminar Doctor")
            print("4.- Mostrar apellido y especialidad de un Doctor ")
            print("5.- Visualizar datos de grupo de un Hospital")
            print("6.- Salir ")
            print(" ---------------------------------- ")
            opcion = input("Introduzca la opción requerida :  \n")
            if opcion=="1":
                obj.altaDoctor()
            if opcion=="2":
                obj.modificarSalarioDoctor()
            if opcion == "3":
                obj.eliminarDoctor()
            if opcion == "4":
                obj.mostrarApellidoEspecialidad()
            if opcion == "5":
                obj.visualizarDatosGrupo()
            if opcion == "6":
                obj.salir()
            print(" ----------------------------------------------")
            intento = input("¿Quiere volver a intentarlo? (S/N)").upper()
            if intento=="S" or intento=="s" :
                quiereIntentarlo=True
                letra="S"
            else:
                quiereIntentarlo=False
                letra="N"