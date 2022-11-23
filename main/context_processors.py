from .models import Album, Foto
from preferences import preferences
from  django.core.exceptions import ObjectDoesNotExist


def cp(*args):
    context = dict()
    tel1 = str(preferences.PrPreferences.tel1)
    tel2 = str(preferences.PrPreferences.tel2)
    context['tel1plain'] = tel1.replace('-','').replace(' ','')
    context['tel2plain'] = tel2.replace('-','').replace(' ','')
    context['album'] = Foto.objects.filter(foto_album_id=2)
    context['backgrounds'] = Album.objects.get(id=1)

    return context
