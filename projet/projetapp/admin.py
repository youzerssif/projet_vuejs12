# vim: set fileencoding=utf-8 :
from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


class utilisateurAdmin(admin.ModelAdmin):

    list_display = (
        'affiche_image',
        'name',
        'username',
        'email',
        'phone',
        'images',
        'password',
        'password1',
        'date_add',
        'date_update',
        'staut',
    )
    list_filter = (
        'name',
        'username',
        'email',
        'phone',
        'images',
        'password',
        'password1',

    )
    def affiche_image(self, obj):
        return mark_safe('<img src = " {url} " width = " 100px " heigth = " 30px " />'.format(url= obj.images.url))

    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.utilisateur, utilisateurAdmin)
