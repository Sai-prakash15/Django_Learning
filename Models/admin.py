from django.contrib import admin

# Register your Models here.

from .models import Publication, Article, Reporter, Articler , Place, Restaurant, Content, Video, Car, Truck, Person,InformationX, PlaceX, TaskX, VehicleXx


# class ToDoListAdmin(admin.ModelAdmin):
#     list_display = ['user', '__str__', 'priority','created_timestamp','modified_timestamp']
#     form = ToDoListForm
#     # class Meta:
#     #     model = ToDoList
# class ListItemAdmin(admin.ModelAdmin):
#     list_display = ['to_do_list', '__str__', 'priority','created_timestamp','modified_timestamp']

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
# admin.site.register(Timestamp)
