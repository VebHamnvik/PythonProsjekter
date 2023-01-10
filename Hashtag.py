
def hashtag(setning):
    s = setning

    if len(s) == 0 or len(s) > 140:
        return False

    tegn = "#"
    liste = s.split()
    liste.insert(0, tegn)

    ferdig = []

    for x in liste:
        y = str.title(x)
        ferdig.append(y)

    streng = ''

    for x in ferdig:
        streng += x

    return streng

print(hashtag("Hello world"))