# import webbrowser

from Clearing import Clear
Clear()


def about(article):
    import wikipedia
    a = wikipedia.summary(article, sentences=10)
    print(a)
    return a
