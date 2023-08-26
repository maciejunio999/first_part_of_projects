w = "kakadu"
letter = 'k'

x = w.index(letter)
while letter in w:
    y = list(w)
    y[x] = ''
    w = "".join(y)

print(w)