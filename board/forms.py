from django import forms
from .models import PostContents, BoardBase
from django.forms import ModelForm

class PostForm(ModelForm):
    class Meta:
        model = PostContents
        fields = ('post_user', 'post_title', 'post_content','post_category')

    post_user = forms.CharField(
        label='投稿者',
        max_length=20,
        required=True,
        widget=forms.TextInput()
    )
    post_title = forms.CharField(
        label='タイトル',
        max_length='50',
        required=True,
        widget=forms.TextInput()
    )
    post_content = forms.CharField(
        label='内容',
        max_length=400,
        required=True,
        widget=forms.Textarea
    )
    post_category = forms.ModelChoiceField(
        queryset=BoardBase.objects,
        required=True,
    )


class MakeBoard(ModelForm):
    class Meta:
        model = BoardBase
        fields = ('board_title', 'board_about')

    board_title = forms.CharField(
        label='掲示板タイトル',
        max_length=50,
        required=True,
        widget=forms.TextInput()
    )
    board_about = forms.CharField(
        label='掲示板の説明',
        max_length=100,
        required=True,
        widget=forms.Textarea
    )

