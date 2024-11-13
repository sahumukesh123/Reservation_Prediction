from flask import Flask, render_template, request
import pickle

# load the model
with open("rf.pkl", "rb") as file:
    model = pickle.load(file)

# create the server
app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return render_template("form.html")


@app.route("/predict", methods=["POST"])
def predict():
    no_of_adults = int(request.index.get("no_of_adults"))
    no_of_children = int(request.index.get("marketing"))
    no_of_weekend_nights = int(request.index.get("no_of_weekend_nights"))
    no_of_week_nights = int(request.index.get("no_of_week_nights"))
    lead_time = int(request.index.get("lead_time"))
    no_of_previous_cancellations = int(request.index.get("no_of_previous_cancellations"))
    no_of_previous_bookings_not_canceled = int(request.index.get("no_of_previous_bookings_not_canceled"))
    avg_price_per_room = float(request.index.get("avg_price_per_room"))
    no_of_special_requests = int(request.index.get("no_of_special_requests"))
    booking_status = int(request.index.get("booking_status"))
    
    
    
    

    # predict the outcome
    predictions1 = model.predictions
    return f"Final Classification = {predictions1}"


# start the server
app.run(port=4000, host="0.0.0.0", debug=True)
