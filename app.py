from flask import Flask, request, render_template, redirect, url_for
import sklearn
import pickle
app = Flask(__name__)

List = ['Resale', 'MaintenanceStaff', 'Gymnasium',
       'ShoppingMall', 'Intercom', 'SportsFacility', 'ATM', 'School',
       'PowerBackup', 'StaffQuarter', 'Cafeteria', 'WashingMachine',
       'Gasconnection', 'AC', 'Wifi', 'BED', 'Microwave', 'GolfCourse',
       'Wardrobe']
# one-hot function
def compare_lists(List, Input):
    Output = []
    for item in List:
        if item in Input:
            Output.append(1)
        else:
            Output.append(0)
    return Output


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print('test1')
        return redirect(url_for('home'))
    return redirect(url_for('index'))

@app.route('/home', methods=['POST', 'GET'])
def home():
    print('test2')
    if request.method == 'POST':
        entry = dict(request.form)
        print(entry)
        entries = request.form.getlist('amenities')
        checkbox_inputs = compare_lists(List,entries)
        area_input = int(request.form.get('Area'))
        location_input = int(request.form.get('location'))
        features = [[location_input,area_input] + checkbox_inputs]
        print(features)
        lr = pickle.load(open('house_pricehyd.pkl','rb'))
        prediction = round(lr.predict(features)[0])
        lb = prediction - 1800000
        ub = prediction + 1800000 
        return render_template('prediction.html', prediction=prediction)
    return render_template('mainpage.html')    

