a = 1.234
b = 2.4567
c = 82.641
d = 312.79851

# .x means print x digits
print('a: {0}, b: {1} c: {2} d: {3}'.format(a, b, c, d))
print('a: {0}, b: {1:.3} c: {2:.5} d: {3}'.format(a, b, c, d))
print('---------------------------------')
# .f means print full digits of the stored values
print('Last Number is: {0:.5}'.format(d))
print('Last Number is: {0:f}'.format(d))
print('---------------------------------')
# you can add f in fron tof the '' for format
print('a:{a}, b: {b} c: {c} d: {d}')
print(f'a:{a}, b: {b} c: {c} d: {d}')
print('---------------------------------')
# you can pick from any variable
print('Second Number is: {0:.4}'.format(b))
print('Third Number is: {0:f}'.format(c))
print('---------------------------------')

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
x = thisdict.get("model")
print(x)
