import random
import os


def winner(win_1, win_2):
     if win_1 == 3:
          print("Gano usr1")

     if win_2 == 3:
          print("Gano usr2")




def usuarios():
    usuarios = input("piedra, papel o tijera: ").lower()

    return usuarios




def opciones():
    opciones = ("piedra", "papel", "tijera")
    
    return opciones




def escoger_pc(op):
     escoge_cpu = random.choice(op)
     
     return escoge_cpu




def logic(opcion_usr, opcion_cpu, win_1, win_2):

     if opcion_usr == opcion_cpu:
          print("Empate")

     elif opcion_usr == "piedra":
          if opcion_cpu == "tijera":
               print("Piedra gana a tijera")
               win_1 += 1
          else:
               print("Papel gana a piedra")
               win_2 += 1

     elif opcion_usr == "papel":
          if opcion_cpu == "piedra":
               print("Papel gana a Piedra")
               win_1 += 1
          else:
               print("Tijera gana a Papel")
               win_2 += 1
     
     elif opcion_usr == "tijera":
          if opcion_cpu == "papel":
               print("Tijera gana a Papel")
               win_1 += 1
          else:
               print("Piedra gana a Tijera")
               win_2 += 2

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
       while True:
        print(win_1, win_2)
        winner(win_1, win_2)
        opciones_pc = opciones()
        usuario_1 = usuarios()
        
        if not usuario_1  in opciones_pc:
             print("Escoge una opcion correcta")
             continue 

        

        cpu_option = escoger_pc(opciones_pc)

        print(f"   （﹙𝑼𝑺𝑬𝑹﹚）:   {usuario_1}")
        print(f"    （﹙𝑪𝑷𝑼﹚）:   {cpu_option}\n")

        win_1, win_2 = logic(usuario_1,cpu_option, win_1, win_2)
        
        


                
    if men == 2:
       
       win_1 = 0 
       win_2 = 0 

       while True:
        print(win_1, win_2)
        winner(win_1, win_2)

        opciones_pl = opciones()

        usuario_1 = usuarios() 
        
        if not usuario_1  in opciones_pl:
             print("Escoge una opcion correcta")
             continue

        usuario_2 = usuarios()
        if not usuario_2  in opciones_pl:
             print("Escoge una opcion correcta")
             continue




        print(f"   （﹙𝑼𝑺𝑬𝑹﹚）:   {usuario_1}")
        print(f"    （﹙𝑪𝑷𝑼﹚）:   {usuario_2}\n")

        win_1, win_2 = logic(usuario_1,usuario_2, win_1, win_2)
        
        
    else:
            pass
            
                
game(menu)      