from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Seller_Lot(models.Model):
    id = models.AutoField(primary_key=True)
    name_seller = models.CharField(max_length=50, db_index=True)
    lot = models.ForeignKey('Lots', on_delete=models.CASCADE)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    id_lot = models.IntegerField(null=True)
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name


class Coments(models.Model):
    id = models.AutoField(primary_key=True)
    text_Coment = models.TextField("Coment")
    coment_by = models.ForeignKey('User', on_delete=models.CASCADE, default=None, null=True)





class Lots(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField("Name lot", max_length=50)
    text_lot = models.TextField("Information for lot")
    main_image = models.ImageField(null=True, blank=True, upload_to=f"Photo/")
    image1 = models.ImageField(null=True, blank=True, upload_to=f"Photo/")
    image2 = models.ImageField(null=True, blank=True, upload_to=f"Photo/")
    image3 = models.ImageField(null=True, blank=True, upload_to=f"Photo/")
    image4 = models.ImageField(null=True, blank=True, upload_to=f"Photo/")
    image5 = models.ImageField(null=True, blank=True, upload_to=f"Photo/")
    image6 = models.ImageField(null=True, blank=True, upload_to=f"Photo/")
    image7 = models.ImageField(null=True, blank=True, upload_to=f"Photo/")

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name_buyer_lot = models.ForeignKey('User', on_delete=models.PROTECT, default=None, null=True)
    cost_initial = models.DecimalField(max_digits=10, decimal_places=2)
    cost_lot = models.DecimalField(max_digits=10, decimal_places=2)
    time_create = models.DateTimeField(auto_now_add=True)
    close_lot_date = models.DateField(null=True, default=None)
    close_lot_time = models.TimeField(null=True, default=None)
    lot_close = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Lot"
        verbose_name_plural = "Lots"


