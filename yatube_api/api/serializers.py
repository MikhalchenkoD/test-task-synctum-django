from rest_framework import serializers
from posts.models import Group, Post, Comment
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'text', 'image', 'group', 'pub_date']
        read_only_fields = ['author']

    def get_author(self, obj):
        return obj.author.username if obj.author else None


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ["id", "author", "text", "created", "post"]
        read_only_fields = ['author', 'post']

    def get_author(self, obj):
        return obj.author.username if obj.author else None
