from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from skinapp import dbconnection
from skinapp import predicts
from django.core.files.storage import FileSystemStorage
from datetime import date

# Create your views here.
def home(request):  
    return render(request,'index.html',{})

def predict(request): 
    if request.method=='POST':
        t=request.POST.get('t')
        up=request.FILES['up']
        fs=FileSystemStorage()
        filename=fs.save("skinapp/static/pic/"+up.name,up) 
        qry="INSERT INTO `dpic`(`tit`, `pic`) VALUES ('"+t+"','"+up.name+"')"
        dbconnection.insertdata(qry)
    qry1="select * from dpic order by id desc"
    data=dbconnection.selectalldata(qry1)
    return render(request,'predict.html',{'data':data})

def analysedata(request):  
    if(request.GET.get("pic")):
        pic=request.GET.get("pic") 
        import os
        from werkzeug.utils import secure_filename
        #from gevent.pywsgi import WSGIServer
        import numpy as np    
        basepath = os.path.dirname(__file__)        
        file_path = os.path.join(basepath, 'static\\pic', secure_filename(pic))  
        out=predicts.load_image(file_path) 
    return render(request,'analysedata.html',{'p':pic,'out':out})