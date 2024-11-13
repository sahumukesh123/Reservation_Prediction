from flask import Flask, render_template, request
import pickle

# load the model
with open("rf_model.pkl", "rb") as file:
    model = pickle.load(file)

# create the server
app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return render_template("form.html")


@app.route("/predict", methods=["POST"])
def predict():
    no_of_adults = int(request.form.get("no_of_adults"))
    no_of_children = int(request.form.get("no_of_children"))
    no_of_weekend_nights = int(request.form.get("no_of_weekend_nights"))
    no_of_week_nights = int(request.form.get("no_of_week_nights"))
    required_car_parking_space = int(request.form.get("required_car_parking_space"))
    lead_time = int(request.form.get("lead_time"))
    repeated_guest = int(request.form.get("repeated_guest"))
    no_of_previous_cancellations = int(request.form.get("no_of_previous_cancellations"))
    no_of_previous_bookings_not_canceled = int(request.form.get("no_of_previous_bookings_not_canceled"))
    avg_price_per_room = float(request.form.get("avg_price_per_room"))
    no_of_special_requests = int(request.form.get("no_of_special_requests"))
    type_of_meal_plan_encoded = int(request.form.get("type_of_meal_plan_encoded"))
    room_type_reserved_encoded = int(request.form.get("room_type_reserved_encoded"))
    market_segment_type_encoded = int(request.form.get("market_segment_type_encoded"))
    arrival_month_encoded = int(request.form.get("arrival_month_encoded"))

    x = [no_of_adults,
         no_of_children,
         no_of_weekend_nights,
         no_of_week_nights,
         required_car_parking_space,
         lead_time,
         repeated_guest,
         no_of_previous_cancellations,
         no_of_previous_bookings_not_canceled,
         avg_price_per_room,
         no_of_special_requests,
         type_of_meal_plan_encoded,
         room_type_reserved_encoded,
         market_segment_type_encoded,
         arrival_month_encoded]

    # predict the outcome

    #if predictions1 == 0:
    #    return f"The Customer will cancel the reservation"
    #else:
    #   return f"The Customer will not cancel the reservation"

    return render_template(
        "prediction_result.html",
        predictions1=model.predict([x]))


# start the server
app.run(port=4000, host="0.0.0.0", debug=True)
