import pygame

pygame.init()
x = 400
y = 300
pos_X = 200
pos_Y = 300
velocidade_objeto1 = 10
velocidade_Npc = 13

tela_fundo1 = pygame.image.load('game/estrada_estagio_1.png')
carro = pygame.image.load('game/carropreto.png')
carro_npc = pygame.image.load('game/carropreto.png')
carro_npc_2 = pygame.image.load('game/carronpc3.png')


janela = pygame.display.set_mode((800,600))
#nome da janela abaixo

pygame.display.set_caption("Carrinhos do Emo")

janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)
#mostrar eventos

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
            
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y-= velocidade_objeto1
    if comandos[pygame.K_DOWN]:
        y+= velocidade_objeto1
    if comandos[pygame.K_RIGHT]:
        x+= velocidade_objeto1
    if comandos[pygame.K_LEFT]:
        x-= velocidade_objeto1 
    pos_Y -= velocidade_Npc
    if (pos_Y <= -600):
        pos_Y = 600
           
    janela.blit(tela_fundo1, (0,0))   
    janela.blit(carro, (x,y))
    janela.blit(carro_npc, (pos_X,pos_Y))
    janela.blit(carro_npc_2,(pos_X - 300,pos_Y))
 
                    
    pygame.display.update ()  
pygame.quit