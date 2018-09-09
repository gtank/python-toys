def reverse(s):
    return "".join([s[(len(s)-1)-i] for i in range(len(s))])
