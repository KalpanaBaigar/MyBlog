from datetime import date
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .forms import CommentForm
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse


from . models import Post
# Create your views here.


class StartingPageView(ListView):
  template_name="blog/index.html"
  model=Post
  ordering=["-date"]
  context_object_name="posts"

  def get_queryset(self):
    queryset=super().get_queryset()
    data=queryset[:3]
    return data
    
class AllPostsView(ListView):
  template_name="blog/all-posts.html"
  model=Post
  ordering=["-date"]
  context_object_name="all_posts"


class SinglePostView(View):
  template_name="blog/post-detail.html"
  model=Post
  
  def get(self,request,slug):
    post=Post.objects.get(slug=slug)
    context={
      "post":post,
      "post_tags":post.tags.all(),
      "comment_form":CommentForm()
    }
    return render(request,"blog/post-detail.html",context)

  def post(self,request,slug):  
    comment_form=CommentForm(request.POST)
    post=Post.objects.get(slug=slug)
    
    if comment_form.is_valid():
      comment=comment_form.save(commit=False) 
      comment.post=post
      
      comment.save()
      return HttpResponseRedirect(reverse("post-detail-page",args=[slug]))
   
   
    context={
      "post":post,
      "post_tags":post.tags.all(),
      "comment_form":comment_form

    }
    return render(request,"blog/post-detail.html",context)

  # def get_context_data(self, **kwargs):
  #   context=super().get_context_data(**kwargs)
  #   context["comment_form"]=CommentForm()
  #   return context  

# class SinglePostView(DetailView):
#   template_name="blog/post-detail.html"
#   model=Post


#   def get_context_data(self, **kwargs):
#     context=super().get_context_data(**kwargs)
#     context["comment_form"]=CommentForm()
#     return context

  # def get_context_data(self, **kwargs):
  #   context=super().get_context_data(**kwargs)
  #   context["post_tags"]=self.object.tags.all()





# def post_detail(request,slug):
#   identified_post=get_ov

# def all_posts(request):
#     posts = Post.objects.all()
#     return render(request, "blog/all-posts.html", {
#       "all_posts": posts
#     })



all_posts = [
    # {
    #     "slug": "hike-in-the-mountains",
    #     "image": "mountains.jpg",
    #     "author": "Maximilian",
    #     "date": date(2021, 7, 21),
    #     "title": "Mountain Hiking",
    #     "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
    #     "content": """
    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    #     """
    # },
    # {
    #     "slug": "programming-is-fun",
    #     "image": "coding.jpg",
    #     "author": "Maximilian",
    #     "date": date(2022, 3, 10),
    #     "title": "Programming Is Great!",
    #     "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
    #     "content": """
    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    #     """
    # },
    # {
    #     "slug": "into-the-woods",
    #     "image": "woods.jpg",
    #     "author": "Maximilian",
    #     "date": date(2020, 8, 5),
    #     "title": "Nature At Its Best",
    #     "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
    #     "content": """
    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    #     """
    # }
]
def get_date(post):
  return post['date']

# def starting_page(request):
#   latest_posts=Post.objects.all().order_by("-date")[:3]
#   # sorted_posts =sorted(all_posts,key=get_date)
#   # latest_post=sorted_posts[-3:]   

#   return render(request,"blog/index.html",{
#     "posts":latest_posts
#   })
   

# def starting_page(request):
#     posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html", {
#       "posts": posts
#     })
#  return render(request, "blog/index.html", {
#       "posts": latest_posts
#     })

# def all_posts(request):
    # posts = Post.objects.all()
    # return render(request, "blog/all-posts.html", {
    #   "all_posts": posts
    # })