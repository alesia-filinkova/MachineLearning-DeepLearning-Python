from flask import Flask, jsonify, request

app = Flask(__name__)

weather_data = {
    "new york": {"temperature": 22, "condition": "Sunny"},
    "london": {"temperature": 15, "condition": "Cloudy"},
    "tokyo": {"temperature": 28, "condition": "Clear"},
    "sydney": {"temperature": 18, "condition": "Rainy"}
}

@app.route('/')
def home():
    return jsonify({"message": "Welcome to MINI Weather API"})

@app.route('/weather', methods=['GET'])
def get_all_weather():
    return jsonify(weather_data)

@app.route('/weather/<city>', methods=['GET'])
def get_weather_by_city(city):
    city = city.lower()
    if city in weather_data:
        return jsonify({city: weather_data[city]})
    return jsonify({"error": "City not found"}), 404

@app.route('/weather', methods=['POST'])
def add_city_weather():
    data = request.json
    city = data.get("city", '').lower()
    temperature = data.get("temperature")
    condition = data.get("condition")
    
    if not city or not temperature or not condition:
        return jsonify({"error": "Missing city name or temperature or condition"}), 400
    
    weather_data[city] = {"temperature": temperature, "condition": condition}
    return jsonify({"message": f"weather to {city} was added successfully"}), 201

if __name__ == "__main__":
    app.run(debug=True)