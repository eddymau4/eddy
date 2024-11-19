from django.db import models

# Create your models here.
class MenuType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
class Menu(models.Model):
    menu_type = models.ForeignKey(MenuType, on_delete=models.CASCADE, related_name='menus')
    menu_title = models.CharField(max_length=100)
    image =models.ImageField(upload_to = 'image/menu/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.menu_title
    
    
class Chefs(models.Model):
    image = models.ImageField(upload_to='image/chiefs/')
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    available = models.BooleanField(default=True)  # Default should be a boolean value

    def __str__(self):
        return f"Table {self.table_number} ({'Available' if self.available else 'Not Available'})"
    
class Reservation(models.Model):
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    num_guests = models.IntegerField()
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    table_number = models.ForeignKey(Table, on_delete=models.CASCADE)
    special_request = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.customer_name} {self.table_number}"
    

    