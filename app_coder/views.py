import os
from datetime import date
from django.shortcuts import render
from django.db.models import Q
from django.forms.models import model_to_dict
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from app_coder.models import Articles, Comments, Avatar
from django.contrib.auth.models import User
from app_coder.forms import ArticlesForm, CommentsForm, AvatarForm

from django.contrib import messages


def index(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/home.html"
    )


def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {"url": avatars[0].image.url}
    return {}

def articles(request):
    articles = Articles.objects.all()

    context_dict = {
        'articles': articles
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/articles.html"
    )

def comments(request):
    comments = Comments.objects.all()

    context_dict = {
        'comments': comments
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/comments.html"
    )

def form_hmtl(request):

    if request.method == 'POST':
        article = Articles(title=request.POST['title'], sub_title=request.POST['subtitle'])
        article.save()

        articles = Articles.objects.all()
        context_dict = {
            'articles': articles
        }

        return render(
            request=request,
            context=context_dict,
            template_name="app_coder/courses.html"
        )

    return render(
        request=request,
        template_name='app_coder/formHTML.html'
    )

@login_required
def articles_forms_django(request):
    if request.method == 'POST':
        article_form = ArticlesForm(request.POST, request.FILES)

        if article_form.is_valid():
            data = article_form.cleaned_data
            articles = Articles(title=data['title'], sub_title=data['sub_title'], text = data ['text'],author = data['author'])

            image = request.FILES['image']
            if len(request.FILES) != 0:
                articles.image = image
            articles.save()

            articles = Articles.objects.all()
            context_dict = {
                'articles': articles
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/articles.html"
            )

    article_form = ArticlesForm(request.POST)
    context_dict = {
        'article_form': article_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/article_django_forms.html'
    )
      
@login_required
def update_article(request, pk: int):
    article = Articles.objects.get(pk=pk)

    if request.method == 'POST':
        article_form = ArticlesForm(request.POST)
        if article_form.is_valid():
            data = article_form.cleaned_data
            article.title = data['title']
            article.sub_title = data['sub_title']
            article.tect = data['text']
            article.save()

            articles = Articles.objects.all()
            context_dict = {
                'articles': articles
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/articles.html"
            )

    article_form = ArticlesForm(model_to_dict(article))
    context_dict = {
        'article': article,
        'article_form': article_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/article_form.html'
    )


@login_required
def delete_article(request, pk: int):
    article = Articles.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()

        articles = Articles.objects.all()
        context_dict = {
            'articles': articles
        }
        return render(
            request=request,
            context=context_dict,
            template_name="app_coder/articles.html"
        )

    context_dict = {
        'article': article,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/article_confirm_delete.html'
    )

@login_required
def comment_forms_django(request):
    if request.method == 'POST':
        comment_form = CommentsForm(request.POST,comment_id)
        if comment_form.is_valid():
            data = comment_form.cleaned_data
            
            comments = Comments(data = data['data'],due_date = date.today(), comment_by = request.user.id,article = article_id)
            comments.save()

            comments = Comments.objects.all()
            context_dict = {
                'comments': comments
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/comments.html"
            )

    comment_form = CommentsForm(request.POST)
    context_dict = {
        'comment_form': comment_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/comment_django_forms.html'
    )
      
@login_required
def update_comment(request, pk: int):
    comments = Comments.objects.get(pk=pk)

    if request.method == 'POST':
        comment_form = CommentsForm(request.POST)
        if comment_form.is_valid():
            data = comment_form.cleaned_data
            comments.save()

            comments = Comments.objects.all()
            context_dict = {
                'comments': comments
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/comments.html"
            )

    comment_form = CommentsForm(model_to_dict(comments))
    context_dict = {
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/comment_form.html'
    )


@login_required
def delete_comment(request, pk: int):
    comment = Comments.objects.get(pk=pk)
    if request.method == 'POST':
        comments.delete()

        comments = Comments.objects.all()
        context_dict = {
            'comments': comments
        }
        return render(
            request=request,
            context=context_dict,
            template_name="app_coder/comments.html"
        )

    context_dict = {
        'comment': comment,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/comment_confirm_delete.html'
    )

