from django.db import models

class Mensaje(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	message = models.TextField()
	url = models.CharField(max_length=128, blank=True, default="")
	owner = models.ForeignKey('auth.User', related_name='mensajes', on_delete=models.CASCADE)
	deleted = models.BooleanField(default=False)

	class Meta:
		ordering=['created']