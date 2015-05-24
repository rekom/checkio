def find_message(text):
    """Find a secret message"""
    result = ""
    for i in text :

        if i.isupper() == True:
            result = result + i

        else :
            pass
    return result






find_message(u"How are you? Eh, ok. Low or Lower? Ohhh.")
find_message(u"hello world!")
find_message(u"HELLO WORLD!!!")
