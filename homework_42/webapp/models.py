from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя')
    surname = models.CharField(max_length=100, null=False, blank=False, verbose_name='Фамилия')
    email = models.EmailField(null=False, blank=False, verbose_name='E-mail')
    favorit = models.ManyToManyField('Article', related_name='favorites', blank=True)

    def __str__(self):
        return '%s: %s %s' % (self.pk, self.name, self.surname)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Article(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article', verbose_name='Автор')
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Тема')
    content = models.TextField(max_length=5000, null=False, blank=False, verbose_name='Текст')
    date = models.DateField(auto_now_add=True)



    def __str__(self):
        return '%s: %s' % (self.pk, self.title)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='Статья')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Автор')
    answer = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='answers')
    comment = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Комментарий')
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return '%s: %s' % (self.pk, self.comment)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class Rating(models.Model):
    RATE_1 = 'F'
    RATE_2 = 'D'
    RATE_3 = 'C'
    RATE_4 = 'B'
    RATE_5 = 'A'

    RATE_CHOICES = (
        (RATE_1, 'Ужасно'),
        (RATE_2, 'Плохо'),
        (RATE_3, 'Нормально'),
        (RATE_4, 'Хорошо'),
        (RATE_5, 'Отлично')
    )

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='ratings', verbose_name='Статья')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings', verbose_name='Автор')
    rating = models.CharField(max_length=20, choices=RATE_CHOICES, default=None, verbose_name="Оценка")

    def __str__(self):
        return '%s: %s' % (self.pk, self.rating)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

