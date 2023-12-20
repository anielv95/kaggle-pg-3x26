from flask import Flask
from flask import request
from flask import jsonify

app = Flask("base-line-model")


@app.route("/predict", methods=["POST"])
def predict():
    input_var = request.get_json()

    # X = dv.transform([customer])
    # y_pred = model.predict_proba(X)[0, 1]
    # churn = y_pred >= 0.5

    result = {
        "id": input_var["id"],
        "Status_C": 0.628084,
        "Status_CL": 0.034788,
        "Status_D": 0.337128,
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9695)
