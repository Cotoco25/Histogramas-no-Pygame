from pygame import *
import sys
import pygame, sys
from pygame.locals import QUIT
import random

modo = ""


xaxa1 = ""
xaxa2 = ""
xaxa3 = ""
xaxa4 = ""
xaxa5 = ""

lista_input = [
    xaxa1,xaxa2,xaxa3,xaxa4,xaxa5
        ]
tamano = len(lista_input)



nums = [
    400, 320, 130, 720, 50, 600, 360, 200, 190, 710, 515, 225, 435, 170, 330
]

conta = ""

def numeros(event):
    global conta
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
            conta = conta[:-1]
        elif event.unicode.isnumeric():
            conta += event.unicode






tamanhooo = len(nums)
tamanho = random.randint(1,tamanhooo)
num_cat = 4
num_min = min(nums)
num_max = max(nums)
tam_cat = (num_max - num_min) / num_cat
lista_total = [0] * num_cat



background_color = (112, 128, 144)
def contabiliza_totais(nums, lista_total):
    #para cada n na minha lista
    for i in range(len(nums)):
        if nums[i] == num_max:
            lista_total[-1] += 1
            continue
        #para cada faixa/categoria
        for i_cat in range(num_cat):
            #obtem os limites inferior e superior
            lim_inf = num_min + i_cat + tam_cat
            lim_sup = lim_inf + tam_cat

            #checa em qual faixa / categoria o N esta com base nesses limites
            if lim_inf <= nums[i] < lim_sup:
                lista_total[i_cat] += 1
                break
            return lista_total

def draw(screen):
    screen_h =  screen.get_height()
    for i in range(len(lista_total)):
        x = 100 + i * 50
        h = 20 * lista_total[i]
        pygame.draw.rect(screen, (255, 0, 0), (x, 0 , 25, h))

lista_nums = [
    
    ]
x = random.randint(80, 200)
for i in range(50):
    x = random.randint(0, 900)
    lista_nums.append(x)


tamanho_2 = len(lista_nums)

#num = int(input("Entre um numero: "))
#lista_nums.append(num)


pygame.init()
fonte = font.Font("Worldstar.ttf", 55)
fonte_pequena = font.Font("Worldstar.ttf", 20)
screen_x = 1500
screen_y = 900
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption('Histograma')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                modo = 1
            elif event.key == pygame.K_w:
                modo = 2
            elif event.key == pygame.K_e:
                modo = 3
                
            if modo == 3:
                numeros(event) 
                
                if event.key == pygame.K_RETURN:
                    if xaxa1 == "":
                        xaxa1 = conta
                    elif xaxa2 == "":
                        xaxa2 = conta
                    elif xaxa3 == "":
                        xaxa3 = conta
                    elif xaxa4 == "":
                        xaxa4 = conta
                    elif xaxa5 == "":
                        xaxa5 = conta
                    
                    conta = "" 

    screen.fill(background_color)
    draw(screen)

    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 10, 900))
    screen.blit(fonte_pequena.render("100", True, (0,0,0)), (10, 770, 10, 10))
    pygame.draw.rect(screen, (0, 0, 0), (0, 800, 30, 10))
    screen.blit(fonte_pequena.render("150", True, (0,0,0)), (10, 720, 10, 10))
    pygame.draw.rect(screen, (0, 0, 0), (0, 750, 30, 10))
    screen.blit(fonte_pequena.render("200", True, (0,0,0)), (10, 670, 10, 10))
    pygame.draw.rect(screen, (0, 0, 0), (0, 700, 30, 10))
    screen.blit(fonte_pequena.render("250", True, (0,0,0)), (10, 620, 10, 10))
    pygame.draw.rect(screen, (0, 0, 0), (0, 650, 30, 10))
    screen.blit(fonte_pequena.render("300", True, (0,0,0)), (10, 570, 10, 10))
    pygame.draw.rect(screen, (0, 0, 0), (0, 600, 30, 10))
    screen.blit(fonte_pequena.render("350", True, (0,0,0)), (10, 520, 10, 10))
    pygame.draw.rect(screen, (0, 0, 0), (0, 550, 30, 10))
    screen.blit(fonte_pequena.render("400", True, (0,0,0)), (10, 470, 10, 10))
    pygame.draw.rect(screen, (0, 0, 0), (0, 500, 30, 10))
    screen.blit(fonte_pequena.render("450", True, (0,0,0)), (10, 420, 10, 10))
    pygame.draw.rect(screen, (0, 0, 0), (0, 450, 30, 10))
    screen.blit(fonte_pequena.render("500", True, (0,0,0)), (10, 370, 10, 10))
    pygame.draw.rect(screen, (0, 0, 0), (0, 400, 30, 10))
    screen.blit(fonte_pequena.render("550", True, (0,0,0)), (10, 320, 10, 10))
    pygame.draw.rect(screen, (0, 0, 0), (0, 350, 30, 10))
    screen.blit(fonte_pequena.render("600", True, (0,0,0)), (10, 270, 10, 10))
    pygame.draw.rect(screen, (0, 0, 0), (0, 300, 30, 10))
    screen.blit(fonte_pequena.render("650", True, (0,0,0)), (10, 220, 10, 10))
    pygame.draw.rect(screen, (0, 0, 0), (0, 250, 30, 10))
    screen.blit(fonte_pequena.render("700", True, (0,0,0)), (10, 170, 10, 10))
    pygame.draw.rect(screen, (0, 0, 0), (0, 200, 30, 10))
    screen.blit(fonte_pequena.render("750", True, (0,0,0)), (10, 120, 10, 10))
    pygame.draw.rect(screen, (0, 0, 0), (0, 150, 30, 10))
    screen.blit(fonte_pequena.render("800", True, (0,0,0)), (10, 70, 10, 10))
    pygame.draw.rect(screen, (0, 0, 0), (0, 100, 30, 10))
    screen.blit(fonte_pequena.render("850", True, (0,0,0)), (10, 20, 10, 10))
    pygame.draw.rect(screen, (0, 0, 0), (0, 50, 30, 10))


    if modo == 1:
        for i in range(tamanho_2):
            pygame.draw.rect(screen, (0, 0, 150), (30+i*(1470/tamanho_2), screen_y-lista_nums[i], 1000/tamanho_2, lista_nums[i]*2))

    if modo == 2:
        for i in range(tamanho):
            pygame.draw.rect(screen, (150, 0, 0), (30+i*(1470/tamanho), screen_y-nums[i], 1000/tamanho, nums[i]*2))
    
    if modo == 3:
        screen.blit(fonte.render("Escreva 5 numeros de 0 a 900", True, (0,0,0)), (530, 40, 100, 100))
        screen.blit(fonte.render(f"{conta}", True, (0,0,0)), (530, 100, 100, 100))

        if xaxa1 != "" and xaxa2 != "" and xaxa3 != "" and xaxa4 != "" and xaxa5 != "":
            lista_input = [int(xaxa1), int(xaxa2), int(xaxa3), int(xaxa4), int(xaxa5)]
            for i in range(tamano):
                pygame.draw.rect(screen, (0, 150, 0), (30+i*(1470/tamano), screen_y-lista_input[i], 1000/tamano, lista_input[i]*2))

    pygame.display.update()

