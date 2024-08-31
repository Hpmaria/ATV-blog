from django.contrib import admin

# Register your models here.

from .models import CursoRealizado, Gosto, Postagem  

admin.site.register(CursoRealizado)
admin.site.register(Gosto)
admin.site.register(Postagem)


