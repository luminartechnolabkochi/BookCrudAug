from django.shortcuts import render

from django.views.generic import View

from store.forms import BookForm

# Create your views here.


# BookCreateView
# url:localhost:8000/books/add/
# method:

    # GET:book_add.html,form
    #POST:create  book object


class BookCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=BookForm()

        return render(request,"book_add.html",{"form":form_instance})

