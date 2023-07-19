from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CatShop
from .serializers import CatShopSerializer
from rest_framework import status


class CatShopList(APIView):
    def get(self, request):
        CatShops = CatShop.objects.all()
        serializer = CatShopSerializer(CatShops, many  = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CatShopSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

class CatShopDetail(APIView):
    def get(self, request, pk):
        catshop = CatShop.objects.get(pk = pk)
        serializer = CatShopSerializer(catshop)
        return Response(serializer.data)
    def put(self, request, pk):
        catshop = CatShop.objects.get(pk=pk)
        serializer = CatShopSerializer(catshop, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(selt, request, pk):
        catshop = CatShop.objects.get(pk=pk)
        catshop.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    

