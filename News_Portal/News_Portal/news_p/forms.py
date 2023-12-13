from django.forms import ModelForm
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from .models import Post


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'category', 'type']


