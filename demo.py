# coding:utf-8

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app=Flask(__name__)
bootstrap=Bootstrap(app)

@app.route('/')
def demo():
    return render_template('demo.html',name='heh')

if __name__=='__main__':
    app.run(debug=True)

