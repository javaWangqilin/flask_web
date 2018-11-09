# coding:utf-8
from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
import os
import time

app=Flask(__name__)

@app.route('/upload2',methods=['POST','GET'])
def upload_file(request):
    if request.method == "POST":  # 请求方法为POST时，进行处理
        myFile = request.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")
        destination = open(os.path.join("static\\uploads", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        return HttpResponse(myFile.name)
    return render_template('upload2.html')
if __name__=='__main__':
    app.run(debug=True)

