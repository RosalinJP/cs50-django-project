from django.shortcuts import render

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