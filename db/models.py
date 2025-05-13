from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255)  #unique char field with the maximum length of 255 characters Elf, Dwarf, Human, or Ork
    description = models.TextField(blank=True, null=True)  # text field, can be blank


class Skill(models.Model):
    name = models.CharField(
        unique=True, max_length=255
    )
    bonus = models.CharField(
        max_length=255
    )
    race = models.ForeignKey(
        Race, related_name="skills", on_delete=models.CASCADE
    )

class Guild(models.Model):
    name = models.CharField(
        unique=True, max_length=255
    )  # unique char field with the maximum length of 255 characters
    description = models.TextField(null=True, blank=True)  # text field, can be null


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=False)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race, related_name="race_players", on_delete=models.CASCADE
    )  # foreign key that points to the Race model and shows the race of the player. Important Note: The player must be deleted when the race is deleted.
    guild = models.ForeignKey(
        Guild, related_name="guild_players", on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
