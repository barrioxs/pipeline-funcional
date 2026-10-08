if __name__ == "__main__":
    transacciones = [ 
        {"id": 1, "categoria": "tecnologia", "monto": 1200, "descuento": 0.10},
        {"id": 2, "categoria": "hogar", "monto": 150, "descuento": 0.0}, 
        {"id": 3, "categoria": "tecnologia", "monto": 800, "descuento": 0.15},
        {"id": 4, "categoria": "libros", "monto": 45, "descuento": 0.05}, 
        {"id": 5, "categoria": "tecnologia", "monto": 2300, "descuento": 0.20} ]

    # Funcion para calcular el monto total de cada una de las transacciones
    importe_total_individual = list(map(lambda t : t["monto"] * (1 - t["descuento"]), transacciones))
    print("Importe total de las transacciones:", importe_total_individual)

    # Funcion filter para fuiltrar las transacciones de la categoria tecnologia
    filtrar_tecnologia = list(filter(lambda t: t["categoria"] == "tecnologia" and t["monto"] > 500, transacciones))
    print("Transacciones de la categoria tecnologia mayores a 500$", filtrar_tecnologia)

    # Funciuon que calcula el monto total acumulado de la lista original
    from functools import reduce
    montos = list(map(lambda t: t["monto"], transacciones))
    monto_total = reduce(lambda x, y: x + y, montos)
    print("Monto total de acumulados de la lista original", monto_total)

    #Pipeline funcional para la categoria tecnologia
    filtro = list(filter(lambda t: t["categoria"] == "tecnologia", transacciones))
    mapeo = list(map(lambda m: m["monto"] * (1 - m["descuento"]), filtro))
    total = reduce(lambda x, y: x + y, mapeo)
    print("Monto total de la categoria tecnologia con descuentos aplicados", total)

    #Funcion unica Pipeline

    total_unica = reduce(
        lambda x, y: x + y,
        map(
            lambda m: m["monto"] * (1 - m["descuento"]),
            filter(lambda t: t["categoria"] == "tecnologia", transacciones)
        )
        
    )
    print("Total unico", total_unica)