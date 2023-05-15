def swap(x, y):
    temp = x
    x = y
    y = temp

    print("x : ", x)
    print("y : ", y)


x = int(input("x : "))
y = int(input("y : "))

print("original value")
print("x : ", x)
print("y : ", y)

print("\n")

print("swaped value")
swap(x, y)
