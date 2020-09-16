from django.shortcuts import render, redirect, HttpResponse
from myweb.models import User

# Create your views here.
from django.conf import settings
# 学号查询

login = False

def queryByid(request):
    id = request.POST.get('id')
    id_judge = User.objects.filter(id=id).exists()
    if id_judge == False:
        return render(request, "login.html")
    else:
        p1 = User.objects.get(id=id)
        changdi = request.POST.get('cd')
        jinchu = request.POST.get('jc')
    # 将数据发给页面
        context = {"p1": p1, "cd": changdi, "jc": jinchu}
        return render(request, "出.html", context)
# 打开查询
def openQuery(request):
    return render(request, "login.html")
# 页面查询
def queryUsers(request):

    if (request.POST.get('username1')=='admin' and request.POST.get('password1')=='dxg1999') :
        us = User.objects.all()
        # 将数据发给页面
        login = True
        context = {"ls": us, 'login': login}
        return render(request, "users.html", context)
    else:
        login = False
        context = {"login": login}
        return render(request, "users.html", context)

 #  添加数据
def openAdd(request):
    my_request = request
    status = referer_check(my_request)
    if status == False:
        return render(request, "login.html")
    else:
        return render(request, "userAdd.html")


# 保存数据
def saveUser(request):
    # 判断不合法操作
    my_request = request
    status = referer_check(my_request)
    if status == False:
        return render(request, "login.html")
    else:
        id = request.POST.get('id')
        username = request.POST.get('username')
        selfimg= request.POST.get('selfimg')
        code = request.POST.get('code')
        faculty = request.POST.get('faculty')
        User.objects.create(id=id, username=username, selfimg=selfimg, code=code, faculty=faculty)
        return redirect("/myweb/queryUsers/")

    # 打开修改页面


def openEdit(request):
    # 判断不合法操作
    my_request = request
    status = referer_check(my_request)
    if status == False:
        return render(request, "login.html")
    else:
        id = request.GET.get('id')
        # 到数据库查询用户信息
        m = User.objects.filter(id=id).first()
        # 将数据发给页面
        context = {"m": m}
        return render(request, "userEdit.html", context)

    # 更新数据


def updateUser(request):
    # 判断不合法操作
    my_request = request
    status = referer_check(my_request)
    if status == False:
        return render(request, "login.html")
    else:
        id = request.GET.get('id')
        username = request.GET.get('username')
        selfimg = request.GET.get('selfimg')
        code = request.GET.get('code')
        faculty = request.GET.get('faculty')
        User.objects.filter(id=id).update(username=username, selfimg=selfimg, code=code, faculty=faculty)
        return redirect("/myweb/queryUsers/")

  # 删除数据


def deleteUser(request):
    # 判断不合法操作
    my_request = request
    status = referer_check(my_request)
    if status == False:
        return render(request, "login.html")
    else:
        id = request.GET.get('id')
        User.objects.filter(id=id).delete()
        return redirect("/myweb/queryUsers/")


def openupLoad(request):
    # 判断不合法操作
    my_request = request
    status = referer_check(my_request)
    if status == False:
        return render(request, "login.html")
    else:
        return render(request, "upLoad.html")

# 上传图片
def upLoad(request):
    if request.method == "POST":  # 请求方法为POST时，进行处理
        myFile = request.FILES.get("picture", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("请选择需要上传的图片")
        destination = open("./static/img/" + myFile.name, "wb+")
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        return HttpResponse("上传成功!")

# 配置404,500
def page_not_found(request, exception):
    return render(request, "404.html")
def page_error(request):
    return render(request, "500.html")

# 判断referer是否存在
def referer_check(request):
    headers = request.headers
    if 'Referer' not in headers:
        status = False
        return status

