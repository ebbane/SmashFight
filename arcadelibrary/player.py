import arcade

class Player(arcade.Sprite):
    def _init_(self):
        super().__init__()
        self.curtime = 0
        self.delay = 0
        self.growl = False
        self.fireball_list = None
        self.health = 100
        self.death_animation = 0

    def shoot(self):
        if self.player.alive:
            arcade.play_sound(self.sound_list[4])

            fireball = Fireball("images/players/shoot.jpg")
            fireball.center_x = self.center_x
            fireball.center_y = self.center_y
            fireball.reflected = False

            

            self.fireball_list.append(fireball)

    def update(self):
        self.curtime += 1

        # If enemy dies play death animation
        if self.health <= 0 and self.death_animation == 0:
            self.death_animation = self.curtime + 30
        if self.death_animation - 20 > self.curtime:
            self.set_texture(1)
        elif self.death_animation - 10 > self.curtime:
            self.set_texture(2)
        elif self.death_animation > self.curtime:
            # Spawn a coin on death
            coin = arcade.Sprite("images/coin.png", 0.1)
            coin.center_x = self.center_x
            coin.center_y = self.center_y
            coin.force = 0
            self.coin_list.append(coin)
            self.kill()


        # If player is nearby shoot at him every 100-200 frames
        d = math.sqrt(((self.center_x - self.player.center_x) ** 2) + ((self.center_y - self.player.center_y) ** 2))
        if d < 150 and self.health > 0:
            if not self.growl:
                self.growl = True
                arcade.play_sound(self.sound_list[5])

            x_diff = self.player.center_x - self.center_x
            y_diff = self.player.center_y - self.center_y
            self.angle = math.degrees(math.atan2(y_diff, x_diff)) - 90

            if self.curtime > self.delay:
                self.delay = self.curtime + random.randint(100, 200)
                self.shoot()
        else:
            # Prevent detection noise from playing every frame
            self.growl = False
