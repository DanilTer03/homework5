name = 'Danil'
age = 29
ver = True
num = 55

immutable_var = tuple([name, age, ver, num])
print(immutable_var)

# immutable_var[0] = 12
# (immutable_var) #Кортеж является неизменяемым объектом, поэтому не поддерживает назначение элемента

mutable_list = [name,age, ver, num]
print(mutable_list)
mutable_list[2] = False
print(mutable_list)
