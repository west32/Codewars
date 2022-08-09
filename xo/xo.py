def xo(s):
    result = True
    if s.lower().count("x") != s.lower().count("o"):
        result = False
    return result
