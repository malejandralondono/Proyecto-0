
import re 

def div_comandos(text:str):
    """
    Divine los caracteres de los comandos en una lista
    """

    lista = re.split(r"[,()]", text)
    lista = [x for x in lista if x]
    return lista

def rev_jump(text: str):
    """
    Revisa si la accion jump es correcto
    """

    tokens = div_comandos(text)

    try:
        x = int(tokens[1])
        y = int(tokens[2])
    except (IndexError, ValueError):
        return False
    
    if len(tokens) == 3 and tokens[0] == "jump":
        return True

    if not isinstance(x, int) and not isinstance(y, int):
        return True
    
    return False

