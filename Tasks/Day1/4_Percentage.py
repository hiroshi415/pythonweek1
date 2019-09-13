a = input("Score for Python: ")
b = input("Score for PHP: ")
c = input("Score for JS: ")
d = input("Score for Java: ")
e = input("Score for Math: ")
f = input("Score for English: ")

sum = int(a)+int(b)+int(c)+int(d)+int(e)+int(f)
perc = sum/6

print(f"Your total score is {sum} and the average is {perc}%")