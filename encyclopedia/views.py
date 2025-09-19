from django.shortcuts import render,redirect
from django.urls import reverse

from . import util
# add markdown to change md to html
import markdown2

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
    



            




        
