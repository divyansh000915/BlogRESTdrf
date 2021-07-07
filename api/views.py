from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser




from rest_framework import generics
from api import serializers
from django.contrib.auth.models import User

from api.models import Post

from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly

from api.models import Comment
from api.models import Category

from .responseMethod import errorResponseMethodToken, successResponseMethodToken, successResponseMethod, \
    errorResponseMethod
from rest_framework.response import Response
from rest_framework import status





class AppToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        print("yo1")
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})

        print("yo2")
        if serializer.is_valid():
            print("yo")
            user = serializer.validated_data['user']
            password = serializer.validated_data['password']
            # print(user)
            # print(password)
            print("yo")
            token, created = Token.objects.get_or_create(user=user)
            print(token)
            print("yo")
            # print("token id ")
            # print(token.user_id)
            # print(token.user)
            # print(token.user.is_staff)
            print("yo")
            # if token.user.is_staff:
            #     try:
            #         vendor_now = Vendor_management.objects.filter(user=token.user)
            #     except:
            #         return Response(errorResponseMethodToken(request, 'Invalid username and password!'),status=status.HTTP_400_BAD_REQUEST)
            #     data = GetCurrentUserWithToken().get_VendorManagementData(token.user)
            # else:
            try:
                print("yoidk")
                user_now = User.objects.filter(username=token.user.username)
                print("yo2")
            except:
                return Response(errorResponseMethodToken(request, 'Invalid username and password!'),status=status.HTTP_400_BAD_REQUEST)
            #data = GetCurrentUserWithToken().get_data(token.user)
            
            #context = {"token": token.key, "userDetails": data} Commented 14/09
            
            #data["token"] = token.key #added on 14/09

            #if data:
                #return Response(successResponseMethodToken(request, context))  # token.key
                
                #return Response (data)
            #    return Response (user_now)
            data = { "id" : user_now[0].id, "userame" : user_now[0].username, "token" : token.key}
            return Response (data)

            #return Response(errorResponseMethodToken(request, 'User information not exists')) #Commented for Prabha
            return Response(errorResponseMethodToken(request, 'User information not exists'),status=status.HTTP_404_NOT_FOUND)
        else:
            #return Response(errorResponseMethodToken(request, serializer.errors)) #Commented for Prabha
            return Response(errorResponseMethodToken(request, serializer.errors),status=status.HTTP_401_UNAUTHORIZED)
            #return Response(errorResponseMethodToken(request, serializer.errors))


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,) 
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        print (self.request.user)
        serializer.save(owner=self.request.user)

    # @detail_route(methods=['post'])
    # def upload_docs(request):
    #     try:
    #         file = request.data['file']
    #     except KeyError:
    #         raise ParseError('Request has no resource file attached')
    #     newpost = Post.objects.create(image=file, ....)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
# Create your views here.

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
