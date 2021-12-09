from pygame.key import get_pressed
<<<<<<< HEAD
from pygame.constants import K_LEFT, K_RIGHT, K_SPACE
from pygame.sprite import Group

from models import Entity, Bullet

HEIGHT = 640
WIDTH = 480
=======
from pygame.constants import K_LEFT, K_RIGHT, K_SPACE, K_UP, K_DOWN
from pygame.sprite import Group

from models import Entity, Bullet, HEIGHT, WIDTH

HEIGHT = HEIGHT
WIDTH = WIDTH
>>>>>>> 7de83ecefb57547b9e44c2e11a6d87651059fb1d


class Player(Entity):
    COOLDOWN = 20

    def __init__(self, health_point, score):
<<<<<<< HEAD
        super(Player, self).__init__('users')
=======
        super().__init__('users')
>>>>>>> 7de83ecefb57547b9e44c2e11a6d87651059fb1d
        self.weapon = None
        self.weapons = Group()
        self.cool_down_counter = 0
        self.health_point = health_point
        self.score = score

    def move(self) -> None:
        key = get_pressed()

        if key[K_LEFT]:
            self.rect.x -= self.speed

        if key[K_RIGHT]:
            self.rect.x += self.speed

        if key[K_SPACE]:
            self.attack()
<<<<<<< HEAD
        super(Player, self).move()
=======

        super().move()
>>>>>>> 7de83ecefb57547b9e44c2e11a6d87651059fb1d
        for weapon in self.weapons:
            weapon.move()

    def attack(self) -> None:
        if self.cool_down_counter > self.COOLDOWN:
            self.weapons.add(self.weapon(self.rect.x, self.rect.y))
            self.cool_down_counter = 0

    def update(self, *args, **kwargs) -> None:
        self.cool_down_counter += 1
<<<<<<< HEAD
        super(Player, self).update()
        self.weapons.update()

    def set_images(self, image_path) -> None:
        super(Player, self).set_images(image_path)
=======
        super().update()
        self.weapons.update()

    def set_images(self, image_path) -> None:
        super().set_images(image_path)
>>>>>>> 7de83ecefb57547b9e44c2e11a6d87651059fb1d
        self.pos_y = HEIGHT - self.image.get_height() - 30
        self.pos_x = (WIDTH - self.image.get_width()) / 2
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y


class PlayerBullet(Bullet):
    def __init__(self, pos_x, pos_y):
<<<<<<< HEAD
        super(PlayerBullet, self).__init__(pos_x, pos_y)
=======
        super().__init__(pos_x, pos_y)
>>>>>>> 7de83ecefb57547b9e44c2e11a6d87651059fb1d
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move(self) -> None:
        self.rect.y -= self.speed
