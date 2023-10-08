from flask import Flask,render_template,request
import os
import numpy as np
import keras

# for pridiction function
def model_fun(path):
    project = keras.models.load_model('./model/model.h5')
    
    img = keras.utils.load_img(path,target_size=(150,150))
    img = keras.utils.img_to_array(img)/255
    img = np.expand_dims(img,axis=0)

    result = project.predict(img).round(3)
    pred = np.argmax(result)

    if pred==0:
        return 'Healthy Cotton Plant', 'health_burned_leaf.html'
    elif pred==1:
        return 'Disease Cotton Plant', 'disease.html'
    elif pred==2:
        return 'Healthy Cotton Plant', 'healthy.html'
    else:
        return 'Healthy Cotton Plant', 'healthy.html'
# for pridiction function

app = Flask(__name__,static_folder='static',template_folder='templates')

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/predict',methods=["POST"])
def pred():
    if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename

        if (len(filename) < 3):
            output_page='notfound.html'
            file_path = './static/img/f1.jpg'
        else:
            file_path = os.path.join('static/user-uploaded', filename)
            file.save(file_path)
        
            pred, output_page = model_fun(file_path)
            
    return render_template(output_page,user_uploaded = file_path)

    # return render_template('healthy.html')
# readme.md file
@app.route('/readme')
def readme():
    return render_template('readmi.html')











if __name__=="__main__":
    app.run(debug=False)