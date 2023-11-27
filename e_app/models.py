from django.db import models
from django.contrib.auth.models import User

# Create your models here.



CATEGORY_CHOICES=(
    ('CR','Curd'),
    ('ML','Milk'),
    ('LS','Lassi'),
    ('MS','Milkshake'),
    ('PN','Paneer'),
    ('GH','Ghee'),
    ('CZ','Cheese'),
    ('IC','Ice-Creams'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title
    


STATE_CHOICES=(
    ("DL","Delhi"),
    ("UP","Uttar Pradesh"),
    ("WB", "West Bengal"),
    ("MH", "Maharashtra"),
    ("RJ", "Rajasthan"),
    ("MP", "Madhya Pradesh"),
    ("TN", "Tamil Nadu"),
    ("AP", "Andhra Pradesh"),
    ("KA", "Karnataka"),
    ("OR", "Orissa"),
    ("GJ", "Gujarat"),
    ("HR", "Haryana"),
    ("PB", "Punjab"),
    ("JH", "Jharkhand"),
    ("HP", "Himachal Pradesh"),
    ("UT", "Uttarakhand"),
    ("UK", "Uttrakhand"),
    ("AN", "Andaman and Nicobar Islands"),
    ("CH", "Chandigarh"),
    ("DN", "Dadra and Nagar Haveli"),
    ("DD", "Daman and Diu"),
    ("LD", "Lakshadweep"),
    ("PY", "Pondicherry"),
    ("SK", "Sikkim"),
    ("JK", "Jammu and Kashmir"),
    ("TG", "Telangana"),
    ("TR", "Tripura"),
    ("MN", "Manipur"),
    ("NL", "Nagaland"),
    ("ML", "Meghalaya"),
)
    
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name