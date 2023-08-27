# from django.views import generic


# # Create your views here.
# from .models import Post

# def blogPost(request):
#     if request.method=="POST":
#         # name=request.POST['full_name']
#         # email=request.POST['email_id']
#         # mobile_num=request.POST['mobile_num']
#         # password=request.POST['pass']
#         # data=Employee(full_name=name,email_id=email,mob_num=mobile_num,password=password)
#         # data.save()
#         # msg="Record Inserted Succesfully !"
#         # print(name+" "+email_id+" "+mobile_num+" "+password)
#         title = request.POST['title']
#         slug = request.POST['slug']
#         author = request.POST['author']
#         content = request.POST['content']
#         # status = request.POST['status']
#         # post = Post(title=title, slug=slug, author=author, content=content, status=status)
#         # post.save()
#         try:
#              post = Post(title=title, slug=slug, author=author, content=content)
#              post.save()
#              print("Post saved successfully")
#         except Exception as e:
#             print("Error saving post:", e)



#         print(title, slug, author, content)
#     return render(request,'post.html')


from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
