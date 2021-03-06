from django.db import models


class Subscription(models.Model):
    class Meta:
        verbose_name_plural = 'inscrições'
        verbose_name = 'inscrição'
        ordering = ('-created_at',)

    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11)
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone', max_length=20)
    created_at = models.DateTimeField('criado em', auto_now=True)
    paid = models.BooleanField('pago', default=False)

    def __str__(self):
        return self.name
