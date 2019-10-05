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

message_count = 0
file_name = "error"

for chat in chats:
     url = chat + '/message_1.json'
     json_data = get_json_data(chat)
     if json_data != None:
         messages = json_data["messages"]
         my_responses = 0
         for message in messages:
             if message['sender_name'] == "Carter Hartmann":
                my_responses +=1
                convo = json_data["participants"]
         if my_responses > message_count:
            file_name = str(convo)
            message_count = my_responses
print(file_name)



# open all Messages
# go through each conversation
# count my responses for each conversation
# print the highest of those values
