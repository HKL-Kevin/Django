from django.shortcuts import render,HttpResponse,redirect
from app01 import models

# 展示所有出版社
def publisher_list(request):
    all_publisher = models.Publisher.objects.all().order_by("id")
    return render(request,'publisher_list.html',{"all_publisher":all_publisher})

# 新增出版社
def publisher_add(request):
    if request.method == "POST":
        pub_name = request.POST.get('pub_name')
        print(pub_name)
        if pub_name == "":
            return render(request,"publisher_add.html",{"error":"出版社名称不能为空!"})
        if models.Publisher.objects.filter(name = pub_name):
            return render(request,"publisher_add.html",{"error":"出版社名称已存在!"})
        models.Publisher.objects.create(name=pub_name)
        return redirect("/publisher_list/")
    return render(request,"publisher_add.html")

# 删除出版社
def publisher_del(request):
    pk = request.GET.get('pk')
    models.Publisher.objects.filter(pk=pk).delete()
    return redirect("/publisher_list/")

# 编辑出版社
def publisher_eidt(request):
    pk = request.GET.get('pk')
    pub_obj = models.Publisher.objects.get(pk=pk)
    if request.method == "GET":
        return render(request,"publisher_edit.html",{"pub_obj":pub_obj})
    elif request.method == "POST":
        pub_name = request.POST.get("pub_name")
        if pub_name == "":
            return render(request,"publisher_add.html",{"error":"出版社名称不能为空!"})
        if models.Publisher.objects.filter(name = pub_name):
            return render(request,"publisher_add.html",{"error":"出版社名称已存在!"})
        pub_obj.name = pub_name
        pub_obj.save()
        return redirect("/publisher_list/")

# 展示所有书籍
def book_list(request):
    all_book = models.Book.objects.all().order_by("id")
    return render(request,"book_list.html",{"all_book":all_book})

# 新增书籍
def book_add(request):
    error = ''
    if request.method == "POST":
        book_name = request.POST.get("book_name")
        det = request.POST.get("det")
        pub_id = request.POST.get("pub_id")
        author_ids = request.POST.getlist("author_ids")
        print(author_ids)
        if not book_name:
            error = "书名不能为空！"
        elif models.Book.objects.filter(name=book_name,publisher_id=pub_id):
            error = "该书已存在！"
        else:
            book_obj = models.Book.objects.create(name = book_name,publisher_id=pub_id,detail = det)
            book_obj.author.set(author_ids)
            return redirect("/book_list/")
    all_publisher = models.Publisher.objects.all()
    all_author = models.Author.objects.all()
    return render(request,"book_add.html",{"all_publisher":all_publisher,"all_author":all_author,"error":error})

# 删除书籍
def book_del(request):
    pk = request.GET.get("pk")
    models.Book.objects.filter(pk=pk).delete()
    # return HttpResponse("oK!")
    return redirect("/book_list/")

# 编辑书籍
def book_edit(request):
    error=""
    pk = request.GET.get("pk")
    book_obj = models.Book.objects.get(pk=pk)
    if request.method == "POST":
        book_name=request.POST.get("book_name")
        pub_id=request.POST.get("pub_id")
        det = request.POST.get("det")
        if not book_name:
            error="书籍名称不能为空!"
        else:
            models.Book.objects.filter(pk=pk).update(name=book_name,publisher_id=pub_id,detail=det)
            return redirect("/book_list/")
    
    all_publisher = models.Publisher.objects.all()
    all_author = models.Author.objects.all()
    return render(request,"book_edit.html",{"book_obj":book_obj,"all_publisher":all_publisher,"all_author":all_author,"error":error})


def author_list(request):
    all_author = models.Author.objects.all()
    return render(request,"author_list.html",{"all_author":all_author})

def author_add(request):
    error = ""
    if request.method == "POST":
        author_name = request.POST.get("author_name")
        print(author_name)
        if not author_name:
            error = "作者姓名不能为空！"
        elif models.Author.objects.filter(name = author_name):
            error = "作者已存在！"
        else:
            models.Author.objects.create(name = author_name)
            return redirect("/author_list/")
    return render(request,"author_add.html",{"error":error})

def author_del(request):
    pk = request.GET.get("pk")
    print(pk)
    models.Author.objects.filter(pk=pk).delete()
    all_author = models.Author.objects.all()
    return render(request,"author_list.html",{"all_author":all_author})

def author_edit(request):
    error = ""
    pk = request.GET.get("pk")
    if request.method == "POST":
        author_name = request.POST.get("author_name")
        if not author_name:
            error = "作者姓名不能为空！"
        elif models.Author.objects.filter(name = author_name):
            error = "作者姓名已存在！"
        else:
            models.Author.objects.filter(pk=pk)
            
            models.Author.objects.filter(pk=pk).update(name = author_name)
            return redirect("/author_list/")
    auhtor = models.Author.objects.get(pk=pk)
    return render(request,"author_edit.html",{"author":auhtor,"error":error})


def serach(request):
    search = request.POST.get("search_for")
    
    book_found = models.Book.objects.filter(name = search)
    author_found = models.Author.objects.filter(name = search)
    publisher_found = models.Publisher.objects.filter(name = search)

    return render(request,"search.html",{"bf":book_found,"af":author_found,"pf":publisher_found})

def book_det(request):
    pk = request.GET.get("pk")
    book_obj = models.Book.objects.get(pk=pk)
    return render(request,"book_det.html",{"book_obj":book_obj})

