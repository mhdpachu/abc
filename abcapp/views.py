from django.shortcuts import render,redirect,get_object_or_404
from . models  import Category,Item
# Create your views here.
def home(request,category_id=None):
    categories=Category.objects.all()
    if category_id:
        items=Item.objects.filter(category_id=category_id)
    else:
        items=Item.objects.all()
       
    return render(request,'home.html',{'items':items,'categories':categories})
def sample(request):
    return render(request,'sample.html')

def user_product(request):
    if request.method == "POST":
        name=request.POST['name']
        category_id=request.POST['category']
        price=request.POST['price']
        image=request.FILES.get('image')
        category=Category.objects.get(id=category_id)
        obj=Item(name=name,category=category,price=price,image=image)
        obj.save()
        return redirect('home')
    categories=Category.objects.all()
    return render(request,'user_product.html',{'categories':categories})



def delete(request,taskid):
    if request.method=="POST":
        item=get_object_or_404(Item,id=taskid)
        item.delete()
    return redirect('/')