from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name.title()


class Card(models.Model):
    question = models.CharField(max_length=170)
    answer = models.TextField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.question if self.question[-1] == "?" else self.question + "?"
