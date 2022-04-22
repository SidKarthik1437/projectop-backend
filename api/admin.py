from django.contrib import admin

# Register your models here.
from .models import Prob
from .models import User

admin.site.register(Prob)
admin.site.register(User)
