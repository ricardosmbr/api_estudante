from django.db import models

class Estudante(models.Model):
	
	nome = models.CharField('Nome',max_length=100)
	telefone = models.CharField('Telefone',max_length=100)
	curso = models.CharField('Curso',max_length=100)
	create_at = models.DateTimeField(
		'Criando em',auto_now_add=True, null=True, blank=True
	)
	update_at = models.DateTimeField(
		'Atualizado em',auto_now=True, null=True, blank=True
	)	

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = 'Estudante'
		verbose_name_plural = 'Estudantes'
		ordering = ['nome']	