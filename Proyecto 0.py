import re 

w_2 = ["front", "right", "left", "back"] 
w_3 = ["north", "south", "west", "east"]
commands = ["jump", "walk", "leap", "turn", "turnto", "drop", "get", "grab", "letGo", "nop"]
lista_variables = []
lista_proc= {}

def rev_defVar(text1, text2, text3):
    """
    Revisa que los defVar estan bien escritos
    """
    text2
    if text1 == "defVar" and type(text2)== str and text3.isnumeric(): 
        return True
    else: 
         return False   

def rev_dec_defProc(text1, text2, text3):
     
     if  text1 == "defProc" and type(text2)== str and text3[0]=="(" and text3[-1]==")" and( (text3[1:-1]).replace(",", "").isnumeric() or (text3[1:-1]).replace(",", "").isalpha() or (text3[1:-1])== ""):
          return True
     else: 
         return False   

def rev_jump(text: str, es_parte_proc):
    """
    Revisa si la accion jump es correcta
    """
    x= text.replace("jump","jump " )
    x = x.replace(')','')
    x = x.replace("(", "")
    tokens = div_text(x)  

    if  (es_parte_proc[0]) :
        if tokens[0] == "jump":
            if len(tokens) == 4:
                if (tokens[1].isnumeric() or tokens[1] in lista_variables or tokens[1] in lista_proc[es_parte_proc[1]]) and tokens[2] == "," and (tokens[3].isnumeric() or tokens[3] in lista_variables or tokens[3] in lista_proc[es_parte_proc[1]]):
                    return True 
                else: 
                    return False
            else:
                return False    
        else:
            return False
    else:
        if tokens[0] == "jump":
            if len(tokens) == 4:
                if (tokens[1].isnumeric() or tokens[1] in lista_variables) and tokens[2] == "," and (tokens[3].isnumeric() or tokens[3] in lista_variables):
                    return True 
                else: 
                    return False
            else:
                return False    
        else:
            return False

def rev_walk(text: str, es_parte_proc):
    """
    Revisa si las acciones walk son correctas
    """
    w_2 = ["front", "right", "left", "back"] 
    w_3 = ["north", "south", "west", "east"]

    x= text.replace("walk","walk " )
    x = x.replace(')','')
    x = x.replace("(", "")
    tokens = div_text(x)    
    
    if  (es_parte_proc[0]) :
        if tokens[0] == "walk":
            if len(tokens) == 2:
                if (tokens[1].isnumeric() or tokens[1] in lista_variables or tokens[1] in lista_proc[es_parte_proc[1]]):
                    return True
                else: 
                    return False
            elif len(tokens) == 4:
                if (tokens[1].isnumeric() or tokens[1] in lista_variables or tokens[1] in lista_proc[es_parte_proc[1]]) and tokens[2] == "," and (tokens[3] in w_2 or tokens[3] in w_3):
                    return True 
                else: 
                    return False
            else: 
                return False
        else:
            return False
    else:
        if tokens[0] == "walk":
            if len(tokens) == 2:
                if (tokens[1].isnumeric() or tokens[1] in lista_variables):
                    return True
                else: 
                    return False
            elif len(tokens) == 4:
                if (tokens[1].isnumeric() or tokens[1] in lista_variables) and tokens[2] == "," and (tokens[3] in w_2 or tokens[3] in w_3):
                    return True 
                else: 
                    return False
            else: 
                return False
        else:
            return False
        
def rev_leap(text: str, es_parte_proc):
    """
    Revisa si las acciones leap son correctas
    """

    w_2 = ["front", "right", "left", "back"] 
    w_3 = ["north", "south", "west", "east"]

    x= text.replace("leap","leap " )
    x = x.replace(')','')
    x = x.replace("(", "")
    tokens = div_text(x)    
    
    if  (es_parte_proc[0]) :
        if tokens[0] == "leap":
            if len(tokens) == 2:
                if (tokens[1].isnumeric() or tokens[1] in lista_variables or tokens[1] in lista_proc[es_parte_proc[1]]):
                    return True
                else: 
                    return False
            elif len(tokens) == 4:
                if (tokens[1].isnumeric() or tokens[1] in lista_variables or tokens[1] in lista_proc[es_parte_proc[1]]) and tokens[2] == "," and (tokens[3] in w_2 or tokens[3] in w_3):
                    return True 
                else: 
                    return False
            else: 
                return False
        else:
            return False
    else:
        if tokens[0] == "leap":
            if len(tokens) == 2:
                if (tokens[1].isnumeric() or tokens[1] in lista_variables):
                    return True
                else: 
                    return False
            elif len(tokens) == 4:
                if (tokens[1].isnumeric() or tokens[1] in lista_variables) and tokens[2] == "," and (tokens[3] in w_2 or tokens[3] in w_3):
                    return True 
                else: 
                    return False
            else: 
                return False
        else:
            return False
    
