from flask import Flask, request, jsonify
import json
app = Flask(__name__)
json_file = open('C:\\Users\\DELL\\PycharmProjects\\pythonProject\\COUNTRIES_API\\countries.json', 'r',
                encoding='utf-8')
'''
The App would be read from a json file

The API would be able to get infromation from the json file with endpoints
Example:
    GET/all- Get all data in the json file
    GET/country - to get only the countries in the json file
    GET/country/states - to get all the states of all countries
'''


@app.route('/all', methods=['GET'])


def all_countries():


    data = json_file.read()

    json_dump = json.dumps(data)
    return json_dump



@app.route('/country', methods=['GET'])
def only_country():
    data = json_file.read()
    object = json.loads(data)
    location = []

    for places in object["countries"]:
        x = places["country"]
        location.append(x)
        print(location)

    return jsonify(location), 201

@app.route('/country/states', methods=['GET'])
def only_states():
    data = json_file.read()
    object = json.loads(data)
    location = []

    for places in object["countries"]:
        x = places["states"]
        location.append(x)
        print(location)

    return jsonify(location), 201




if __name__ == "__main__":
    app.run(debug=True)
