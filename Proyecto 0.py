import re 

def div_comandos(text:str):
    """
    Divide los caracteres de los comandos en una lista
    """

    lista = re.split(r"[,()]", text)
    lista = [x.strip() for x in lista if x]
    print(lista)
    return lista

def rev_defVar(text1, text2, text3):
    """
    Revisa que los defVar estan bien escritos
    """
    if text1 == "defVar" and type(text2)== str and text3.isnumeric(): 
        return True
    else: 
         return False   

def rev_dec_defProc(text1, text2, text3):
     
     if  text1 == "defProc" and type(text2)== str and text3[0]=="(" and text3[-1]==")" and( (text3[1:-1]).replace(",", "").isnumeric() or (text3[1:-1]).replace(",", "").isalpha()):
          return True
     else: 
         return False   

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
    Revisa si las acciones turn son correctas 
    """
    
    tokens = div_comandos(text)
    
    t_1 = ["left", "right", "around"]
    t_2 = ["north", "south", "west", "east"]

    if len(tokens) == 2 and tokens[0] == "turn" and (tokens[1] in t_1 or tokens[1] in t_2):
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

    if len(tokens) == 1 and tokens[0] == "nop":
        return True
    
    return False

def rev_parentesis_balanced(text: str): 
     
    open_list = ["{","("]
    close_list = ["}",")"]
    
    stack = []
    for i in text:
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                pos = close_list.index(i)
                if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack)-1])):
                    stack.pop()
                else:
                    return False
    if len(stack) == 0:
            return True
    else:
            return False
    
def rev_parentesis_extra(text:str):
     es = True
     if ("[" or "]" or "((" or ")(")in text:
          es = False
     return es

def div_text(text:str):
    x = text.replace(')',' ) ')
    x = x.replace("(", " ( ")
    x = x.replace("{", " { ")
    x = x.replace(")", " ) ")
    x = x.split()
    return x


#def comandos

def entrada_texto(text: str):
    if rev_parentesis_balanced(text) == False:
        return "No"
    if rev_parentesis_extra(text) == False:
        return "No"
    else:
        text = div_text(text)
        while text != []:
            if text[0]== "defVar":
                if rev_defVar(text[0],text[1],text[2])== True:
                    i= 3
                    while i!= 0 :                
                     text.pop(0)
                     i -=1
            elif text[0]== "defProc":
                text0= text[0]
                text1= text[1]
                i= 2
                while i!= 0 :                
                   text.pop(0)
                   i -=1
                cont= True
                x= 0
                text3=""
                while x!=len(text) and (cont):
                    text3 += text[x]
                    if text[x]== ")":
                        cont = False  
                    x +=1
                if (cont):
                    return "No"
                else:
                    if rev_dec_defProc(text0, text1, text3)== True:
                          while x!= 0 :                
                           text.pop(0)
                           x -=1
                if text[0]!="{": 
                     return "No"
                else:
                    cont= True
                    x= 0
                    comandos= ""
                    while x!=len(text) and (cont):
                        comandos += text[x]
                        print(comandos)
                        if text[x]== "}":
                            cont = False  
                        x +=1
                    print(div_comandos(comandos))
        text=[]                  
    return None             
            



         
          
     
    
         
print(entrada_texto("defVar nom 0 defVar x 0 defVar y 0 defVar one 0 defProc putCB (c , b ) { drop( c ) ; letGo ( b ) ; } 3 defProc goNorth () {while can(walk(1 , north ) ) { walk(1 , north ) } } { jump (3 ,3) ; putCB (2 ,1) }"))
