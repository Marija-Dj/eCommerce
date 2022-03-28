from audioop import reverse
from django.db import models
from django.urls import reverse


SIZES= (
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL')
)

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('product:category_list', args=[self.slug])
    

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    catrgory=models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    size=models.CharField(max_length=2, choices=SIZES, default=SIZES[0][0])
    number = models.IntegerField()
    slug = models.SlugField(max_length=255)

    class Meta:
           verbose_name_plural = 'Products' 
           ordering = ('-price',)
           

    def get_absolute_url(self):
        return reverse('product:detail_product', args=[self.slug])
    
    def __str__(self):
        return f"{self.id} : {self.title}"

