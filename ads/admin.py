from django.contrib import admin


from ads.models import Ad, Category
from users.models import User, Location

admin.site.register(User)
admin.site.register(Location)

admin.site.register(Ad)
admin.site.register(Category)
