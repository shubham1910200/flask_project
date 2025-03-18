from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# orrectly initializing MongoDB client
client = MongoClient("mongodb+srv://razzput19102000:1234@flask-app.t8hyb.mongodb.net/?retryWrites=true&w=majority&appName=Flask-app")

# Selecting database and collection
db = client["mydatabase"]  # Replace with your database name
collection = db["users"]  # Replace with your collection name

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.form.to_dict()  # Convert form data to dictionary
        collection.insert_one(data)  # Insert into MongoDB
        print(data)  # Debugging purpose
        return jsonify({'status': 'success', 'message': 'Form submitted successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/view', methods=['GET'])
def view():
    try:
        # ✅ Convert MongoDB cursor to a list of dictionaries
        vdata = list(collection.find({}, {"_id": 0}))  # Exclude ObjectId

        return jsonify({'status': 'success', 'data': vdata})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
