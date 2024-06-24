def back(tekst):
    if len(tekst) == 0:
        return tekst
    return back(tekst[1:]) + tekst[0]

print(back("test"))