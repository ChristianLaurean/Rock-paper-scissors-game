import random
import os


def winner(win_1, win_2,):
     if win_1 == 3:
          print("                               πβγπΌπΊπ¬πΉ πΎπ°π΅γβπ")
          print("                                   2 player γππΆπΌ π³πΆπΊπ»γ")

     if win_2 == 3:
          print("                                   1 player γππΆπΌ π³πΆπΊπ»γ")
          print("                               πβγπΌπΊπ¬πΉ πΎπ°π΅γβπ")

     







def usr():
    option_usr = input("πΉπΆπͺπ² π·π¨π·π¬πΉ πΊπͺπ°πΊπΊπΆπΉπΊ...: ").lower()
    return option_usr




def opciones():
    opciones = ("rock", "paper", "scissors")
    return opciones




def choose_option(op):
     escoge_cpu = random.choice(op)
     return escoge_cpu




def logic(opcion_usr, opcion_cpu, win_1, win_2):

     if opcion_usr == opcion_cpu:
          print("      β¦γοΉπ»π°π¬οΉγβ¦\n")

     elif opcion_usr == "rock":
        if opcion_cpu == "scissors":
            win_1 += 1
            print("  β¦γοΉπΉπΆπͺπ² π©π¬π¨π»πΊ πΊπͺπ°πΊπΊπΆπΉπΊοΉγβ¦\n")
        else:
            print("  β¦γοΉπ·π¨π·π¬πΉ π©π¬π¨π»πΊ πΉπΆπͺπ²οΉγβ¦\n")
            win_2 += 1


     elif opcion_usr == "paper":
        if opcion_cpu == "rock":
            win_1 += 1
            print("  β¦γοΉπ·π¨π·π¬πΉ π©π¬π¨π»πΊ πΉπΆπͺπ²οΉγβ¦\n")
        else:
            print("  β¦γοΉπΊπͺπ°πΊπΊπΆπΉπΊ πΎπ°π΅πΊ π·π¨π·π¬πΉοΉγβ¦\n")
            win_2 += 1
          
     elif opcion_usr == "scissors":
        if opcion_cpu == "paper":
            win_1 += 1
            print("  β¦γοΉπΊπͺπ°πΊπΊπΆπΉπΊ πΎπ°π΅πΊ π·π¨π·π¬πΉοΉγβ¦\n")
        else:
            print("  β¦γοΉπΉπΆπͺπ² π©π¬π¨π»πΊ πΊπͺπ°πΊπΊπΆπΉπΊοΉγβ¦\n")
            win_2 += 1

     return win_1, win_2
     



def menu():
        menu = int(input("""


    β§γοΌ·οΌ₯οΌ¬οΌ£οΌ―οΌ­οΌ₯ οΌ΄οΌ― οΌ΄οΌ¨οΌ₯ οΌ§οΌ‘οΌ­οΌ₯ οΌ―οΌ¦ οΌ²οΌ―οΌ£οΌ« οΌ°οΌ‘οΌ°οΌ₯οΌ² οΌ³οΌ£οΌ©οΌ³οΌ³οΌ―οΌ²οΌ³γβ§




                                1- π₯οΌοΉ1 π½πΊ πͺπ·πΌοΉοΌπ₯
                                
                                2- π₯οΌοΉ1 π½πΊ 1οΉοΌπ₯


                                
                οΌ΄ο½ο½ ο½ο½ο½ο½ο½ ο½ο½ ο½ο½ο½ 3 ο½ο½ο½ο½ο½ο½ ο½ο½ο½ο½.



    Cο½ο½ο½ο½ο½ ο½ο½ ο½ο½ο½ο½ο½ο½: """))
        return menu

menu = menu()




def game(men):
    if men == 1:
       
       win_1 = 0 
       win_2 = 0 

       while win_1 < 4 and win_2 < 4:

        print(f"  πΌπΊπ¬πΉ: {win_1} ===== πͺπ·πΌ: {win_2}")
        winner(win_1, win_2)
        opciones_pc = opciones()
        usuario_1 = usr()
        
        if not usuario_1  in opciones_pc:
             print("Escoge una opcion correcta")
             continue 

        cpu_option = choose_option(opciones_pc)

        print(f"   οΌοΉπΌπΊπ¬πΉοΉοΌ:   {usuario_1}")
        print(f"    οΌοΉπͺπ·πΌοΉοΌ:   {cpu_option}\n")

        win_1, win_2 = logic(usuario_1,cpu_option, win_1, win_2)
        
        


                
    if men == 2:
       
       win_1 = 0 
       win_2 = 0 

       while True:
        print(f"  πΌπΊπ¬πΉ: {win_1} ===== πͺπ·πΌ: {win_2}")
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




        print(f"   οΌοΉπΌπΊπ¬πΉοΉοΌ:   {usuario_1}")
        print(f"    οΌοΉπͺπ·πΌοΉοΌ:   {usuario_2}\n")

        win_1, win_2 = logic(usuario_1,usuario_2, win_1, win_2)
        
        
    else:
        print("οΌ΄οΌ¨οΌ‘οΌ΄ οΌ―οΌ°οΌ΄οΌ©οΌ―οΌ? οΌ©οΌ³ οΌ?οΌ―οΌ΄ οΌ¦οΌ―οΌ΅οΌ?οΌ€ οΌ©οΌ? οΌ΄οΌ¨οΌ₯ οΌ€οΌ‘οΌ΄οΌ‘οΌ’οΌ‘οΌ³οΌ₯.\n")
                          
game(menu)      