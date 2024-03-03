from django.contrib import admin
from .models import Public_board, Authors_public, Relevance_board

# Register your models here.
admin.site.register(Public_board)
admin.site.register(Authors_public)
admin.site.register(Relevance_board)
