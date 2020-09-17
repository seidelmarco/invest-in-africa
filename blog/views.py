from django.shortcuts import render
from django.utils import timezone

from .models import Post
# Und nun? Um vom Post-Model die tatsächlichen Blogposts zu erhalten, brauchen wir etwas, das QuerySet heißt.

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# Beachte, dass wir eine Variable für unser QuerySet erstellt haben: posts. Das ist sozusagen der Name unseres
# QuerySets. Ab jetzt bezeichnen wir das QuerySet mit diesem Namen.

# Warum das dict in der render response?
# In der render-Funktion haben wir einen Parameter request (also alles, was wir vom User über das Internet bekommen)
# und einen weiteren Parameter, der den Template-Namen ('blog/post_list.html') angibt. Der letzte Parameter, {}, ist
# eine Stelle, in der wir weitere Dinge hinzufügen können, die das Template dann benutzen kann. Wir müssen diesen einen
# Namen geben (wir verwenden einfach wieder 'posts'). :) Es sollte nun so aussehen: {'posts': posts}. Bitte achte
# darauf, dass der Teil vor : ein String ist; das heißt, du musst ihn mit Anführungszeichen '' umschliessen.
