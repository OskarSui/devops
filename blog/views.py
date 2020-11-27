from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post
from django.db.models import Q

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset =queryset.filter(Q(title__icontains=search) | Q(content__icontains=search))
        return queryset

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
#
#     def post_single(request, pk):
#         post = get_object_or_404(Post, pk=pk)
#         comment = Comment.objects.filter(post=post)
#         if request.method == "POST":
#             form = CommentForm(request.POST)
#             if form.is_valid():
#                 comm = form.save(commit=False)
#                 comm.user = request.user
#                 comm.post = post
#                 comm.save()
#         else:
#             form = CommentForm()
#         return render(request, 'blog/post_detail.html', {"post":post, "form":form, "comment":comment})
#


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# class TagDetail(ObjectDetailMixin, View):


# def post_share(request, post_id):
#     # Получение статьи по идентификатору.
#     post = get_object_or_404(Post, id=post_id, status='published')
#     sent = False
#     if request.method == 'POST':
#         # Форма была отправлена на сохранение.
#         form = EmailPostForm(request.POST)
#         if form.is_valid():
#             # Все поля формы прошли валидацию.
#             cd = form.cleaned_data
#             # ... Отправка электронной почты.
#             post_url = request.build_absolute_uri(post.get_absolute_url())
#             subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
#             message = 'Read "{}" at {}\n\n{}\'s comments:{}'.format(post.title, post_url, cd['name'], cd['comments'])
#             send_mail(subject, message, 'admin@myblog.com', [cd['to']])
#             sent = True
#         else:
#             form = EmailPostForm()
#             return render(request, 'blog/share.html',
#                           {'post': post, 'form': form, 'sent': sent})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})