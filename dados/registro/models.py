from django.db import models

class Registro(models.Model):

	HORA_CHOICES = [
		(u'00',u'00'),
		(u'01',u'01'),
		(u'02',u'02'),
		(u'03',u'03'),
		(u'04',u'04'),
		(u'05',u'05'),
		(u'06',u'06'),
		(u'07',u'07'),
		(u'08',u'08'),
		(u'09',u'09'),
		(u'10',u'10'),
		(u'11',u'11'),
		(u'12',u'12'),
		(u'13',u'13'),
		(u'14',u'14'),
		(u'15',u'15'),
		(u'16',u'16'),
		(u'17',u'17'),
		(u'18',u'18'),
		(u'19',u'19'),
		(u'20',u'20'),
		(u'21',u'21'),
		(u'22',u'22'),
		(u'23',u'23'),
		(u'24',u'24'),

	]
	MINUTO_CHOICES = [
		(u'00',u'00'),
		(u'15',u'15'),
		(u'30',u'30'),
		(u'45',u'45'),

	]

	SISTEMA_CHOICES = [
		(u'anexar',u'Anexar'),
		(u'aviso',u'Aviso'),
		(u'estrutura',u'Estrutura'),
		(u'safari',u'Safari'),
		(u'sublime',u'Sublime Text 2'),
		(u'projeto',u'Projeto'),
		(u'terminal',u'Terminal'),
		(u'transferencia',u'Transferência'),
		(u'war',u'War'),
		(u'outro',u'Outro'),

	]

	COMANDO_CHOICES = [
		(u'1',u'cd'),
		(u'2',u'mkdir'),
		(u'3',u'django-admin startproject'),
		(u"4",u"settings.py LANGUAGE_CODE = 'pt-br'"),
		(u'5',u'Outro'),

		

	]



	data = models.DateField(verbose_name='Data')
	hora = models.CharField(max_length=2,choices = HORA_CHOICES)
	minuto = models.CharField(max_length=2,choices = MINUTO_CHOICES)
	sistema = models.CharField(max_length=20,choices = SISTEMA_CHOICES)
	comando = models.CharField(max_length=50,choices = COMANDO_CHOICES)
	descricao = models.TextField(verbose_name='Descrição')
	concluido = models.BooleanField(verbose_name='Concluído')
	

	class Meta:
		verbose_name = "Registro"
		verbose_name_plural = "Registro"


