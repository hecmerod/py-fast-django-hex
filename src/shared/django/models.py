from django.db import models


class ConcertModel(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    starts_at = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "concerts"
        ordering = ["starts_at"]

    def __str__(self) -> str:
        return f"{self.name} - {self.artist}"
