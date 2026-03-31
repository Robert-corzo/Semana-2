edad = 17
if edad == 18:
    print ("Mayor de edad")
elif edad  < 18:
    print("niño")
else:
    print("muy viejo")
    

# while loop: repeat code as long as condition is True
spam = 0
while spam < 5:  # Continue while spam is less than 5
    print('Hello, world.')
    spam = spam + 1  # Increment counter to avoid infinite loop

print()

for i in range(5):
    print(f'Will stop at 5! or 4? ({i})')

print()
for i in range(3, -1, -1):
    print(i)