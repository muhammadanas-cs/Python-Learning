temp = [22.5, 23.1,24.8,27.2,30.5,32.1,31.4,29.9,27.5,25.0,23.8,22.9]

print(min(temp))
print(max(temp))
print(sum(temp))
print(len(temp))

print(temp[0:5])
print(temp[-3:])
print(temp[::2])
print(temp[::-1])

fahrenheit = [(c * 9/5) + 32 for c in temp]

print(fahrenheit)

temp.append(40)
print(temp)
temp.remove(22.5)
print(temp)

temp.sort(reverse=True)
print(temp)