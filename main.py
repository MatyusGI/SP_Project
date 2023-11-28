# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask,render_template,request
import pickle
import numpy as np
app = Flask(__name__, template_folder='templates')

model = pickle.load(open('model_svm.pkl','rb'))

@app.route('/')
def home():
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    return render_template('home.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    print(request.form)
    int_features = [float(x) for x in request.form.values()]
    final = [np.array(int_features)]
    print(final)
    # td = np.array([[0.5, 1., 1., 1., 0., 0.5, 1., 0.5, 0.5, 0.5, 0.5, 1., 0.,
    #                 1., 0., 1., 1., 1.]])
    prediction = model.predict(final)

    output = int(prediction)

    if output == 0:
        return render_template('home.html',
                               pred='Tidak Depresi atau Depresi Ringan')
    elif output == 1:
        return render_template('home.html',
                               pred='Depresi Sedang')
    else:
        return render_template('home.html',
                               pred='Anda Mengalami Depresi')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
