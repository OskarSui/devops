# from django.forms import forms

# from blog.models import Comment

#
# class CommentForm(forms.ModelForm):
#     content = forms.CharField(widget=forms.Textarea(attrs={
#         'class': 'form-control',
#         'placeholder': 'Введите свой комментарий',
#         'id': 'usercomment',
#         'rows': '4'
#     }))
#     class Meta:
#         model = Comment
#         fields = ('content', )