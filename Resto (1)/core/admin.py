from django.contrib import admin
from . models import Menu, Table, Reservation, Chefs,MenuType

# Register your models here.
@admin.register(MenuType)
class MenuTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Reservation) 
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'table_number', 'num_guests', 'reservation_date', 'special_request']

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['table_number', 'capacity', 'available']
    
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['menu_title', 'menu_type', 'price', 'created_at']
    
@admin.register(Chefs)
class ChefsAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']
    
    