from django.contrib import admin
from .models import User, Group, User_Group, Restaurant, Restaurant_Group, Vote

admin.site.register(User)
admin.site.register(Group)
admin.site.register(User_Group) 
admin.site.register(Restaurant)
admin.site.register(Restaurant_Group)
admin.site.register(Vote)



# Register your models here.
