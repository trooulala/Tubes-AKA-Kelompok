import pygame
import random
import time

pygame.font.init()
startTime = time.time()
n = 151
screen = pygame.display.set_mode(
    (900, 650)
)

pygame.display.set_caption("SORTING VISUALISER")

run = True

width = 900
length = 600
array = [0] * n
arr_clr = [(0, 204, 102)] * n
clr_ind = 0
clr = [(0, 204, 102), (255, 0, 0), \
        (0, 0, 153), (255, 102, 0)]
fnt = pygame.font.SysFont("Helvetica", 30)
fnt1 = pygame.font.SysFont("Helvetica", 20)

def generate_arr():
    for i in range(1, n):
        arr_clr[i] = clr[0]
        array[i] = random.randrange(1, 100)

generate_arr()

def refill():
    screen.fill((255, 255, 255))
    draw()
    pygame.display.update()
    pygame.time.delay(20)

def insertionSort(arr):
    for i in range(1, len(arr)): #Cek dari 1 sampai panjang array
        pygame.event.pump()
        refill()
        key = arr[i]        #Key melambangkan data yang saat ini dibandingkan
        arr_clr[i] = clr[2]
        j = i - 1           #j melambangkan posisi untuk data yang sedang dibandingkan
        while j >= 0 and key < arr[j]:
            arr_clr[j] = clr[2]
            arr[j+1] = arr[j]          #Memindahkan element dari arr[0..i-1], yang paling gede dari key
            refill()
            arr_clr[j] = clr[3]
            j -= 1                     #menuju satu posisi di depan posisi saat ini
        arr[j+1] = key
        refill()
        arr_clr[i] = clr[0]

def draw():
    txt = fnt.render("SORT: PRESS 'ENTER'", \
                     1, (0, 0, 0))
    screen.blit(txt, (20, 20))
    txt1 = fnt.render("NEW ARRAY: PRESS 'R'", \
                      1, (0, 0, 0))
    screen.blit(txt1, (20, 50))
    txt2 = fnt1.render("ALGORITHM USED:" \
                       "INSERTION SORT", 1, (0, 0, 0))
    screen.blit(txt2, (600, 60))
    # text3 = fnt1.render("Running Time(sec): " + \
    #                     str(int(time.time() - startTime)), \
    #                     1, (0, 0, 0))
    # screen.blit(text3, (600, 20))
    element_width = (width - 200) // 150
    boundry_arr = 900 / 150
    boundry_grp = 550 / 100
    pygame.draw.line(screen, (0, 0, 0), (0, 95), \
                     (1024, 95), 6)

    for i in range(1, n):
        pygame.draw.line(screen, arr_clr[i], \
                         (boundry_arr * i - 3, 100), \
                         (boundry_arr * i - 3, \
                          array[i] * boundry_grp + 100), element_width)

while run:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                generate_arr()
            if event.key == pygame.K_RETURN:
                insertionSort(array)
    draw()
    pygame.display.update()

pygame.quit()