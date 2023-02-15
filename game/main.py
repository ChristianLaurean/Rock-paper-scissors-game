import random
import os


def winner(win_1, win_2,):
     if win_1 == 3:
          print("                               🏆♕【𝑼𝑺𝑬𝑹 𝑾𝑰𝑵】♕🏆")
          print("                                   2 player 【𝒀𝑶𝑼 𝑳𝑶𝑺𝑻】")

     if win_2 == 3:
          print("                                   1 player 【𝒀𝑶𝑼 𝑳𝑶𝑺𝑻】")
          print("                               🏆♕【𝑼𝑺𝑬𝑹 𝑾𝑰𝑵】♕🏆")

     







def usr():
    option_usr = input("𝑹𝑶𝑪𝑲 𝑷𝑨𝑷𝑬𝑹 𝑺𝑪𝑰𝑺𝑺𝑶𝑹𝑺...: ").lower()
    return option_usr




def opciones():
    opciones = ("rock", "paper", "scissors")
    return opciones




def choose_option(op):
     escoge_cpu = random.choice(op)
     return escoge_cpu




def logic(opcion_usr, opcion_cpu, win_1, win_2):

     if opcion_usr == opcion_cpu:
          print("      ✦〔﹝𝑻𝑰𝑬﹞〕✦\n")

     elif opcion_usr == "rock":
        if opcion_cpu == "scissors":
            win_1 += 1
            print("  ✦〔﹝𝑹𝑶𝑪𝑲 𝑩𝑬𝑨𝑻𝑺 𝑺𝑪𝑰𝑺𝑺𝑶𝑹𝑺﹞〕✦\n")
        else:
            print("  ✦〔﹝𝑷𝑨𝑷𝑬𝑹 𝑩𝑬𝑨𝑻𝑺 𝑹𝑶𝑪𝑲﹞〕✦\n")
            win_2 += 1


     elif opcion_usr == "paper":
        if opcion_cpu == "rock":
            win_1 += 1
            print("  ✦〔﹝𝑷𝑨𝑷𝑬𝑹 𝑩𝑬𝑨𝑻𝑺 𝑹𝑶𝑪𝑲﹞〕✦\n")
        else:
            print("  ✦〔﹝𝑺𝑪𝑰𝑺𝑺𝑶𝑹𝑺 𝑾𝑰𝑵𝑺 𝑷𝑨𝑷𝑬𝑹﹞〕✦\n")
            win_2 += 1
          
     elif opcion_usr == "scissors":
        if opcion_cpu == "paper":
            win_1 += 1
            print("  ✦〔﹝𝑺𝑪𝑰𝑺𝑺𝑶𝑹𝑺 𝑾𝑰𝑵𝑺 𝑷𝑨𝑷𝑬𝑹﹞〕✦\n")
        else:
            print("  ✦〔﹝𝑹𝑶𝑪𝑲 𝑩𝑬𝑨𝑻𝑺 𝑺𝑪𝑰𝑺𝑺𝑶𝑹𝑺﹞〕✦\n")
            win_2 += 1

     return win_1, win_2
     



def menu():
        menu = int(input("""


    ✧【ＷＥＬＣＯＭＥ ＴＯ ＴＨＥ ＧＡＭＥ ＯＦ ＲＯＣＫ ＰＡＰＥＲ ＳＣＩＳＳＯＲＳ】✧




                                1- 🔥（﹙1 𝑽𝑺 𝑪𝑷𝑼﹚）🔥
                                
                                2- 🔥（﹙1 𝑽𝑺 1﹚）🔥


                                
                Ｔｈｅ ｆｉｒｓｔ ｔｏ ｗｉｎ 3 ｒｏｕｎｄｓ ｗｉｎｓ.



    Cｈｏｏｓｅ ａｎ ｏｐｔｉｏｎ: """))
        return menu

menu = menu()




def game(men):
    if men == 1:
       
       win_1 = 0 
       win_2 = 0 

       while win_1 < 4 and win_2 < 4:

        print(f"  𝑼𝑺𝑬𝑹: {win_1} ===== 𝑪𝑷𝑼: {win_2}")
        winner(win_1, win_2)
        opciones_pc = opciones()
        usuario_1 = usr()
        
        if not usuario_1  in opciones_pc:
             print("Escoge una opcion correcta")
             continue 

        cpu_option = choose_option(opciones_pc)

        print(f"   （﹙𝑼𝑺𝑬𝑹﹚）:   {usuario_1}")
        print(f"    （﹙𝑪𝑷𝑼﹚）:   {cpu_option}\n")

        win_1, win_2 = logic(usuario_1,cpu_option, win_1, win_2)
        
        


                
    if men == 2:
       
       win_1 = 0 
       win_2 = 0 

       while True:
        print(f"  𝑼𝑺𝑬𝑹: {win_1} ===== 𝑪𝑷𝑼: {win_2}")
        winner(win_1, win_2)

        opciones_pl = opciones()

        usuario_1 = usr() 
        
        if not usuario_1  in opciones_pl:
             print("Escoge una opcion correcta")
             continue

        usuario_2 = usr()
        if not usuario_2  in opciones_pl:
             print("Escoge una opcion correcta")
             continue




        print(f"   （﹙𝑼𝑺𝑬𝑹﹚）:   {usuario_1}")
        print(f"    （﹙𝑪𝑷𝑼﹚）:   {usuario_2}\n")

        win_1, win_2 = logic(usuario_1,usuario_2, win_1, win_2)
        
        
    else:
        print("ＴＨＡＴ ＯＰＴＩＯＮ ＩＳ ＮＯＴ ＦＯＵＮＤ ＩＮ ＴＨＥ ＤＡＴＡＢＡＳＥ.\n")
                          
game(menu)      