from pygame import *
import sys
import pygame, sys
from pygame.locals import QUIT
import random

modo = ""


xaxa = int(input("Entre um numero: "))
zaza = int(input("Entre um numero: "))
papa = int(input("Entre um numero: "))
sasa = int(input("Entre um numero: "))
baba = int(input("Entre um numero: "))

lista_input = [
    xaxa,zaza,papa,sasa,baba
        ]
tamano = len(lista_input)

nums = [
    100, 120, 130, 120, 150, 100, 160, 200, 190, 110, 115, 125, 135, 170, 130
]

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
    x = random.randint(80, 200)
    lista_nums.append(x)


tamanho_2 = len(lista_nums)

#num = int(input("Entre um numero: "))
#lista_nums.append(num)

pygame.init()
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
            if event.key == pygame.K_1:
                modo = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                modo = 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_3:
                modo = 3
    
    screen.fill(background_color)
    draw(screen)



    if modo == 1:
        for i in range(tamanho_2):
            pygame.draw.rect(screen, (0, 0, 150), (10+i*(1500/tamanho_2), screen_y-lista_nums[i]*2, 1000/tamanho_2, lista_nums[i]*2))
    
    if modo == 2:
        for i in range(tamanho):
            pygame.draw.rect(screen, (150, 0, 0), (10+i*(1500/tamanho), screen_y-nums[i]*2, 1000/tamanho, nums[i]*2))
    


    if modo == 3:
        for i in range(tamano):
            pygame.draw.rect(screen, (0, 150, 0), (10+i*(1500/tamano), screen_y-lista_input[i]*2, 1000/tamano, lista_input[i]*2))


    pygame.display.update()

