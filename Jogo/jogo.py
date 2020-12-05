import pygame
import random
import time
# Versão teste
# iniciando o pygame
pygame.init()
# Criando a tela
clock = pygame.time.Clock()
tela = pygame.display.set_mode((800, 600))
# Definindo a fonte do sistema
fonte = pygame.font.SysFont("Berlin Sans FB", 40)
# Imagens
background = pygame.image.load("Pictures/bg.png").convert()

imgNave = pygame.image.load("Pictures/spaceship.png")
imgNave = pygame.transform.scale(imgNave, (100,50))
rectNave = imgNave.get_rect()

imgLaser = pygame.image.load("Pictures/laser.png")
imgLaser = pygame.transform.scale(imgLaser, (30,30))
rectLaser = imgLaser.get_rect()

imgInimigo = pygame.image.load("Pictures/monster1.png")
imgInimigo = pygame.transform.scale(imgInimigo, (50, 50))
rectInimigo = imgInimigo.get_rect()

imgInimigo2 = pygame.image.load("Pictures/monster2.png")
imgInimigo2 = pygame.transform.scale(imgInimigo2, (50, 50))
rectInimigo2 = imgInimigo2.get_rect()

imgInimigo3 = pygame.image.load("Pictures/monster3.png")
imgInimigo3 = pygame.transform.scale(imgInimigo3, (50, 50))
rectInimigo3 = imgInimigo3.get_rect()

pygame.mixer.music.load("Soundtrack/track.mp3")
pygame.mixer.music.play(loops = -1)
pygame.mixer.music.set_volume(0.2)

sfxShoot = pygame.mixer.Sound("Soundtrack/shoot.wav")
sfxShoot.set_volume(1.0)

velNave = 7
velInimigo = 3
velInimigo2 = 5
VelInimigo2 = 8
velLaser = 20
pontuacao = 0
vida = 100
lose = 0
disparos = [] 
inimigos = [] 

# Carregando inimigos
quantidade = 100

for i in range (quantidade):
    rectInimigo = imgInimigo.get_rect()

    # Posicionando inimigos
    while True:
        novoX = random.randint(500,4000)
        novoY = random.randint(100,500)
        rectInimigo.x = novoX
        rectInimigo.y = novoY
        if rectInimigo.collidelist(inimigos):
            break
    inimigos.append(rectInimigo)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sfxShoot.play(loops=0, maxtime=0)
                rectLaser.x = rectNave.x + 100
                rectLaser.y = rectNave.y
                disparos.append(rectLaser)
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_d]:
        rectNave.move_ip(velNave, 0)
    if tecla[pygame.K_a]:
        rectNave.move_ip(-velNave, 0)
    if tecla[pygame.K_w]:
        rectNave.move_ip(0, -velNave)
    if tecla[pygame.K_s]:
        rectNave.move_ip(0, velNave)

    # Movimentação disparo
    for disparo in disparos:
        disparo.move_ip (velLaser,0)
        if disparo.left > tela.get_width():
            disparos.remove(disparo)

    # Movimentação inimigo
    for inimigo in inimigos:
        inimigo.move_ip(-velInimigo,0)
        if inimigo.right < 0:
            inimigos.remove(inimigo)
            vida -= 2
            lose += 1
            if vida < 0:
                vida = 0

    # Controle de colisão 
    for inimigo in inimigos:
        i = inimigo.collidelist(disparos)
        if i != -1:
            disparos.pop(i)
            inimigos.remove(inimigo)
            pontuacao += 1

    tela.blit(background, (0,0))   
    tela.blit(imgNave, rectNave)
    for disparo in disparos:
        tela.blit(imgLaser, disparo)

    for inimigo in inimigos:
            tela.blit(imgInimigo, inimigo)  
        
    show = fonte.render ("        Score : "+ str(pontuacao) + "     Health :  " + str(vida)+ "     Losses : "+str(lose), True, (255, 255, 255))
    tela.blit(show, (10,5))

    pygame.display.update()
    clock.tick(30)



