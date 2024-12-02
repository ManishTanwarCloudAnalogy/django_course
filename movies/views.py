from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies': [
        {'id': 1, 'name': 'Terminator', 'year': 2020},
        {'id': 2, 'name': 'Inception', 'year': 2010},
        {'id': 3, 'name': 'The Matrix', 'year': 1999},
        {'id': 4, 'name': 'The Godfather', 'year': 1972},
        {'id': 5, 'name': 'Pulp Fiction', 'year': 1994},
        {'id': 6, 'name': 'The Dark Knight', 'year': 2008},
        {'id': 7, 'name': 'Forrest Gump', 'year': 1994},
        {'id': 8, 'name': 'Interstellar', 'year': 2014},
        {'id': 9, 'name': 'Gladiator', 'year': 2000},
        {'id': 10, 'name': 'Titanic', 'year': 1997}
    ],
    'documentaries': [
        {'id': 1, 'name': 'Planet Earth', 'year': 2006},
        {'id': 2, 'name': 'The Last Dance', 'year': 2020},
        {'id': 3, 'name': 'Won’t You Be My Neighbor?', 'year': 2018},
        {'id': 4, 'name': '13th', 'year': 2016},
        {'id': 5, 'name': 'Free Solo', 'year': 2018},
        {'id': 6, 'name': 'My Octopus Teacher', 'year': 2020},
        {'id': 7, 'name': 'Making a Murderer', 'year': 2015},
        {'id': 8, 'name': 'Inside Job', 'year': 2010},
        {'id': 9, 'name': 'An Inconvenient Truth', 'year': 2006},
        {'id': 10, 'name': 'American Factory', 'year': 2019}
    ]
}


def movies(request):
    return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse("Home Page")  # This will cause an error because we are redefining