def rev_turn(text: str, es_parte_proc):
    """
    Revisa si la accion turn es correcta 
    """
    
    t = ["left", "right", "around"]
    
    x= text.replace("turn","turn " )
    x = x.replace(')','')
    x = x.replace("(", "")
    tokens = div_text(x)
    
    if len(tokens) == 2 and tokens[0] == "turn" and (tokens[1] in t ):
        return True
    else:
        return False

def rev_turnto(text: str, es_parte_proc):
    """
    Revisa si la accion turnto es correcta
    """
    t=  ["north", "south", "west", "east"]

    x= text.replace("turnto","turnto " )
    x = x.replace(')','')
    x = x.replace("(", "")
    tokens = div_text(x)

    if len(tokens) == 2 and tokens[0] == "turnto" and tokens[1] in t:
        return True 

    return False

def rev_drop(text: str, es_parte_proc):
    """
    Revisa si la accion drop es correcta
    """
    x= text.replace("drop","drop " )
    x = x.replace(')','')
    x = x.replace("(", "")
    tokens = div_text(x)

    if  (es_parte_proc[0]):
        if len(tokens) == 2 and tokens[0] == "drop" and (tokens[1].isnumeric() or tokens[1] in lista_variables or  tokens[1] in lista_proc[es_parte_proc[1]]):
            return True
        else:
            return False
    else:
        if len(tokens) == 2 and tokens[0] == "drop" and (tokens[1].isnumeric() or tokens[1] in lista_variables ):
            return True
        else:
            return False

def rev_get(text: str, es_parte_proc):
    """
    Revisa si la accion get es correcta
    """

    x= text.replace("get","get " )
    x = x.replace(')','')
    x = x.replace("(", "")
    tokens = div_text(x)
    
    if  (es_parte_proc[0]):
        if len(tokens) == 2 and tokens[0] == "get" and (tokens[1].isnumeric() or tokens[1] in lista_variables or  tokens[1] in lista_proc[es_parte_proc[1]]):
            return True
        else:
            return False
    else:
        if len(tokens) == 2 and tokens[0] == "get" and (tokens[1].isnumeric() or tokens[1] in lista_variables ):
            return True
        else:
            return False

def rev_grab(text: str, es_parte_proc):
    """
    Revisa si la accion grab es correcta
    """

    x= text.replace("grab","grab " )
    x = x.replace(')','')
    x = x.replace("(", "")
    tokens = div_text(x)
    
    if  (es_parte_proc[0]):
        if len(tokens) == 2 and tokens[0] == "grab" and (tokens[1].isnumeric() or tokens[1] in lista_variables or  tokens[1] in lista_proc[es_parte_proc[1]]):
            return True
        else:
            return False
    else:
        if len(tokens) == 2 and tokens[0] == "grab" and (tokens[1].isnumeric() or tokens[1] in lista_variables ):
            return True
        else:
            return False

def rev_letGo(text: str, es_parte_proc):
    """
    Revisa si la accion letGo es correcta
    """

    x= text.replace("letGo","letGo " )
    x = x.replace(')','')
    x = x.replace("(", "")
    tokens = div_text(x)
    
    if  (es_parte_proc[0]):
        if len(tokens) == 2 and tokens[0] == "letGo" and (tokens[1].isnumeric() or tokens[1] in lista_variables or  tokens[1] in lista_proc[es_parte_proc[1]]):
            return True
        else:
            return False
    else:
        if len(tokens) == 2 and tokens[0] == "letGo" and (tokens[1].isnumeric() or tokens[1] in lista_variables ):
            return True
        else:
            return False
    
