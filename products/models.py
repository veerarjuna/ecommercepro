from django.db import models

# Create your models here.
CATEGORY = (('Electronics', 'EL'),
            ('Clothing', 'CL'),
            ('Groceries', 'GR'),
            ('Accesories', 'AC'),
            ('Food and Beverages', 'FB')
            )

RETURN_POLICY = (('Yes', 'Y'),
                 ('No', 'N')
                 )

class Stores(models.Model):

    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_no = models.BigIntegerField()
    landmark = models.CharField(max_length=200)
    email = models.EmailField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return "-".join([self.name, self.location])


class Products(models.Model):
    store_id = models.ForeignKey(Stores, related_name='store_prod', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY, default='EL')
    exp_date = models.DateField()
    reviews = models.CharField(max_length=255)
    ratings = models.CharField(max_length=10)
    return_policy = models.CharField(max_length=5, choices=RETURN_POLICY, default='Y')

    def __str__(self):
        return '-'.join([self.store_id.name, self.store_id.location])
