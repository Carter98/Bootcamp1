# coded by Carter Hartmann
import json
import os
CURRENT_DIRECTORY = os.getcwd()
chats = os.listdir(CURRENT_DIRECTORY + "/messages/")
def get_json_data(chat):
    try:
        json_location = CURRENT_DIRECTORY + "/messages/" + chat + "/message_1.json"
        with open(json_location) as json_file:
            json_data = json.load(json_file)
            return json_data
    except IOError:
        pass # some things the directory aren't messages (DS_Store, stickers_used, etc.)


ttr = []
for chat in chats:
    url = chat + '/message_1.json'
    json_data = get_json_data(chat)
    print(chat)
    if json_data != None:
        messages = json_data["messages"]

        nur = 0
        last_response = 0
        multi_lockout = False
        found_a_name = False

        for message in messages:
            if message['sender_name'] == "Carter Hartmann":
                found_a_name = True
                multi_lockout = True
                last_response = message['timestamp_ms']
            else:
                if found_a_name:
                    if multi_lockout:
                        multi_lockout = False
                        ttr.append(last_response - message["timestamp_ms"])
holder = 0
for number in ttr:
    holder += number
holder = holder / len(ttr)
print(str(holder/1000/60/60) + " hours")
