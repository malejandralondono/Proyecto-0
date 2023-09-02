import re 

def div_comandos(text:str):
    """
    Divine los caracteres de los comandos en una lista
    """

    lista = re.split(r"[,()]", text)
    lista = [x.strip() for x in lista if x]
    return lista

def rev_jump(text: str):
    """
    Revisa si la accion jump es correcta
    """

    tokens = div_comandos(text)

    try:
        x = int(tokens[1])
        y = int(tokens[2])
    except (IndexError, ValueError):
        return False
    
    if len(tokens) == 3 and tokens[0] == "jump":
        if isinstance(x, int) and isinstance(y, int):
            return True
    
    return False

def rev_walk(text: str):
    """
    Revisa si las acciones walk son correctas
    """

    tokens = div_comandos(text)

    w_2 = ["front", "right", "left", "back"] 
    w_3 = ["north", "south", "west", "east"]

    try:
        x = int(tokens[1])
    except (IndexError, ValueError):
        return False
    
    if len(tokens) == 2 and tokens[0] == "walk":
        if isinstance(x, int):
            return True
    
    if len(tokens) == 3 and tokens[0] == "walk":
        if isinstance(x, int):
            if tokens[2] in w_2 or tokens[2] in w_3:
                return True

    return False

def rev_leap(text: str):
    """
    Revisa si las acciones leap son correctas
    """

    tokens = div_comandos(text)

    l_2 = ["front", "right", "left", "back"] 
    l_3 = ["north", "south", "west", "east"]

    try:
        x = int(tokens[1])
    except (IndexError, ValueError):
        return False
    
    if len(tokens) == 2 and tokens[0] == "leap":
        if isinstance(x, int):
            return True
    
    if len(tokens) == 3 and tokens[0] == "leap":
        if isinstance(x, int):
            if tokens[2] in l_2 or tokens[2] in l_3:
                return True

    return False

def rev_turn(text: str):
    """
    Revisa si las acciones turn son correctas 
    """
    
    tokens = div_comandos(text)
    
    t_1 = ["left", "right", "around"]
    t_2 = ["north", "south", "west", "east"]

    if len(tokens) == 2 and tokens[0] == "turn":
        if tokens[1] in t_1 or tokens[1] in t_2:
            return True 
        
    return False

def rev_drop(text: str):
    """
    Revisa si la accion drop es correcta
    """

    tokens = div_comandos(text)

    try:
        x = int(tokens[1])
    except (IndexError, ValueError):
        return False
    
    if len(tokens) == 2 and tokens[0] == "drop":
        if isinstance(x, int):
            return True
    
    return False

def rev_get(text: str):
    """
    Revisa si la accion get es correcta
    """

    tokens = div_comandos(text)

    try:
        x = int(tokens[1])
    except (IndexError, ValueError):
        return False
    
    if len(tokens) == 2 and tokens[0] == "get":
        if isinstance(x, int):
            return True
    
    return False

def rev_grab(text: str):
    """
    Revisa si la accion grab es correcta
    """

    tokens = div_comandos(text)

    try:
        x = int(tokens[1])
    except (IndexError, ValueError):
        return False
    
    if len(tokens) == 2 and tokens[0] == "grab":
        if isinstance(x, int):
            return True
    
    return False

def rev_letGo(text: str):
    """
    Revisa si la accion letGO es correcta
    """

    tokens = div_comandos(text)

    try:
        x = int(tokens[1])
    except (IndexError, ValueError):
        return False
    
    if len(tokens) == 2 and tokens[0] == "letGo":
        if isinstance(x, int):
            return True
    
    return False
