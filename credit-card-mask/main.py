def maskify(cc):
    if len(cc) < 4:
        return cc
    after = cc[-4:]
    before = "#"*int(len(cc)-4)
    return before+after