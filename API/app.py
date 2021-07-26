from flask import Flask, request, jsonify

app = Flask(__name__)

Notes_list = [
    {
        "id": 0,
        "body": "This is an empty note",
    },
    {

        "id": 1,
        "body": "NOT EMPTY",
    },
    {
        "id": 2,
        "body": "Yesterday was a good day",
    },
    {
        "id": 3,
        "body": "Not everything Goes as planned, we try again?",
    },
]


@app.route('/Notes', methods=['GET', 'POST'])
def Notes():
    if request.method == 'GET':
        if len(Notes_list) > 0:
            return jsonify(Notes_list)
    else:
       return 'Nothing Found', 404

    if request.method == 'POST':
        new_body = request.form['body']
        iD = Notes_list[-1]['id'] + 1

        new_object = {
            'id': iD,
            'body': new_body,
        }
        Notes_list.append(new_object)
        return jsonify(Notes_list), 201

@app.route('/Notes/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_notes(id):
    if request.method == 'GET':
        for note in Notes_list:
            if note['id'] == id:
                return jsonify(note)
            pass
    if request.method == 'PUT':
        for note in Notes_list:
            if note['id'] == id:
                note['body'] = request.form['body']
                update_note = {
                    "id": id ,
                    "body": note['body']
                }
                return jsonify(update_note)
    if request.method == 'DELETE':
        for index, book in enumerate(Notes_list):
            if book['id'] == id:
                Notes_list.pop(index)
                return jsonify(Notes_list)


if __name__ == "__main__":
    app.run()