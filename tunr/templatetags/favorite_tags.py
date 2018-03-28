from django import template

register = template.Library()

@register.filter(name='has_favorite')
def has_favorite(song, user):
    return song.favorites.filter(user=user).exists()
