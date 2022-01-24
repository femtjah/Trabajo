from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from films.api.serializers import MovieSerializer



class MovieViewSet (viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    permission_class = (IsAuthenticated,)
    queryset = MovieSerializer.Meta.model.objects.all()

    def get_queryset(self, pk= None):
        if pk is None:
            return self.get_queryset().Meta.Model.filter(id = pk).first()
        return self.get_queryset().Meta.Model.filter(id = pk).first()

    def create(self,request):
        serializer = self.serializer_class(data= request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Producto creado correctamente!'},status= status.HTTP_200_OK)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            movie_serializer = self.serializer_class(self.get_queryset(pk),data=request.data)
            if movie_serializer.is_valid():
                movie_serializer.save()
                return Response(movie_serializer.data,status= status.HTTP_200_OK)
        return Response(movie_serializer.errors,status= status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        movie = self.get_queryset().filter(id = pk).first()
        if movie:
            movie.delete()
            movie.save()
            return Response({'message': 'Producto eliminado correctamente!'},status= status.HTTP_200_OK)
        return Response(movie.errors,status= status.HTTP_400_BAD_REQUEST)