from django.contrib import admin

# Register your models here.
from  .models import Thread, Comment, Game
admin.site.register(Thread)
admin.site.register(Comment)
admin.site.register(Game)