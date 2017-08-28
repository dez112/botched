from django.db import models
from django.urls import reverse

#TODO dodac model dla technokracji
class Chronicle(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Base(models.Model):
    NATURE_CHOICES = [
        (1, "Activist"),
        (2, "Benefactor"),
        (3, "Contrary"),
        (4, "Crusader"),
        (5, "Hacker"),
        (6, "Idealist"),
        (7, "Innovator"),
        (8, "Kid"),
        (9, "Loner"),
        (11, "Machine"),
        (12, "Mad Scientist"),
        (13, "Martyr"),
        (14, "Monster"),
        (15, "Prophet"),
        (16, "Rogue"),
        (17, "Sensualist"),
        (18, "Survivor"),
        (19, "Traditionalist"),
        (20, "Trickster"),
        (21, "Visionary")
    ]

    ESSENCE_CHOICES = [
        (1, "Dynamic"),
        (2, "Static"),
        (3, "Primordial"),
        (4, "Questing"),
        (5, "Brak")
    ]

    player = models.CharField(max_length=200)
    chname = models.ForeignKey('Chronicle')
    name = models.CharField(max_length=200)
    nature = models.IntegerField(choices=NATURE_CHOICES)
    demenor = models.IntegerField(choices=NATURE_CHOICES)
    essence = models.IntegerField(choices=ESSENCE_CHOICES)
    willpower = models.PositiveIntegerField() #TODO dodac walidator 1-10
    traits = models.TextField(null=True, default="Empty")
    backgrounds = models.TextField(null=True)
    is_technocrat = models.BooleanField(default=False)
    is_mage = models.BooleanField(default=False)
    is_independent_mage = models.BooleanField(default=False)
    is_enemy = models.BooleanField()
    is_player_character = models.BooleanField(default=False)
    # picture = ImageField(upload_to=/media/photos/, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('schoolsubject-edit', kwargs={'pk': self.id})
        return reverse('base-list')


class Attributes(models.Model):
    name = models.ForeignKey('Base')
    strength = models.IntegerField(null=True)
    dexterity = models.IntegerField(null=True)
    stamina = models.IntegerField(null=True)
    charisma = models.IntegerField(null=True)
    manipulation = models.IntegerField(null=True)
    apperance = models.IntegerField(null=True)
    perception = models.IntegerField(null=True)
    intelligencee = models.IntegerField(null=True)
    wits = models.IntegerField(null=True)


class Abilities(models.Model):
    name = models.ForeignKey('Base')
    alertness = models.IntegerField(null=True)
    art = models.IntegerField(null=True)
    athletics = models.IntegerField(null=True)
    awareness = models.IntegerField(null=True)
    brawl = models.IntegerField(null=True)
    empathy = models.IntegerField(null=True)
    expression = models.IntegerField(null=True)
    intimidation = models.IntegerField(null=True)
    leadership = models.IntegerField(null=True)
    streetwise = models.IntegerField(null=True)
    subterfuge = models.IntegerField(null=True)
    crafts = models.IntegerField(null=True)
    drive = models.IntegerField(null=True)
    etiquette = models.IntegerField(null=True)
    firearms = models.IntegerField(null=True)
    martial_arts = models.IntegerField(null=True)
    meditation = models.IntegerField(null=True)
    melee = models.IntegerField(null=True)
    research = models.IntegerField(null=True)
    stealth = models.IntegerField(null=True)
    survival = models.IntegerField(null=True)
    technology = models.IntegerField(null=True)
    academics = models.IntegerField(null=True)
    computer = models.IntegerField(null=True)
    cosmology = models.IntegerField(null=True)
    enigmas = models.IntegerField(null=True)
    esoterica = models.IntegerField(null=True)
    investigation = models.IntegerField(null=True)
    law = models.IntegerField(null=True)
    medicine = models.IntegerField(null=True)
    occult = models.IntegerField(null=True)
    politics = models.IntegerField(null=True)
    science = models.IntegerField(null=True)

class Spheres(models.Model):
    AFFINITY_SPHERE = ((1, "Correspondence"), (2, "Entropy"), (3, "Forces"), (4, "Life"),
                      (5, "Matter"), (6, "Mind"), (7, "Prime"), (8, "Spirit"), (9, "Time"))
    name = models.ForeignKey('Base')
    correspondence = models.IntegerField(null=True)
    entropy = models.IntegerField(null=True)
    forces = models.IntegerField(null=True)
    life = models.IntegerField(null=True)
    matter = models.IntegerField(null=True)
    mind = models.IntegerField(null=True)
    prime = models.IntegerField(null=True)
    spirit = models.IntegerField(null=True)
    time = models.IntegerField(null=True)
    affinity_sphere = models.IntegerField(choices=AFFINITY_SPHERE, null=True)



