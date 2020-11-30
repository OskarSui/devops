from django import forms
from .models import Comment


# class EmailPostForm(forms.Form):
#     name = forms.CharField(max_length=25)
#     email = forms.EmailField()
#     to = forms.EmailField()
#     comments = forms.CharField(required=False,
#                                widget=forms.Textarea)


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('content',)



class CommentForm(forms.ModelForm):
    # content = forms.CharField(label="", widget=forms.Textarea(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Comment here !',
    #     'rows': 4,
    #     'cols': 50
    # }))
    class Meta:
        model = Comment
        fields = ('author', 'content')