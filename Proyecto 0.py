import re 

def div_comandos(text:str):
    """
    Divide los caracteres de los comandos en una lista
    """

    lista = re.split(r"[,()]|:", text)
    lista = [x.strip() for x in lista if x]
    return lista

def rev_defVar(text: str):
    """
    Revisa que los defVar estan bien escritos
    """

    tokens = text.split()
    esp = re.match(r"^defVar\s(.*)\s(.*)$", text)

    if tokens[0] == "defVar" and len(tokens) == 3 and tokens[1].isalpha() and (tokens[2].isdigit() or tokens[2].isalpha()) and esp:
         return True

    return False    

def remove_can(text):
    """
    Remover can para verificar el comando
    """
    match = re.match(r"can\((.*)\)", text)

    if match is None:
        return text

    expression = match.group(1)

    return text.replace(match.group(0), expression)

def remove_not(texto: str) -> str:
    """
    Remover not para verificar el condicional
    """

    patron = re.compile(r"^not:")
    return patron.sub('', texto).strip()

def rev_jump(text: str):
    """
    Revisa si la accion jump es correcta
    """

    tokens = div_comandos(text)

    try:
        x, y = int(tokens[1]), int(tokens[2])
    except (IndexError, ValueError):
        return False
    
    if len(tokens) == 3 and tokens[0] == "jump" and isinstance(x, int) and isinstance(y, int):
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
    
    if len(tokens) == 2 and isinstance(x, int) and tokens[0] == "walk":
        return True
    
    if len(tokens) == 3 and isinstance(x, int) and tokens[0] == "walk" and (tokens[2] in w_2 or tokens[2] in w_3):
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
    
    if len(tokens) == 2 and isinstance(x, int) and tokens[0] == "leap":
        return True
    
    if len(tokens) == 3 and isinstance(x, int) and tokens[0] == "leap" and (tokens[2] in l_2 or tokens[2] in l_3):
        return True

    return False

def rev_turn(text: str):
    """
    Revisa si la accion turn es correcta 
    """
    
    tokens = div_comandos(text)
    t = ["left", "right", "around"]

    if len(tokens) == 2 and tokens[0] == "turn" and tokens[1] in t:
        return True 
        
    return False

def rev_turnto(text: str):
    """
    Revisa si la accion turnto es correcta
    """

    tokens = div_comandos(text)
    t=  ["north", "south", "west", "east"]

    if len(tokens) == 2 and tokens[0] == "turnto" and tokens[1] in t:
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
    
    if len(tokens) == 2 and isinstance(x, int) and tokens[0] == "drop":
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
    
    if len(tokens) == 2 and isinstance(x, int) and tokens[0] == "get":
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
    
    if len(tokens) == 2 and isinstance(x, int) and tokens[0] == "grab":
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
    
    if len(tokens) == 2 and isinstance(x, int) and tokens[0] == "letGo":
        return True
    
    return False

def rev_nop(text: str):
    """
    Revisa si la accion nop es correcta
    """

    tokens = div_comandos(text)

    if len(tokens) == 1 and text == "nop()" and tokens[0] == "nop":
        return True
    
    return False

def rev_facing(text: str):
    """
    Revisar si el condicional facing esta bien 
    """

    f = ["north", "south", "west", "east"]
    tokens = div_comandos(text)

    if len(tokens) == 2 and tokens[1] in f and tokens[0] == "facing":
         return True
    
    return False

def rev_can(text: str):
    """
    Revisar si el condicional can esta bien
    """
    commands = ["jump", "walk", "leap", "turn", "turnto", "drop", "get", "grab", "letGo", "nop"]

    tokens = div_comandos(text)
    buscar_comando = commands.index(tokens[1])
    comando = remove_can(text)

    if (2 <= len(tokens) <= 4) and tokens[1] in commands and tokens[0] == "can":
        if buscar_comando == 0:
            return rev_jump(comando)
        elif buscar_comando == 1:
            return rev_walk(comando)
        elif buscar_comando == 2:
            return rev_leap(comando)
        elif buscar_comando == 3:
            return rev_turn(comando)
        elif buscar_comando == 4:
            return rev_turnto(comando)
        elif buscar_comando == 5:
            return rev_drop(comando)
        elif buscar_comando == 6:
            return rev_get(comando)
        elif buscar_comando == 7:
            return rev_grab(comando)
        elif buscar_comando == 8:
            return rev_letGo(comando)
        elif buscar_comando == 9:
            return rev_nop(comando)

    return False

def rev_not(text: str):

    tokens = div_comandos(text)
    condicional = remove_not(text)

    if tokens[0] == "not":
        if tokens[1] == "facing":
            return rev_facing(condicional)
        elif tokens[1] == "can":
            return rev_can(condicional)
        elif tokens[1] == "not":
            return rev_not(condicional)
        
    return False