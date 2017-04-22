from django.contrib import admin
from .models import Registro

class RegistroAdmin(admin.ModelAdmin):
	model = Registro
	list_display = ['data', 'hora', 'minuto','sistema', 'comando', 'descricao','concluido']
	list_filter = ['data', 'comando','concluido']
	search_fields = ['sistema']
	save_on_top = True
admin.site.register(Registro, RegistroAdmin)