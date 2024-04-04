from django.shortcuts import render
from django.views.generic import View
# Create your views here.


class BlogListView(View):
    def get(self,request,*arg,**kwargs):
        context={
            
        }
        
        return render(request,'blog_list.html',context)