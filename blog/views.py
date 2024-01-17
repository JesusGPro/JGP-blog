from django.shortcuts import render
from django.utils import timezone
from .models import Post

# views concta modelos con plantillas, para ellos necesitamos los QuerySets (variable posts)

def post_list(request):
    posts = Post.objects.filter(publishing_date__lte=timezone.now()).order_by('publishing_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# request: todo lo que recibimos del usuario por internet
# {'posts': posts} es un lugar ene el que podemos agregar algunas cosas para que la plantilla las use
# lo nombramos de momento 'posts'


