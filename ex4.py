def count_words(text, words):
    counter = 0
    for i in words:
        if text.lower().find(i) != -1:
            counter += 1
    return counter




print count_words(u"How aresjfhdskfhskd you?", {u"how", u"are", u"you", u"hello"})
count_words(u"Bananas, give me bananas!!!", {u"banana", u"bananas"})
count_words(u"Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {u"sum", u"hamlet", u"infinity", u"anything"})
