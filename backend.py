import numpy as np
from crypt import methods
from pyexpat import model
from flask import Flask, app, render_template, url_for, request
import pickle

def pre_process(x):
    x['gender']= x['gender'].replace('male', 1)
    x['gender']= x['gender'].replace('female', 0)
    x['smoke']= x['smoke'].replace('No', 0)
    x['smoke']= x['smoke'].replace('Yes', 1)
    x['alco']= x['alco'].replace('No', 0)
    x['alco']= x['alco'].replace('Yes', 1)
    x['active']= x['active'].replace('No', 0)
    x['active']= x['active'].replace('Yes', 1)
    return x


def load_model(x):
    model= pickle.load(open('finalized_model.sav', 'rb'))
    out= model.predict(np.array(x), np.reshape(1, -1))
    return out(0)

app = Flask(__name__, template_folder='D:\Edu\Statistics\Statistics Project\Biostatistics_project-master\Biostatistics_project-master\Biostatistics\index1.html')

@app.route('/', methods=["GET"])
def inder():
    return render_template('index1.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request == "POST":
        f = request.file['file']
        x = pre_process(f)
        out = load_model(x)
        if out == 0 :
            return "Negative"
        else:
            return "Positive"
    return None



if __name__  == '__main__' :
    app.run(debug=True)