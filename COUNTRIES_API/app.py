from flask import Flask, request, jsonify
import json
app = Flask(__name__)
json_file = open('C:\\Users\\DELL\\PycharmProjects\\pythonProject\\COUNTRIES_API\\countries.json', 'r',
                encoding='utf-8')



@app.route('/countries', methods=['GET'])
def all_countries():


    data = json_file.read()

    json_dump = json.dumps(data)
    return json_dump

#json_data = json_file.read()
#obj = json.loads(json_data)
#list = obj['country']

@app.route('/country', methods=['GET'])
def only_country():
    data = json_file.read()
    json_dump = json.dumps(data)
    for country in data['country']:


    return json_dump



if __name__ == "__main__":
    app.run(debug=True)
