from flask import Flask, render_template, request
import os
import numpy as np
from tensorflow.keras.models import load_model
from utils.preprocess import preprocess_image

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load trained model
model = load_model("model/trained_model.h5")

# Labels must match training order
labels = ["Healthy", "Diseased"]

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    image_path = None

    if request.method == "POST":
        file = request.files["image"]

        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            processed = preprocess_image(filepath)
            pred = model.predict(processed)

            pred = np.asarray(pred)
            # If model was trained with a single-output sigmoid (binary), pred shape is (1,1)
            if pred.ndim == 2 and pred.shape[1] == 1:
                prob = float(pred[0][0])
                class_index = 1 if prob >= 0.5 else 0
                confidence = prob if class_index == 1 else 1.0 - prob
            else:
                class_index = int(np.argmax(pred, axis=1)[0])
                confidence = float(np.max(pred))

            predicted_class = labels[class_index]
            prediction = f"{predicted_class} ({confidence*100:.2f}%)"
            image_path = filepath

    return render_template(
        "index.html",
        prediction=prediction,
        image_path=image_path
    )

if __name__ == "__main__":
    app.run(debug=True)