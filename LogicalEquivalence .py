def Open(east, west):

    if east and west:
        return(False)

    else:
        return(True)
    
print(Open(False, False))

def whoshockal(x: bool, y: bool):

    if type(x) != bool or type(y) != bool:
        return

    if x == y:
        return False

    else:
        return True


print(whoshockal(True, False))

GCF = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
GCF = GCF[::-1]
GCF = sorted(GCF)
print(GCF)