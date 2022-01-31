from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.code} - {self.name}'


class DefaultTranslation(models.Model):
    user_id = models.CharField(max_length=1000)
    src = models.CharField(max_length=10)
    src_name = models.CharField(max_length=255, null=True, blank=True)
    dest = models.CharField(max_length=10)
    dest_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.user_id} - src: {self.src_name} - dest: {self.dest_name}'
