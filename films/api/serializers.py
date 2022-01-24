from films.models import Movie

from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        field = (
            'id',  
            'name',
            'description',
            'image',
        )

        read_only_Fields = ('id',)  