def comment_forms_django(request):
    if request.method == 'POST':
        comments_form = CommentsForm(request.POST)
        if comments_form.is_valid():
            data = comments_form.cleaned_data
            comment = Comments(
                name=data['name'],
                due_date=data['due_date'],
                is_delivered=data['is_delivered'],
            )
            comment.save()

            comments = Comments.objects.all()
            context_dict = {
                'comments': comments
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/comments.html"
            )

    comments_form = CommentsForm(request.POST)
    context_dict = {
        'comments_form': comments_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/comment_django_forms.html'
    )


def search(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    if request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(title__contains=search_param)
        query.add(Q(sub_title__contains=search_param), Q.OR)
        articles = Articles.objects.filter(query)
        context_dict.update({
            'articles': articles
        })
    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/home.html",
    )

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import loader


class ArticlesListView(ListView):
    model = Articles
    template_name = "app_coder/articles_list.html"


def ArticlesDetailView(request,pk):

    article = Articles.objects.get(id=pk)
    
    comments = list(Comments.objects.filter(article_id=pk).values_list('data'))
    context_dict = {
        'article': article,
        'comments':comments,
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/articles_detail.html"
    )
    


class ArticlesCreateView(LoginRequiredMixin, CreateView):
    model = Articles
    # template_name = "app_coder/course_form.html"
    # success_url = "/app_coder/courses"
    success_url = reverse_lazy('app_coder:articles-list')
    fields = ['title', 'sub_title', 'text', 'image', ]



class CommentsCreateView(LoginRequiredMixin,CreateView):
    model = Comments

    template_name = "app_coder/coments_create.html"

    success_url = reverse_lazy('app_coder:articles-list')
    fields = ['data']


    def form_valid(self, form):
        form.instance.article = Articles.objects.get(id=self.kwargs.get('pk'))
        return super(CommentsCreateView, self).form_valid(form)

class ArticlesUpdateView(LoginRequiredMixin, UpdateView):
    model = Articles
    # template_name = "app_coder/course_form.html"
    # success_url = "/app_coder/courses"
    success_url = reverse_lazy('app_coder:articles-list')
    fields = ['title', 'sub_title','text', 'image']


class ArticlesDeleteView(LoginRequiredMixin, DeleteView):
    model = Articles
    # success_url = "/app_coder/courses"
    success_url = reverse_lazy('app_coder:articles-list')


from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from app_coder.forms import UserRegisterForm, UserEditForm

from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado exitosamente!")
            return redirect("app_coder:user-login")
    # form = UserCreationForm()
    form = UserRegisterForm()
    return render(
        request=request,
        context={"form":form},
        template_name="app_coder/register.html",
    )


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("app_coder:Home")

        return render(
            request=request,
            context={'form': form},
            template_name="app_coder/login.html",
        )

    form = AuthenticationForm()
    return render(
        request=request,
        context={'form': form},
        template_name="app_coder/login.html",
    )


def logout_request(request):
      logout(request)
      return redirect("app_coder:user-login")


@login_required
def user_update(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.email = informacion['email']
            user.password1 = informacion['password1']
            user.password2 = informacion['password2']
            user.save()

            return redirect('app_coder:Home')

    form= UserEditForm(model_to_dict(user))
    return render(
        request=request,
        context={'form': form},
        template_name="app_coder/user_form.html",
    )


@login_required
def avatar_load(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid  and len(request.FILES) != 0:
            image = request.FILES['image']
            avatars = Avatar.objects.filter(user=request.user.id)
            if not avatars.exists():
                avatar = Avatar(user=request.user, image=image)
            else:
                avatar = avatars[0]
                if len(avatar.image) > 0:
                    os.remove(avatar.image.path)
                avatar.image = image
            avatar.save()
            messages.success(request, "Imagen cargada exitosamente")
            return redirect('app_coder:Home')

    form= AvatarForm()
    return render(
        request=request,
        context={"form": form},
        template_name="app_coder/avatar_form.html",
    )

def about_me (request): 
    return render(
        request=request,
        context= {},
        template_name="app_coder/about_me.html"
    )