def rev_nop(text: str , es_parte_proc):
    """
    Revisa si la accion nop es correcta
    """

    x= text.replace("nop","nop " )
    x = x.replace(')','')
    x = x.replace("(", "")
    tokens = div_text(x)

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
    x= x.replace(",", " , ")
    x = x.replace("(", " ( ")
    x = x.replace("{", " { ")
    x = x.replace("}", " } ")
    x = x.split()
    return x

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

def rev_comandos(text, es_parte):
        text= text.replace(";", " ; ")
        text= text.replace(",", " , ")
        text= text.replace("{","")
        text= div_text(text)
        
        mas= True
        while text!=[] and (mas):
            cont= True
            x= 0
            cmd=""
            while x!=len(text) and (cont):
                cmd += text[x]
                if text[x]==")":
                    cont = False
                x +=1
            cmd= cmd.replace(";", " ; ")
            cmd= cmd.replace(",", " , ")
            comando= div_text(cmd)
            if comando[0]== "jump":
                if rev_jump(cmd,es_parte) == False:
                    mas = False
                    return False
                else:
                    while x+1!= 0 :                
                        text.pop(0)
                        x -=1
            elif comando[0]== "walk":
                if rev_walk(cmd,es_parte) == False:
                    mas = False
                    return False
                else:
                    while x+1!= 0 :                
                        text.pop(0)
                        x -=1
            elif comando[0]== "leap":
                if rev_leap(cmd, es_parte) == False:
                    mas = False
                    return False
                else:
                    while x+1!= 0 :                
                        text.pop(0)
                        x -=1
            elif comando[0]== "turn":
                if rev_turn(cmd, es_parte) == False:
                    mas = False
                    return False
                else:
                    while x+1!= 0 :                
                        text.pop(0)
                        x -=1
            elif comando[0]== "turnto":
                if rev_turnto(cmd, es_parte) == False:
                    mas = False
                    return False
                else:
                    while x+1!= 0 :                
                        text.pop(0)
                        x -=1
            elif comando[0]== "drop":
                if rev_drop(cmd, es_parte) == False:
                    
                    mas = False
                    return False
                else:
                    while x+1!= 0 :                
                        text.pop(0)
                        x -=1
            elif comando[0]== "get":
                if rev_get(cmd, es_parte) == False:
                    mas = False
                    return False
                else:
                    while x+1!= 0 :                
                        text.pop(0)
                        x -=1
            elif comando[0]== "grab":
                if rev_grab(cmd, es_parte) == False:
                    mas = False
                    return False
                else:
                    while x+1!= 0 :                
                        text.pop(0)
                        x -=1
            elif comando[0]== "letGo":
                if rev_letGo(cmd, es_parte) == False:
                    mas = False
                    return False
                else:
                    while x+1!= 0 :                
                        text.pop(0)
                        x -=1
            elif comando[0]== "nop":
                if rev_nop(cmd, es_parte) == False:
                    mas = False
                    return False
                else:
                    while x+1!= 0 :                
                        text.pop(0)
                        x -=1
            elif comando[0] in lista_proc:
                cmd= div_text(cmd)
                cmd.remove(comando[0])
                cmd.remove(",")
                cmd= cmd[1:-1]
                if len(cmd)!= len(lista_proc[comando[0]]):
                    return False
                else:
                    while x+1!= 0 :                
                        text.pop(0)
                        x -=1
            else:
                mas = False
                return False
        if text == [] :
            return True

