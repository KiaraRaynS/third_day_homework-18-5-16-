import string


def histogram():
    with open("sample.txt") as opened_file:
        book = opened_file.read()

    for x in string.punctuation:
        book = book.lower()
        book = book.replace(x,'')
        book = book.replace("  ",'')

    book_histogram = {}
    ignore_words = ['a', 'able','about', 'across', 'all', 'if', 'and', 'or', 'we', 'may'
                    'only', 'on', 'i', 'the', 'of', 'to', 'that', 'in', 'it', 'he'
                    'you', 'was', 'his', 'is', 'have', 'had', 'with', 'for', 'my', 'as'
                    'which', 'not', 'at', 'be', 'this', 'he', 'you', 'as', 'which', 'but',
                    'upon', 'me', 'him', 'from', 'said', 'there', 'by', 'so', 'one', 'no',
                    'been', 'are', 'our', 'were', 'man', 'could', 'an', 'will', 'your', 'would',
                    'very', 'do', 'what', 'us', 'has', 'out', 'her', 'should', 'who', 'up', 'when',
                    'some', 'more', 'any', 'she', 'know', 'then', 'see', 'over', 'into', 'they', 'over',
                    'into', 'down', 'only', 'think', 'must', 'than', 'them', 'where', 'here', 'come', 'might',
                    'much', 'came', 'last', 'back', 'other', 'such', 'tell', 'these', 'well', 'their',
                    ]

    for word in book.split(" "):
        if word in ignore_words:
            del(word)
        else:
            if word in book_histogram.keys():
                book_histogram[word] +=1
            else:
                book_histogram[word] = 1

    #for key, value in book_histogram.items():
        #print(key, value)
    import operator
    sorted_hist = sorted(book_histogram.items(), key=operator.itemgetter(1))
    for idx, item in enumerate(sorted_hist[:-21:-1]):
        word, count = item
        symbol_graph_value = round(count % 4)
        print(idx + 1, word.title(), count)
    #print(sorted_hist[:-20:-1])

histogram()