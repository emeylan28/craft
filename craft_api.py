from flask import Flask, jsonify, request
from craft_utils import find_all_crafts, find_craft_activity, find_crafty_item, add_new_craft, create_new_craft_table, new_craft_table_data, add_to_existing_craft_item, add_new_craft_item

app = Flask(__name__)

### Landing page ###

@app.route("/")
def get_landingpage():
    res = {"Landing":"Page"}
    return jsonify(res)

### Showing what the different craft options are ###

@app.route("/crafts/<activity_or_item>")
def get_crafts(activity_or_item):
    res = find_all_crafts(activity_or_item)
    return jsonify(res)

### Return the information with what the craft needs ###

@app.route("/crafts/craft_activity/<craft_activity>")
def get_craft_activity(craft_activity):
    res = find_craft_activity(craft_activity)
    return jsonify(res)

### Show the information about a particular item ###

@app.route("/crafts/craft_item/<craft_item>")
def find_craft_item(craft_item):
    res = find_crafty_item(craft_item)
    return jsonify(res)


### Add a new craft to the craft-type table ###

@app.route('/crafts', methods=['POST'])
def add_craft():
    craft_activity = request.get_json()
    res = add_new_craft(craft_activity)
    return jsonify(res)

### Create a new table for the new craft type ###

@app.route('/crafts/craft_activity', methods=['POST'])
def new_craft_table():
    craft_table = request.get_json()
    res = create_new_craft_table(craft_table)
    return jsonify(res)

### Adds information to the new craft table ###

@app.route('/crafts/craft_activity/item', methods=['PUT'])
def add_data():
    craft_data = request.get_json()
    res = new_craft_table_data(craft_data)
    return jsonify(res)

### Adds info about craft items to the relevant item table ###

@app.route('/crafts/craft_item', methods=['PUT'])
def add_craft_item():
    add_new_craft_item_to_table = request.get_json()
    res = add_to_existing_craft_item(add_new_craft_item_to_table)
    return jsonify(res)

### Adds new item to craft_items table ###

@app.route('/crafts/craft_item_table', methods=['PUT'])
def add_to_craft_items_table():
    new_item_for_craft = request.get_json()
    res = add_new_craft_item(new_item_for_craft)
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)