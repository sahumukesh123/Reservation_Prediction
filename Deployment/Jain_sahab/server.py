from flask import Flask, request, render_template

import pickle

# load the model
with open('lg.pkl','rb') as file:
    model_lg = pickle.load(file)

with open('svm.pkl','rb') as file:
    model_svm = pickle.load(file)

with open('dt.pkl','rb') as file:
    model_dt = pickle.load(file)

with open('rf.pkl','rb') as file:
    model_rf = pickle.load(file)

with open('xgb.pkl','rb') as file:
    model_xgb = pickle.load(file)

# create the server
app = Flask(__name__)

@app.route('/',methods=['GET'])
def root():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    # get input from user

    City = float(request.form.get("City"))
    Target = float(request.form.get("Target"))
    BattingTeam = float(request.form.get("BattingTeam"))
    Runs_required = float(request.form.get("Runs_required"))
    Balls_left = float(request.form.get("Balls_left"))
    Current_runrate = float(request.form.get("Current_runrate"))
    Required_runrate = float(request.form.get("Required_runrate"))
    Wicket_left = float(request.form.get("Wicket_left"))
    BowlingTeam = float(request.form.get("BowlingTeam"))
 

    algo = request.form.get("algo")
    x = [City, Target, BattingTeam, Runs_required,Balls_left,  Current_runrate, Required_runrate,Wicket_left,BowlingTeam]
    if algo == 'svm':
        prediction = model_svm.predict([x])
    elif algo == 'dt':
        prediction = model_dt.predict([x])
    elif algo == 'rf':
        prediction = model_rf.predict([x])
    elif algo == 'lg':
        prediction = model_lg.predict([x])
    elif algo == 'xgb':
        prediction = model_xgb.predict([x])

    return render_template(
        "result.html",
        prediction=prediction[0],
        City=City,Target=Target,BattingTeam=BattingTeam,Runs_required=Runs_required,Balls_left=Balls_left,Current_runrate=Current_runrate,Required_runrate=Required_runrate,Wicket_left=Wicket_left,BowlingTeam=BowlingTeam,algo=algo)


# start the server
app.run(port=4006,debug=True,host='0.0.0.0')
