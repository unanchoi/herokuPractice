from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post

def home(request):
    return render(request, 'home.html')


def my_post(request):
    posts = Post.objects.all()
    return render(request, 'myPost.html', {"post_list": posts})


def new_post(request):
    if request.method == 'POST':
        if request.FILES.get('image'):
            Post.objects.create(
                title = request.POST['title'],
                body = request.POST['body'],
                image = request.FILES['image']
            )
        else:
            Post.objects.create(
                title = request.POST['title'],
                body = request.POST['body']
            )
        post_list = Post.objects.all()
        print("test")
        return render(request, 'myPost.html', {'post_list': post_list})
    return redirect('/')


def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'postDetail.html', {"post": post})


def post_update(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        title = request.POST['title'],
        body = request.POST['body'],
        image = request.FILES['image']
        # 밑에 세줄 추가 해주세요!!
        post.title = title
        post.body = body
        post.image = image
        post.save()
        return redirect('/post/'+ str(post.id))
    else:
        return render(request, 'editPost.html', {"post": post})


def post_delete(request, pk):
    post = Post.objects.get(id= pk)
    post.delete()
    return redirect('/my-post')
            