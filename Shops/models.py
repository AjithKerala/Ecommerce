from django.db import models

# Create your models here.


class category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name


class Productts(models.Model):
    category = models.ForeignKey(category, related_name='Products', on_delete=models.CASCADE)
    photos = models.ImageField(upload_to='product')
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
    def get_price(self):
        return self.price/100