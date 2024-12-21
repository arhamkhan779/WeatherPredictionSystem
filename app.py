from flask import Flask,render_template,redirect,Response,url_for,request
import joblib
import pandas as pd

model=joblib.load("artifacts\\training\\model.pkl")
input_processor=joblib.load("artifacts\\data_preprocessing\\input_processor.pkl")
app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/rainy')
def rainy():
    return render_template("rainy.html")

@app.route('/sunny')
def sunny():
    return render_template("sunny.html")

@app.route('/submit',methods=["GET","POST"])
def submit():
    classes=["sunny","rainy"]
    if request.method == "POST":
        min_temp=request.form['MinTemp']
        max_temp=request.form['MaxTemp']
        wind=request.form['WindSpeed']
        data=[[min_temp,max_temp,wind]]
        input=input_processor.transform(data)
        y_pred_prob = model.predict_proba(input)[:, 1]  
        y_pred_binary = (y_pred_prob >= 0.5).astype(int)  
        prediction=classes[y_pred_binary[0]]
    
    return redirect(url_for(prediction))


if __name__ == "__main__":
    app.run(debug=True)