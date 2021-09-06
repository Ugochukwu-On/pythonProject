from flask import Flask,jsonify
import json
app = Flask(__name__)
json_file = open('C:\\Users\\DELL\\PycharmProjects\\pythonProject\\COUNTRIES_API\\countries.json', 'r',
                encoding='utf-8')
'''
The App would be read from a json file

The API would be able to get infromation from the json file with endpoints
Example:
    GET/all- Get all data in the json file
    GET/countries - to get only the countries in the json file
    GET/country/states - to get all the states of all countries
    GET/countries/Country- to get all the states i a country
'''


@app.route('/all', methods=['GET'])


def all_countries():


    data = json_file.read()

    json_dump = json.dumps(data)
    return json_dump, 200



@app.route('/countries', methods=['GET'])
def only_country():
    data = json_file.read()
    object = json.loads(data)
    location = []

    for places in object["countries"]:
        x = places["country"]
        location.append(x)
        print(location)

    return jsonify(location), 200

@app.route('/country/states', methods=['GET'])
def states():
    data = json_file.read()
    object = json.loads(data)
    location = []

    for places in object["countries"]:
        x = places["states"]
        location.append(x)
        print(location)

    return jsonify(location), 200

@app.route('/countries/<CountryName>', methods=['GET'])
def only_states(CountryName):
    json_file = open('C:\\Users\\DELL\\PycharmProjects\\pythonProject\\COUNTRIES_API\\countries.json', 'r',
                     encoding='utf-8')
    data = json_file.read()
    object = json.loads(data)
    for places in object["countries"]:
        y = places.get("country")
        if y == CountryName:
            x = places.get("states")
            print(x)
    return jsonify(CountryName), 200


if __name__ == "__main__":
    app.run(debug=True)
