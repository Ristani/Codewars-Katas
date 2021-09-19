def lovefunc(flower1, flower2):
    if flower1 % 2 == 0 and flower2 % 2 != 0:
        return True
    elif flower1 % 2 != 0 and flower2 % 2 == 0:
        return True
    return False


def lovefunc2(flower1, flower2):
    return (flower1 + flower2) % 2