def entrada_texto(text: str):

    if rev_parentesis_balanced(text) == False:
        return "No1"
    if rev_parentesis_extra(text) == False:
        return "No2"
    else:
        no_es_parte_proc= (False,1)
        text = div_text(text)
        while text != []:
            if text[0]== "defVar":
                lista_variables.append(text[1])
                if rev_defVar(text[0],text[1],text[2])== True:
                    i= 3
                    while i!= 0 :                
                     text.pop(0)
                     i -=1
                else:
                    return "No3"
            elif text[0]== "defProc":
                lista= []
                text0= text[0]
                text1= text[1]
                es_parte_proc = (True, text[1])
                i= 2
                while i!= 0 :                
                   text.pop(0)
                   i -=1
                cont= True
                x= 0
                text3=""
                while x!=len(text) and (cont):
                    text3 += text[x]
                    if text[x].isalpha():
                        lista.append(text[x])
                    if text[x]== ")":
                        cont = False  
                    x +=1
                lista_proc[text1] = lista
                if (cont):
                    return "No4"
                else:
                    if rev_dec_defProc(text0, text1, text3)== True:
                          while x!= 0 :                
                           text.pop(0)
                           x -=1
                    else:
                        return "No5"
                if text ==[]:
                    return "No6"
                elif text[0]!="{": 
                     return "No7"
                else:
                    if text[1]== "while" and text[2]!= "can":
                        return "No8"
                    elif text[1]== "while":
                        text.remove("{")
                        text.remove("while")
                        text.remove("can")
                        text.remove("}")
                        cont= True
                        lqvddw= ""
                        np=0
                        np2=0
                        w=0
                        while cont:
                            lqvddw += text[w]
                            if text[w]== "(":
                                np +=1
                            if text[w]== ")":
                                np2 +=1
                            if np == np2:
                                cont = False
                            w +=1
                        lqvddw=lqvddw.replace("(","",1)
                        lqvddw=lqvddw.replace(")","",1)
                        while w!=0:
                            text.pop(0)
                            w-=1
                        si= True
                        x= 0
                        comandos= ""
                        n_corch = 0
                        n_corch2 = 0
                        while si:
                            comandos += text[x]
                            if text[x]== "{":
                                n_corch +=1
                            if text[x]== "}":
                                n_corch2 +=1
                            if n_corch == n_corch2:
                                si = False
                            x +=1
                        if comandos[1:-1] != lqvddw:
                            return "No9"
                        elif rev_comandos(comandos, (es_parte_proc))== True:
                            while x!= 0 :                
                                text.pop(0)
                                x -=1
                        else:
                            return "No10"
                    
                    elif text[1]== "if" and text[2]!= "can":
                        return "No11"
                    elif text[1]== "if":
                        text.remove("{")
                        text.remove("if")
                        text.remove("can")
                        cont= True
                        lqvddw= ""
                        np=0
                        np2=0
                        w=0
                        while cont:
                            lqvddw += text[w]
                            if text[w]== "(":
                                np +=1
                            if text[w]== ")":
                                np2 +=1
                            if np == np2:
                                cont = False
                            w +=1
                        lqvddw=lqvddw.replace("(","",1)
                        lqvddw=lqvddw.replace(")","",1)
                        while w!=0:
                            text.pop(0)
                            w-=1
                        si= True
                        x= 0
                        comandos= ""
                        n_corch = 0
                        n_corch2 = 0
                        while si:
                            comandos += text[x]
                            if text[x]== "{":
                                n_corch +=1
                            if text[x]== "}":
                                n_corch2 +=1
                            if n_corch == n_corch2:
                                si = False
                            x +=1
                        if lqvddw not in comandos[1:-1]:
                            return "No12"
                        elif rev_comandos(comandos, (es_parte_proc))== True:
                            
                            while x!= 0 :                
                                text.pop(0)
                                x -=1
                        else:
                            return "No13" 
                        if text[0]== "else":
                            text.remove("else")
                            text.remove("}")
                            si= True
                            x= 0
                            comandos= ""
                            n_corch = 0
                            n_corch2 = 0
                            while si:
                                comandos += text[x]
                                if text[x]== "{":
                                    n_corch +=1
                                if text[x]== "}":
                                    n_corch2 +=1
                                if n_corch == n_corch2:
                                    si = False
                                x +=1
                            if rev_comandos(comandos, (es_parte_proc))== True:
                                while x!= 0 :                
                                    text.pop(0)
                                    x -=1
                            else:
                                return "No14"
                    else:
                        si= True
                        x= 0
                        comandos= ""
                        n_corch = 0
                        n_corch2 = 0
                        while si:
                            comandos += text[x]
                            if text[x]== "{":
                                n_corch +=1
                            if text[x]== "}":
                                n_corch2 +=1
                            if n_corch == n_corch2:
                                si = False
                            x +=1
                    if rev_comandos(comandos, (es_parte_proc))== True:
                        while x!= 0 :                
                            text.pop(0)
                            x -=1
                    else:
                        return "No15"
            elif text[0]== "{":
                si= True
                x= 0
                comandos= ""
                n_corch = 0
                n_corch2 = 0
                while si:
                    comandos += text[x]
                    if text[x]== "{":
                        n_corch +=1
                    if text[x]== "}":
                        n_corch2 +=1
                    if n_corch == n_corch2:
                        si = False
                    x +=1
                if rev_comandos(comandos, (no_es_parte_proc))== True:
                        while x!= 0 :                
                            text.pop(0)
                            x -=1
                else:
                    return "No16"
            elif text[0] in commands or text[0] in lista_proc:
                comandos = text[0]
                text.pop(0)
                si= True
                x= 0
                n_corch = 0
                n_corch2 = 0
                while si:
                    comandos += text[x]
                    if text[x]== "(":
                        n_corch +=1
                    if text[x]== ")":
                        n_corch2 +=1
                    if n_corch == n_corch2:
                        si = False
                    x +=1
                if rev_comandos(comandos, (no_es_parte_proc))== True:
                        while x!= 0 :                
                            text.pop(0)
                            x -=1
            elif text[0] in lista_variables:
                text.pop(0)
                text.remove("=")
                if (text[0].isalnum)== False or text[0] not in w_3 or text[0] not in w_2:
                    return False
                else:
                    text.pop(0)
                    if text[0]== ",":
                        text.pop(0)
            elif text[1]== "while" and text[2]!= "can":
                        return "No8"
            elif text[1]== "while":
                        text.remove("{")
                        text.remove("while")
                        text.remove("can")
                        text.remove("}")
                        cont= True
                        lqvddw= ""
                        np=0
                        np2=0
                        w=0
                        while cont:
                            lqvddw += text[w]
                            if text[w]== "(":
                                np +=1
                            if text[w]== ")":
                                np2 +=1
                            if np == np2:
                                cont = False
                            w +=1
                        lqvddw=lqvddw.replace("(","",1)
                        lqvddw=lqvddw.replace(")","",1)
                        while w!=0:
                            text.pop(0)
                            w-=1
                        si= True
                        x= 0
                        comandos= ""
                        n_corch = 0
                        n_corch2 = 0
                        while si:
                            comandos += text[x]
                            if text[x]== "{":
                                n_corch +=1
                            if text[x]== "}":
                                n_corch2 +=1
                            if n_corch == n_corch2:
                                si = False
                            x +=1
                        if comandos[1:-1] != lqvddw:
                            return "No9"
                        elif rev_comandos(comandos, (no_es_parte_proc))== True:
                            while x!= 0 :                
                                text.pop(0)
                                x -=1
                        else:
                            return "No10"
                    
            elif text[1]== "if" and text[2]!= "can":
                return "No11"
            elif text[1]== "if":
                text.remove("{")
                text.remove("if")
                text.remove("can")
                cont= True
                lqvddw= ""
                np=0
                np2=0
                w=0
                while cont:
                    lqvddw += text[w]
                    if text[w]== "(":
                        np +=1
                    if text[w]== ")":
                        np2 +=1
                    if np == np2:
                        cont = False
                    w +=1
                lqvddw=lqvddw.replace("(","",1)
                lqvddw=lqvddw.replace(")","",1)
                while w!=0:
                    text.pop(0)
                    w-=1
                si= True
                x= 0
                comandos= ""
                n_corch = 0
                n_corch2 = 0
                while si:
                    comandos += text[x]
                    if text[x]== "{":
                        n_corch +=1
                    if text[x]== "}":
                        n_corch2 +=1
                    if n_corch == n_corch2:
                        si = False
                    x +=1
                if lqvddw not in comandos[1:-1]:
                    return "No12"
                elif rev_comandos(comandos, (no_es_parte_proc))== True:
                    
                    while x!= 0 :                
                        text.pop(0)
                        x -=1
                else:
                    return "No13" 
                if text[0]== "else":
                    text.remove("else")
                    text.remove("}")
                    si= True
                    x= 0
                    comandos= ""
                    n_corch = 0
                    n_corch2 = 0
                    while si:
                        comandos += text[x]
                        if text[x]== "{":
                            n_corch +=1
                        if text[x]== "}":
                            n_corch2 +=1
                        if n_corch == n_corch2:
                            si = False
                        x +=1
                    if rev_comandos(comandos, (no_es_parte_proc))== True:
                        while x!= 0 :                
                            text.pop(0)
                            x -=1
                    else:
                        return "No14"
    return "Si"             
            
print("escriba el texto a revisar")
x= input()
print(entrada_texto(x))