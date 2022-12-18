from rest_framework import viewsets
from .models import Genre, Movie
from .serializers import GenreSerializer, MovieSerializer, UpdateMovieSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.select_related("genre").all()
    # serializer_class = MovieSerializer


    def get_serializer_class(self):
        if self.request.method == "PUT":
            return UpdateMovieSerializer
        elif self.request.method == "POST":
            return UpdateMovieSerializer
        else:
            return MovieSerializer