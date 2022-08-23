import pygame
import neat
import time
import os
import random

import visualize #dans visualize.py!
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

import pickle #pour les gros fichier, cpickle sera plus rapide





pygame.font.init()

WIN_WIDTH = 500
WIN_HEIGHT = 800

#on double la taille des images
BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird1.png"))),
            pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird2.png"))),
            pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bg.png")))

STAT_FONT = pygame.font.SysFont("comicsans",50)

GEN = 0#pas nécessaire de le mettre en global, c'est pour gagner du temps

class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0 #garde la trace de la durée depuis le dernier saut
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        """Appellé à chaque fois que l'on ordonne à l'oiseau de battre les ailes"""
        self.vel = -10.5 #rappel : le coin en haut à gauche est 0.0 -> pour monter, il faut de un vecteur y négatif
        self.tick_count = 0
        self.height = self.y
    
    def move(self):
        """Appellé à chaque frame pour bouger l'oiseau"""
        self.tick_count += 1

        #calcul du déplacement. Le calcul se fait à partir de l'emplacement/du moment du dernier saut
        d = self.vel*self.tick_count + 1.5 * self.tick_count**2 #NB : pour une MRUA classique, on  aurait v*t + 0.5*a*t² => ici on suppose que a = 3
        #On limite le déplacement
        if d >= 16: #distance de chute max ??
            d = 16
        elif d < 0: #hauteur de saut max
            d -= 2
        self.y = self.y + d

        #détermination de l'inclinaison de l'oiseau
        if d < 0 or self.y < self.height + 50: #si on monte, ou si on commence à peine à redescendre, on tilte vers le haut
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else: #on oriente vers le bas l'oiseu
            if self.tilt > -90: #si l'oiseau ne regarde pas directement vers le bas
                self.tilt -= self.ROT_VEL

    def draw(self, win): #win = fenêtre
        self.img_count += 1

        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME*4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME*4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        if self.tilt <= -80: #si on chute, pas de flap
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2 #comme ça on reprend à la bonne position quand on rebattra des ailes

        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft) #nécessaire pour que la rotation n'affecte pas la position ?

    def get_mask(self): #pour la détection de colisions
        return pygame.mask.from_surface(self.img)

class Pipe:
    GAP = 200
    VEL = 5

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.gap = 100

        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True)
        self.PIPE_BOTTOM = PIPE_IMG

        self.passed = False
        self.set_height()

    def set_height(self):
        self.height = random.randrange(50,450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.VEL
    
    def draw(self,win):
        win.blit(self.PIPE_TOP,(self.x,self.top))
        win.blit(self.PIPE_BOTTOM,(self.x,self.bottom))

    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x - bird.x, self.top - round(bird.y)) #row pour ne pas avoir de négatif ? pourquoi pas abs ?
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask,bottom_offset) #point de collision ?
        t_point = bird_mask.overlap(top_mask,top_offset)

        if t_point or b_point:
            return True
        else:
            return False

class Base:
    VEL = 5
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH
    
    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH
        
        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))

def draw_window(win, birds, pipes, base, score, gen):
    win.blit(BG_IMG, (0,0))
    for pipe in pipes:
        pipe.draw(win)

    text = STAT_FONT.render("Score: "+ str(score),1,(255,255,255))
    win.blit(text,(WIN_WIDTH -10 - text.get_width(),10))

    text = STAT_FONT.render("gen: "+ str(gen),1,(255,255,255))
    win.blit(text,(10,10))

    base.draw(win)

    for bird in birds:
        bird.draw(win)
    pygame.display.update()

def main(genomes, config): #eval_geomes())
    global GEN
    GEN += 1

    nets = []
    ge = []
    birds = []

    for _, g in genomes: #création d'objet décision dont le cerveau est l'oiseau.
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird(230,350))
        g.fitness = 0
        ge.append(g)

    base = Base(730)
    pipes = [Pipe(700)]

    win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
    clock = pygame.time.Clock()

    score = 0 #débute avec la case de départ

    run = True
    while run:
        clock.tick(240)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        
        #on sélectionne le pipe à considérer pour la prise de décision (le premier devant l'oiseau)
        pipe_ind = 0
        if len(birds) > 0:
            if len(pipes)>1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_ind = 1
        else:
            #quit la génération
            run = False
            break

        for x, bird in enumerate(birds):
            bird.move()
            ge[x].fitness += 0.1 #pour encourager l'oiseau à continuer à avancer

            output = nets[x].activate((bird.y, abs(bird.y - pipes[pipe_ind].height),abs(bird.y - pipes[pipe_ind].bottom)))

            if output[0] > 0.5: #output est une liste, même si on n'a qu'une sortie voulue
                bird.jump()

        rem = []
        add_pipe = False
        for pipe in pipes:
            for x, bird in enumerate(birds):
                if pipe.collide(bird):
                    ge[x].fitness -= 1
                    birds.pop(x)
                    nets.pop(x)
                    ge.pop(x)

                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True

            if pipe.x + pipe.PIPE_TOP.get_width() < 0: #si les tuyaux sortent de l'écran
                rem.append(pipe)
            
            pipe.move()

        if add_pipe:
            score += 1
            for g in ge:
                g.fitness += 5
            pipes.append(Pipe(600))

        for r in rem:
            pipes.remove(r)

        #si l'oiseau touche le sol ou sort de l'écran par le haut
        for x, bird in enumerate(birds):
            if bird.y + bird.img.get_height() >= 730 or bird.y < 0:
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)

        if score > 50:
            break # pour ne pas continuer indéfiniment (possible aussi dans la config du neat je crois)

        base.move()
        draw_window(win, birds, pipes, base,score,GEN)

def run(config_path):
    config = neat.config.Config(neat.DefaultGenome,
                                neat.DefaultReproduction,
                                neat.DefaultSpeciesSet,
                                neat.DefaultStagnation,
                                config_path)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main,50) #le genome gagnant peut être sauvegarder dans un fichier avec le module pickler, et rechargé ailleurs (pas serializable avec json)

    filename = "winner"
    outfile = open(filename,'wb')
    pickle.dump(winner,outfile)
    outfile.close()

    visualize.draw_net(config, winner, True)
    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__) #chemin du dossier dans lequel on se trouve
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)
