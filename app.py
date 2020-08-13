# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 09:45:35 2020

@author: malat
"""


from flask import Flask , request , render_template

app = Flask(__name__)

def cal(w,h):
    return round(w / ((h/100) ** 2),2)




@app.route("/", methods=['GET', 'POST'])
def home():
    bmi = ""
    if request.method == "POST" and "weight" in request.form:
        weight= float(request.form.get("weight"))
        height= float(request.form.get("height"))
        bmi = cal(weight,height)
    return render_template("index.html", 
                           bmi= bmi)

if __name__ == '__main__':
    app.run()


