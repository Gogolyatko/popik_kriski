from pygame import *
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption(("Maze"))
background = transform.scale(image.load("Без названия (1).jfif"), (win_width, win_height))

game = True
clock = time.Clock()
FPS = 60
# mixer.init()
# mixer.music.load("")
# mixer.music.play()

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))
# money = mixer.Sound()
# kick = mixer.Sound()
finish = False
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.rect = self.image.get_rect()
        self.speed = player_speed
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 3:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 70:
            self.rect.x += self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 70:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y > 3:
            self.rect.y -= self.speed
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wal_heidht):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.wall_wigth = wall_width
        self.wall_height = wal_heidht
        self.image = Surface((self.wall_wigth, self.wall_height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
w1 = Wall(154, 205, 50, 100, 20, 450, 10)
player = Player("миша.png", 5, win_height - 80, 4)
monster = Enemy("АСААА.png", win_width - 80, 280, 3)
goal = GameSprite("МНЁЁД.png", 400, 420, 0)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0,0))

    if finish != True:
        window.blit(background, (0,0))
        player.update()
        monster.update()
        player.reset()
        monster.reset()
        goal.reset()
        w1.draw_wall()

        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1):
            # kick.play()
            window.blit(lose, (200, 200))
        if sprite.collide_rect(player, goal):
            # money.play()
            window.blit(win, (200,200))
    else:
        time.delay(3000)
        finish = False
        player = Player("миша.png", 5, win_height - 80, 4)

    display.update()
    clock.tick(FPS)