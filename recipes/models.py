from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    '''DateTimeField > auto_now_add > gera automaticamente a data inicial de
    criaçao da recipe'''
    created_at = models.DateTimeField(auto_now_add=True)
    # DateTimeField > auto_now > gera a data de update da recipe
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')
    '''Faz relaçao com a tabela Category, e se nao existir a categoria ou for
    excluida, ele setta esse campo como null, null=True significa que esse
    campo pode ser null, esta habilitando
    blank permite deixar sem imagem na recipe e default diz que por padrao ela nao recebe imagem'''
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, default=None,)
    ''' Faz relaçao com a tabela User, onde vai ser usado a propria tabela dele
    para salvar os author, seguindo a mesma logica de category, se nao exister
    ou for excluido, o campo se torna null '''
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
