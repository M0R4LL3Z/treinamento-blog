from django.db import models

class Blog(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField(null=True,blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    class Meta:
        verbose_name = "Blog da Amf"
        verbose_name_plural = "Blogs da Amf"

    def __str__(self):
        return self.titulo
