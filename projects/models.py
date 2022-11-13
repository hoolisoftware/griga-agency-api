from django.db import models

class StackItem(models.Model):
    title = models.CharField('название технологии',max_length=55)
    class Meta:
        verbose_name = 'технология'
        verbose_name_plural = 'технологии'
    def __repr__(self):
        return f'{self.title}'
    def __str__(self):
        return f'{self.title}'

class Project(models.Model):
    title = models.CharField('название проекта',max_length=255)
    image = models.ImageField('изображение',upload_to='projects/image/')
    link = models.URLField('ссылка на проект')
    stack = models.ManyToManyField(verbose_name='стек технологий',to=StackItem)
    link_github = models.URLField('сссылка на гитхаб')
    
    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'
    def __repr__(self):
        return f'{self.link_github}'
    def __str__(self):
        return f'{self.link_github}'