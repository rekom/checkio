def checkio(words):
    liste = words.split()
    counter = 0
    for w in liste:
        if w.isalpha() :
            counter = counter + 1
            if counter == 3:
                return True
        else:
            counter = 0
    return False

print checkio(u"Hello World hello")
print checkio(u"He is 123 man")
print checkio(u"1 2 3 4")
print checkio(u"bla bla bla bla")
print checkio(u"Hi")
print checkio("one two 3 four five six 7 eight 9 ten eleven 12")
