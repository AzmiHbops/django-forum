from django.shortcuts import render, redirect, get_object_or_404
from Post.models import Post
from .models import Comment

# Create your views here.

def create(request, parent, parent_id):
    next = request.GET["next"]
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        body = request.POST.get('body')

        #Validating name and body
        #Checking if its a comment on a post itself or a reply to comment via the parent argument passed
        if name and body:
            if parent == "post":
                parent = Post.objects.get(id=parent_id)
                Comment.objects.create(name=name, email=email, post=parent, body=body)
            else:
                parent = Comment.objects.get(id=parent_id)
                Comment.objects.create(name=name, email=email, parent=parent, body=body)
            return redirect(next)
    return render(request, "comment/create.html")



#View to show Twitter-like reply structure
def replies(request, pk):
    reply = Comment.objects.get(id=pk) #Getting the comment with replies user wants to view
    variable_swap = reply
    parent_list = []
    while variable_swap:    #Loop is getting all parents of reply in line(-2) up
        parent_list.insert(0, variable_swap)
        variable_swap = variable_swap.parent
    context = {
        'reply':reply,
        'parents':parent_list
    }

    return render(request, "comment/replies.html", context)


#def delete
#Should only show if user is an admin
def delete(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    next = request.GET["next"]
    context = {'comment':comment}
    if request.method == "POST":
        comment.delete()
        return redirect(next)
        
    return render(request, "post/delete.html", context)




