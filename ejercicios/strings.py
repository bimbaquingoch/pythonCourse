# strngs
course = """
HOLA MUNDO
ESTO ES UN STRING LARGO
DE MULTIPLES LINEAS
"""
otrostring = 'el muy "ingeniero"'
print(course)
print(otrostring)

print(course[6])
# desde 0 hasta la posicion 5
# desde el inicio hasta la posicion 5
print(course[:5])
# copia del string
another = course[:]
print(another)

name = "jedi"
print(name[1:-1])

# format strings

firts = "yon"
last = "adrian"
message = firts + " [" + last + "] is a coder"
msg = f"{firts} [{last}] is a coder"
print(message)
print(msg)

# string methods

course = "Python for begginers"
print(len(course))
print(course.upper())
print(course.lower())
print(course)
print(course.find("g"))
print(course.replace("g", "t"))
print(course.title() + "   jjj")
print(course.capitalize())
print("g" in course)
