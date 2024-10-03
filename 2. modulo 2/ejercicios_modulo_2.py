## 1
################################
print("Mi\nnombre\nes\nBond.", end=" ")
print("James Bond.")

# e python 1/Fundamentos-de-python-1/2. modulo 2/ejercicios_modulo_2.py"
#Mi    
#nombre
#es    
#Bond. James Bond.

## 2
################################
##  print(sep="&", "fish", "chips")

# da error, SyntaxError: positional argument follows keyword argument
# Los argumentos de palabras clave deben pasarse después de cualquier argumento posicional requerido.
# corregida

print("fish", "chips", sep="&")  # fish&chips

## 3
################################
# ¿Cuál de las siguientes print() invocaciones de función generarán un SyntaxError?
print('Greg\'s book.')
print("'Greg's book.'")
print('"Greg\'s book."')
print("Greg\'s book.")
## print('"Greg's book."')  # esta genera error sintaxys SyntaxError: unterminated string literal (detected at line 29)