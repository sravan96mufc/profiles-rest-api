from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from profiles_api import serializers
from django.shortcuts import render

#######################3import shortcuts page 210
from .models import Category, Product

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})


    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def put(self, request, pk=None):
        """ updationg"""
        return Response({'method':'PUT'})
    def patch(self, request, pk=None):
        """handkle partial update"""
        return Response({'method':'PATCH'})
    def delete(self, request, pk=None):
        """ delete obj"""
        return Response({'method':'DELETE'})



class HelloViewSet(viewsets.ViewSet):
    """test api viewsers"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ return ahekkio messafge"""
        a_viewset = [
        'tryhhffhfhfhf',
        'jhgyhjgygyjhgjg',
        'fhgfhfhfhhfgjggjg,'
        ]
        return Response({'message': 'hello', 'a_viewset': a_viewset})

    def create(self, request):
        """ create a new hello msg"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello{name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST

            )
    def retrieve(self, request, pk=None):
        """ handle getting item by id"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """handle update an objects"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """handle update part of an objects"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """handle deletion an objects"""
        return Response({'http_method':'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
    """ handle updating and creating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """ handlecreating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)

################################################3


def product_list(request, category_slug=None):
    category = None
    categories = Categories.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    return render(request,
                    'profiles_api/product/list.html',
                    {'category': category,
                     'categories': categories,
                     'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug)
                                ###available=True)
    return render(request,
                    'profiles_api/product/detail.html',
                    {'product': product})
