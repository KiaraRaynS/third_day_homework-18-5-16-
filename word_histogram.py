import string

def histogram():
    with open("sample.txt") as opened_file:
        book = opened_file.read()

    for x in string.punctuation:
        book = book.replace(x,'')

    book_histogram = {}

    for word in book.split():
        if word in book_histogram.keys():
            book_histogram[word] +=1
        else:
            book_histogram[word] = 1

    for key, value in book_histogram.items():
        if key >= 2:
            print(key, value)

histogram()