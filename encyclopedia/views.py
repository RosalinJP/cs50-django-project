from django.shortcuts import render,redirect
from django.urls import reverse

from . import util
# add markdown to change md to html
import markdown2

from django import forms

class NewPageForm(forms.Form): 
    title = forms.CharField(label="Page Title")


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request,title):
    content=util.get_entry(title)
    
    return render(request, "encyclopedia/entry.html",{
        "html_content": markdown2.markdown(content),
        "title":title
    })

def search(request):
    if request.method == "POST":
        query = request.POST.get("q","").strip()
        entries = util.list_entries()
        # Case 1: exact match → redirect
        if query.lower() in [entry.lower() for entry in entries]:
            return redirect(reverse("entry", kwargs={"title": query}))

        # Case 2: partial matches
        else:
                matches = [entry for entry in entries if query.lower() in entry.lower()]
                if matches:
                     return render(request,"encyclopedia/search.html",{
                        "query":query,
                        "entries":matches
                         } )
            

            
        # Case 3: show results page
        return render(request,"encyclopedia/index.html",{
            "message":"no result found"
        })


def new(request):
    
    if request.method=="POST":
        title = request.POST.get("title","").strip()
        content = request.POST.get("markdown_content")
        entries=util.list_entries()
        if title.lower() in [entry.lower() for entry in entries] :
            return render(request,"encyclopedia/new.html",{
                "message":"Error:Title already exist in directory"
            })
        util.save_entry(title,content)
        return redirect("entry",title=title)
    return render(request,"encyclopedia/new.html")   

def edit (request):
    if request.method == "GET":
        title=request.GET.get("title")
        content=util.get_entry(title)
        return render (request,"encyclopedia/edit.html",{
            "title":title,
            "content":content
         })
def save(request):
    if request.method=="POST":
        title=request.POST.get("title")
        new_content=request.POST.get("content")
        util.save_entry(title,new_content)
        return redirect("entry",title=title)
