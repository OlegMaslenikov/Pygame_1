import pygame


class Sounds:
        def __init__(self):
                """Left Side sounds"""
                self.a_spawn_1_1 = pygame.mixer.Sound("sounds/voices/alliance/spawn_1_1.ogg")
                self.a_spawn_1_2 = pygame.mixer.Sound("sounds/voices/alliance/spawn_1_2.ogg")
                self.a_spawn_1_3 = pygame.mixer.Sound("sounds/voices/alliance/spawn_1_3.ogg")
                self.a_spawn_1 = [self.a_spawn_1_1, self.a_spawn_1_2, self.a_spawn_1_3]
                self.a_death_1_1 = pygame.mixer.Sound("sounds/voices/alliance/death_1_1.ogg")
                self.a_death_1_2 = pygame.mixer.Sound("sounds/voices/alliance/death_1_2.ogg")
                self.a_death_1_3 = pygame.mixer.Sound("sounds/voices/alliance/death_1_3.ogg")
                self.a_death_1 = [self.a_death_1_1, self.a_death_1_2, self.a_death_1_3]
                self.a_spawn_2_1 = pygame.mixer.Sound("sounds/voices/alliance/spawn_2_1.ogg")
                self.a_spawn_2_2 = pygame.mixer.Sound("sounds/voices/alliance/spawn_2_2.ogg")
                self.a_spawn_2_3 = pygame.mixer.Sound("sounds/voices/alliance/spawn_2_3.ogg")
                self.a_spawn_2 = [self.a_spawn_2_1, self.a_spawn_2_2, self.a_spawn_2_3]
                self.a_death_2_1 = pygame.mixer.Sound("sounds/voices/alliance/death_2_1.ogg")
                self.a_death_2_2 = pygame.mixer.Sound("sounds/voices/alliance/death_2_2.ogg")
                self.a_death_2_3 = pygame.mixer.Sound("sounds/voices/alliance/death_2_3.ogg")
                self.a_death_2 = [self.a_death_2_1, self.a_death_2_2, self.a_death_2_3]
                self.a_archer_shoot = pygame.mixer.Sound("sounds/effects/archer_shot.ogg")
                """Right side sounds"""
                self.u_spawn_1_1 = pygame.mixer.Sound("sounds/voices/undead/spawn_1_1.ogg")
                self.u_spawn_1_2 = pygame.mixer.Sound("sounds/voices/undead/spawn_1_2.ogg")
                self.u_spawn_1_3 = pygame.mixer.Sound("sounds/voices/undead/spawn_1_3.ogg")
                self.u_spawn_1 = [self.u_spawn_1_1, self.u_spawn_1_2, self.u_spawn_1_3]
                self.u_death_1_1 = pygame.mixer.Sound("sounds/voices/undead/death_1_1.ogg")
                self.u_death_1_2 = pygame.mixer.Sound("sounds/voices/undead/death_1_2.ogg")
                self.u_death_1 = [self.u_death_1_1, self.u_death_1_2]
                self.u_spawn_2_1 = pygame.mixer.Sound("sounds/voices/undead/spawn_2_1.ogg")
                self.u_spawn_2_2 = pygame.mixer.Sound("sounds/voices/undead/spawn_2_2.ogg")
                self.u_spawn_2_3 = pygame.mixer.Sound("sounds/voices/undead/spawn_2_3.ogg")
                self.u_spawn_2 = [self.u_spawn_2_1, self.u_spawn_2_2, self.u_spawn_2_3]
                self.u_death_2_1 = pygame.mixer.Sound("sounds/voices/undead/death_2_1.ogg")
                self.u_death_2_2 = pygame.mixer.Sound("sounds/voices/undead/death_2_2.ogg")
                self.u_death_2_3 = pygame.mixer.Sound("sounds/voices/undead/death_2_3.ogg")
                self.u_death_2 = [self.u_death_2_1, self.u_death_2_2, self.u_death_2_3]
                self.u_mage_shoot = pygame.mixer.Sound("sounds/effects/mage_1.ogg")
                self.u_mage_shoot_2 = pygame.mixer.Sound("sounds/effects/mage_2.ogg")
                """General sounds"""
                self.damage_base_1 = pygame.mixer.Sound("sounds/effects/base_1.ogg")
                self.damage_base_2 = pygame.mixer.Sound("sounds/effects/base_2.ogg")
                self.damage_damage_receive = pygame.mixer.Sound("sounds/effects/damage_receive.ogg")
                self.damage_melee_1 = pygame.mixer.Sound("sounds/effects/melee_1.ogg")
                self.damage_melee_2 = pygame.mixer.Sound("sounds/effects/melee_2.ogg")
                self.damage_melee_3 = pygame.mixer.Sound("sounds/effects/melee_3.ogg")
                self.damage_melee_4 = pygame.mixer.Sound("sounds/effects/melee_4.ogg")
                self.damage_melee_5 = pygame.mixer.Sound("sounds/effects/melee_5.ogg")
                self.damage_melee_6 = pygame.mixer.Sound("sounds/effects/melee_6.ogg")
                self.damage = [self.damage_melee_1, self.damage_melee_2, self.damage_melee_3,
                               self.damage_melee_4,self.damage_melee_5,self.damage_melee_6]
