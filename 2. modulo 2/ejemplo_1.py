print("hola mundo")

# argumentos de palabras clave

print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")

# pto 2.1.13 laboratorio

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

# minimizar el número de invocaciones de la función print() insertando \n en las cadenas;

print("     *\n","   * *\n","  *   *\n"," *     *\n","***   ***\n","  *   *\n","  *   *\n","  *****")


# crear una flecha el doble de grande manteniendo las proporciones

print("          *")
print("        *   *")
print("       *     *")
print("      *       *")
print("     *         *")
print("    *           *")
print("   *             *")
print("  *               *")
print(" *                 *")
print("******        ******")
print("     *        *")
print("     *        *")
print("     *        *")
print("     **********")

# duplica la flecha, colocando ambas flechas una al lado de la otra; 
# nota: una cadena se puede multiplicar usando el siguiente truco: "string" * 2 producirá "stringstring" (pronto contaremos más al respecto)


print("    *      "*2)
print("   * *     "*2)
print("  *   *    "*2)
print(" *     *   "*2)
print("***   ***  "*2)
print("  *   *    "*2)
print("  *   *    "*2)
print("  *****    "*2)

# elimina cualquiera de las comillas y observe detenidamente la respuesta de Python; 
# presta atención a dónde Python ve un error - ¿es este el lugar donde realmente existe el error?

print("    *      "*2) # por  print(*) da error en la linea 57 SyntaxError: Invalid star expression
print("   * *     "*2)
print("  *   *    "*2)
print(" *     *   "*2)
print("***   ***  "*2)
print("  *   *    "*2)
print("  *   *    "*2)
print("  *****    "*2)

# haz lo mismo con algunos de los paréntesis

print("    *      "*2)
print("   * *     "*2)
print("  *   *    "*2)
print(" *     *   "*2)
print("***   ***  "*2)   # print"***   ***  "*2  SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print("  *   *    "*2)
print("  *   *    "*2)
print("  *****    "*2)


# cambia cualquiera de las palabras print por otra cosa, 
# que difiera solo en mayúsculas y minúsculas (por ejemplo, Print) - qué sucede ahora?

print("    *      "*2)
print("   * *     "*2)
print("  *   *    "*2)
print(" *     *   "*2)
print("***   ***  "*2)   #
print("  *   *    "*2)
print("  *   *    "*2)
print("  *****    "*2)  # Print("  *****    "*2)
                        # Traceback (most recent call last):
                        # File "D:\Documents\2. cisco academy\1. fundamentos de python 1\Fundamentos-de-python-1\2. modulo 2\ejemplo_1.py", line 88, in <module>
                        # Print("  *****    "*2)
                        # ^^^^^
                        # NameError: name 'Print' is not defined. Did you mean: 'print'?

# reemplaza algunas de las comillas con apóstrofes; observa lo que sucede con cuidado

print("    *")
print("   * *")
print('  *   *')
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

