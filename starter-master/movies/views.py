from django.shortcuts import get_object_or_404, render
from .models import Movie
 

# Create your views here.

def home(request):
    movies_list = Movie.objects.order_by('title')[:5]
    context = {'movies_list': movies_list}
    return render(request, 'movie.html', context)
	
def detail(request, id):
    movie = get_object_or_404(Movie, pk=id)
    return render(request, 'detail.html', {'movie': movie})
	
def signup(request):
	return render(request, 'signup.html')