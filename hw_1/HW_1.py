#длинный вариант
string="зима 32нео крестьянин торжествуя 42на на"
l=[]
phrase=string.split()
for word in phrase:
    if word.isalpha():
        l.append(word)
print(l)

#сокращенный вариант
string1="зима 32нео крестьянин торжествуя 42на на"
l=[ word for word in string1.split() if word.isalpha()]
print(l)