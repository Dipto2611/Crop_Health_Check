##  How to Run the Project

Follow the steps below to set up and run the application locally:

# 1. Clone the repository:
[bash]
- git clone https://github.com/Dipto2611/Crop_Health_Check.git
- cd Crop_Health_Check

# 2. Create a virtual environment:

- python -m venv .venv
- source .venv/bin/activate (Linux)      # On Windows use: .venv\Scripts\activate

# 3. Install required dependencies:

- pip install -r requirements.txt

# 4. Ensure the trained model file is present at:

- model/model.h5

# 5. Run the application:

- python app.py

# 6. Open your browser and go to:

- http://127.0.0.1:5000

Upload a plant leaf image and the system will predict whether it is Healthy or Diseased in real time.

