def assign_integer(t: tuple[int]):    
    try:
        t[0] += 1
    except TypeError as e:
        print(e)
    

def assign_list(t: tuple[list[str]]):    
    try:
        t[0] += ["truc"]
    except TypeError as e:
        print(e)