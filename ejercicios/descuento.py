precioinicial= float(input("Digite el valor de su compra: "))
descuento = precioinicial * (36 / 100)
preciofinal = precioinicial - descuento

print(f"El precio total con descuento es de: {preciofinal:.2f}")