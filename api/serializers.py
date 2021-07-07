from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Comment


from api.models import Post
from api.models import Category

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'owner', 'posts']


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #like_count = serializers.IntegerField(required=False)
    like_count =serializers.SerializerMethodField('get_likecnt')
    categories = serializers.SerializerMethodField('get_cat')
    created = serializers.DateTimeField(format='%m/%d/%Y %H:%M:%S')


    #image_url = serializers.SerializerMethodField('get_image_url')



    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner','comments', 'categories', 'created', 'image', 'liked_by', 'like_count']
    
    # def get_image_url(self, obj):
    #     request = self.context.get("request")
    #     return request.build_absolute_uri(obj.image.url)
    def get_likecnt(self,obj):
        return obj.liked_by.all().count()

    def get_cat(self,obj):
        return list(Category.objects.filter(posts = obj).values('id'))

class UserSerializer(serializers.ModelSerializer):
        
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = User
        fields = ['id', 'username', 'first_name','last_name', 'posts','comments', 'categories']

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'post']





