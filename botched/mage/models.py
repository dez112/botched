from django.db import models
from django.urls import reverse

ESSENCE_CHOICES = [
    (1, "Dynamic"),
    (2, "Static"),
    (3, "Primordial"),
    (4, "Questing"),
    (5, "None")
]


class Chronicle(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chronicle-list')
        # return reverse('base-list')


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

    player = models.CharField(max_length=200, blank=True, null=True)
    chname = models.ForeignKey('Chronicle', verbose_name="Chronicle name", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    nature = models.IntegerField(choices=NATURE_CHOICES, blank=True)
    demenor = models.IntegerField(choices=NATURE_CHOICES, blank=True)
    willpower = models.PositiveIntegerField(null=True, blank=True)
    traits = models.TextField(null=True, default="Empty", blank=True)
    backgrounds = models.TextField(null=True, default="Empty", blank=True)
    is_technocrat = models.BooleanField(default=False, blank=True)
    is_mage = models.BooleanField(default=False, blank=True)
    #is_independent_mage = models.BooleanField(default=False, blank=True)
    is_enemy = models.BooleanField(blank=True)
    is_player_character = models.BooleanField(default=False, blank=True)
    picture = models.URLField(max_length=1000, default='http://www.petakids.com/wp-content/uploads/2015/11/Cute-Red-Bunny.jpg')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('base-detail-view', kwargs={'pk': self.id})
        #return reverse('base-list')
    

class Attributes(models.Model):
    name = models.OneToOneField('Base', on_delete=models.CASCADE)
    strength = models.IntegerField(null=True, blank=True, default=1)
    dexterity = models.IntegerField(null=True, blank=True, default=1)
    stamina = models.IntegerField(null=True, blank=True, default=1)
    charisma = models.IntegerField(null=True, blank=True, default=1)
    manipulation = models.IntegerField(null=True, blank=True, default=1)
    apperance = models.IntegerField(null=True, blank=True, verbose_name="appearance", default=1)
    perception = models.IntegerField(null=True, blank=True, default=1)
    intelligencee = models.IntegerField(null=True, blank=True, verbose_name="intelligence", default=1)
    wits = models.IntegerField(null=True, blank=True, default=1)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.name)
    
    def get_absolute_url(self):
        return reverse('base-detail-view', kwargs={'pk': self.name.id})


class Abilities(models.Model):
    name = models.OneToOneField('Base', on_delete=models.CASCADE)
    alertness = models.IntegerField(null=True, blank=True)
    art = models.IntegerField(null=True, blank=True)
    athletics = models.IntegerField(null=True, blank=True)
    awareness = models.IntegerField(null=True, blank=True)
    brawl = models.IntegerField(null=True, blank=True)
    empathy = models.IntegerField(null=True, blank=True)
    expression = models.IntegerField(null=True, blank=True)
    intimidation = models.IntegerField(null=True, blank=True)
    leadership = models.IntegerField(null=True, blank=True)
    streetwise = models.IntegerField(null=True, blank=True)
    subterfuge = models.IntegerField(null=True, blank=True)
    crafts = models.IntegerField(null=True, blank=True)
    secondary_talents = models.CharField(max_length=300, null=True, blank=True)
    drive = models.IntegerField(null=True, blank=True)
    etiquette = models.IntegerField(null=True, blank=True)
    firearms = models.IntegerField(null=True, blank=True)
    martial_arts = models.IntegerField(null=True, blank=True)
    meditation = models.IntegerField(null=True, blank=True)
    melee = models.IntegerField(null=True, blank=True)
    research = models.IntegerField(null=True, blank=True)
    stealth = models.IntegerField(null=True, blank=True)
    survival = models.IntegerField(null=True, blank=True)
    technology = models.IntegerField(null=True, blank=True)
    secondary_skills = models.CharField(max_length=300, null=True, blank=True)
    academics = models.IntegerField(null=True, blank=True)
    computer = models.IntegerField(null=True, blank=True)
    cosmology = models.IntegerField(null=True, blank=True)
    enigmas = models.IntegerField(null=True, blank=True)
    esoterica = models.IntegerField(null=True, blank=True)
    investigation = models.IntegerField(null=True, blank=True)
    law = models.IntegerField(null=True, blank=True)
    medicine = models.IntegerField(null=True, blank=True)
    occult = models.IntegerField(null=True, blank=True)
    politics = models.IntegerField(null=True, blank=True)
    science = models.IntegerField(null=True, blank=True)
    secondary_knowledges = models.CharField(max_length=300, null=True, blank=True)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.name)
    
    def get_absolute_url(self):
        return reverse('base-detail-view', kwargs={'pk': self.name.id})

    
class Spheres(models.Model):
    AFFINITY_SPHERE = [(1, "Correspondence"), (2, "Entropy"), (3, "Forces"), (4, "Life"),
                      (5, "Matter"), (6, "Mind"), (7, "Prime"), (8, "Spirit"), (9, "Time")]
    name = models.OneToOneField('Base', on_delete=models.CASCADE)
    tradition = models.CharField(max_length=200, null=True, blank=True)
    avatar = models.PositiveIntegerField(null=True, blank=True)
    essence = models.IntegerField(choices=ESSENCE_CHOICES, blank=True)
    correspondence = models.IntegerField(null=True, blank=True)
    entropy = models.IntegerField(null=True, blank=True)
    forces = models.IntegerField(null=True, blank=True)
    life = models.IntegerField(null=True, blank=True)
    matter = models.IntegerField(null=True, blank=True)
    mind = models.IntegerField(null=True, blank=True)
    prime = models.IntegerField(null=True, blank=True)
    spirit = models.IntegerField(null=True, blank=True)
    time = models.IntegerField(null=True, blank=True)
    affinity_sphere = models.IntegerField(choices=AFFINITY_SPHERE, null=True, blank=True)
    date_sent = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)
    
    def get_absolute_url(self):
        return reverse('base-detail-view', kwargs={'pk': self.name.id})

    def get_success_url(self):
        return reverse('base-detail-view', kwargs={'pk': self.name.id})


class TechnocracySpheres(models.Model):
    AFFINITY_SPHERE = [(1, "Data"), (2, "Dimensional Science"), (3, "Entropy"), (4, "Forces"), (5, "Life"),
                       (6, "Matter"), (7, "Mind"), (8, "Primal Utility"), (9, "Time")]
    name = models.OneToOneField('Base', on_delete=models.CASCADE)
    Union = models.CharField(max_length=200, null=True, blank=True)
    avatar = models.PositiveIntegerField(null=True, blank=True)
    essence = models.IntegerField(choices=ESSENCE_CHOICES, blank=True)
    data = models.IntegerField(null=True, blank=True)
    dimensional_science = models.IntegerField(null=True, verbose_name="dimensional science", blank=True)
    entropy = models.IntegerField(null=True, blank=True)
    forces = models.IntegerField(null=True, blank=True)
    life = models.IntegerField(null=True, blank=True)
    matter = models.IntegerField(null=True, blank=True)
    mind = models.IntegerField(null=True, blank=True)
    primal_utility = models.IntegerField(null=True, verbose_name="primal utility", blank=True)
    time = models.IntegerField(null=True, blank=True)
    affinity_sphere = models.IntegerField(choices=AFFINITY_SPHERE, null=True, blank=True)
    date_sent = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return "{}".format(self.name)
    
    def get_absolute_url(self):
        return reverse('base-detail-view', kwargs={'pk': self.name.id})



