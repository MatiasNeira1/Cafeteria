import os
import json
import csv

os.system("cls")
URL_EMPLEADOS = "empleados.json"

DIR_PRODUCTOS = "productos.csv"
FIELDNAMES_PRODUCTOS = ["id_producto", "nombre_producto", "precio", "stock"]

# =======================================================================================


def leer_archivo_csv(dir):
    try:
        with open(dir, mode="r", newline="", encoding="utf-8") as archivo:
            data = csv.DictReader(archivo)
            return list(data)
    except:
        return []


def guardar_archivo_csv(dir, data, fieldnames):
    try:
        with open(dir, mode="w", newline="", encoding="utf-8") as archivo:
            data_csv = csv.DictWriter(archivo, fieldnames=fieldnames)
            data_csv.writeheader()
            data_csv.writerows(data)
    except:
        return []


# =======================================================================================


def cargar_json(url_archivo):
    try:
        with open(url_archivo, "r") as archivo:
            return json.load(archivo)
    except:
        return []


def guardar_archivo(url_archivo, data):
    with open(url_archivo, "w") as archivo:
        json.dump(data, archivo, indent=4)


# =======================================================================================
def crear_producto():
    os.system("cls")
    print("=====AGREGAR PRODUCTO=====")
    productos = leer_archivo_csv(DIR_PRODUCTOS)
    id_producto = input("Ingrese ID de producto: ")
    nombre_producto = input("Ingrese nombre de producto: ")

    try:
        precio_producto = int(input("Ingrese el precio del producto: "))
    except:
        sueldo = 0
    try:
        stokc_producto = input("Ingrese stock disponible de producto: ")
    except:
        stokc_producto = 0

    producto_nuevo = {
        "id_producto": id_producto,
        "nombre_producto": nombre_producto,
        "precio": precio_producto,
        "stock": stokc_producto,
    }

    productos.append(producto_nuevo)
    guardar_archivo_csv(DIR_PRODUCTOS, productos, FIELDNAMES_PRODUCTOS)


def actualizar_producto():
    os.system("cls")
    print("=====ACTUALIZAR PRODUCTO=====")
    productos = leer_archivo_csv(DIR_PRODUCTOS)

    id_producto = input("Ingrese ID de producto a actualizar: ")
    nombre_producto = input("Ingrese nombre de producto a actualizar: ")

    try:
        precio_producto = int(input("Ingrese el nuevo precio del producto: "))
    except:
        precio_producto = 0
    try:
        stokc_producto = input("Ingrese nuevo stock disponible de producto: ")
    except:
        stokc_producto = 0

    for producto in productos:
        if producto["id_producto"] == id_producto:
            producto["nombre_producto"] = nombre_producto
            producto["precio"] = precio_producto
            producto["stock"] = stokc_producto
            break

    guardar_archivo_csv(DIR_PRODUCTOS, productos, FIELDNAMES_PRODUCTOS)


# =============================================================================================


def crear_empleado():
    os.system("cls")

    print("=====AGREGAR EMPLEADO=====")
    empleados = cargar_json(URL_EMPLEADOS)

    id_empleado = input("Ingrese ID de empleado: ")
    nombre = input("Ingrese nombre de empleado: ")
    apellido = input("Ingrese apellido de empleado: ")
    try:
        sueldo = int(input("Ingrese sueldo de empleado: "))
    except:
        sueldo = 0

    id_cargo = input("Ingrese Id de cargo del empleado: ")

    empleado_nuevo = {
        "id_empleado": id_empleado,
        "nombre": nombre,
        "apellido": apellido,
        "sueldo": sueldo,
        "id_cargo": id_cargo,
    }
    empleados.append(empleado_nuevo)
    guardar_archivo(URL_EMPLEADOS, empleados)


def actualizar_empleado():
    os.system("cls")
    print("=====ACTUALIZAR INFORMACION=====")
    empleados = cargar_json(URL_EMPLEADOS)

    id_empleado = input("Ingresar ID de empleado que quiera cambiar: ")
    nombre = input("Ingresar nombre de empleado a cambiar: ")
    apellido = input("Ingrese apellido de empleado a cambiar: ")
    try:
        sueldo = int(input("Ingrese sueldo de empleado a cambiar: "))
    except:
        sueldo = 0

    id_cargo = input("Ingrese Id de cargo del empleado a cambiar: ")

    for empleado in empleados:
        if empleado["id_empleado"] == id_empleado:
            empleado["nombre"] = nombre
            empleado["apellido"] = apellido
            empleado["sueldo"] = sueldo
            empleado["id_cargo"] = id_cargo
            break
    guardar_archivo(URL_EMPLEADOS, empleados)


def menu_general():
    os.system("cls")
    print("    =====EMPLEADOS====\t\t      ====PRODUCTOS====")
    print("=" * 60)
    print("1. Crear empleado\t\t| 6. Crear producto")
    print("2. Actualizar empleado\t\t| 7. Actualizar producto")
    print("3. Eliminar empleado\t\t| 8. Listar producto  ")
    print("4. Listar empleado\t\t| 9. Borrar producto")
    print("5. Salir\t\t\t|")


def eliminar_empleado():
    os.system("cls")
    print("=====ELIMINAR EMPLEADO=====")
    empleados = cargar_json(URL_EMPLEADOS)

    empleados_que_quedan = []

    id_empleado = input("Ingresar ID de empleado que desea eliminar: ")

    for empleado in empleados:
        if empleado["id_empleado"] != id_empleado:
            empleados_que_quedan.append(empleado)

        guardar_archivo(URL_EMPLEADOS, empleados_que_quedan)


def listar_empleados():
    empleados = cargar_json(URL_EMPLEADOS)
    headers = ["id_empleado", "nombre", "apellido", "sueldo", "id_cargo"]
    col_widths = [15, 15, 15, 15, 15]
    header_line = " | ".join(
        f"{header.capitalize():^{col_widths[i]}}" for i, header in enumerate(headers)
    )
    print(header_line)
    print("-" * len(header_line))

    for empleado in empleados:
        row = " | ".join(
            f"{str(empleado.get(header, '')):^{col_widths[i]}}"
            for i, header in enumerate(headers)
        )
        print(row)


def seleccionar_opcion(max_opcion):
    opcion = 0
    while True:
        try:
            opcion = int(input("Seleccione una opción >> "))
        except:
            pass
        if opcion < 1 or opcion > max_opcion:
            input("Opción invalida intente nuevamente >> ")
        else:
            return opcion


def iniciar_programa():
    while True:
        menu_general()
        opcion = seleccionar_opcion(9)

        if opcion == 1:
            crear_empleado()
        elif opcion == 2:
            actualizar_empleado()
        elif opcion == 3:
            eliminar_empleado()
        elif opcion == 4:
            listar_empleados()
        elif opcion == 5:
            return
        elif opcion == 6:
            crear_producto()

        elif opcion == 7:
            actualizar_producto()

            # elif opcion == 8:

            # elif opcion == 9:

            input("Presione ENTER para continuar")


iniciar_programa()
