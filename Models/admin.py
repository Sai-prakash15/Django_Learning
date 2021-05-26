from django.contrib import admin

# Register your Models here.

from .models import Publication, Article, Reporter, Articler , Place, Restaurant, Content, Video, Person,InformationX, PlaceX, TaskX, VehicleXx , Temp ,  Car, Truck,Vehicle


# class ToDoListAdmin(admin.ModelAdmin):
#     list_display = ['user', '__str__', 'priority','created_timestamp','modified_timestamp']
#     form = ToDoListForm
#     # class Meta:
#     #     model = ToDoList
# class ListItemAdmin(admin.ModelAdmin):
#     list_display = ['to_do_list', '__str__', 'priority','created_timestamp','modified_timestamp']
class TempAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    fieldsets = [
        (None, {'fields': ['id']}),
        (None, {'fields': ['name']}),
    ]

class VehicleAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Publication)
admin.site.register(Article)
admin.site.register(Articler)
admin.site.register(Reporter)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Content)
admin.site.register(Video)
admin.site.register(Car)
admin.site.register(Truck)
admin.site.register(Person)
admin.site.register(PlaceX)
admin.site.register(InformationX)
admin.site.register(TaskX)
admin.site.register(VehicleXx)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Temp, TempAdmin)
# admin.site.register(Timestamp)
