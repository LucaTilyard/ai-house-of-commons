import os
from dotenv import load_dotenv
from google import genai
import helpers
from google.genai import types

# Load environment variables from .env file
load_dotenv()

client = genai.Client()

model_selection = "gemini-3.5-flash-lite"

# Define reponse schema 
debate_schema = {
    "type": "OBJECT",
    "properties": {
        "user_id": {"type": "STRING"},
        "thoughts": {"type": "STRING"},
        "speech": {"type": "STRING"},
        "notes": {"type": "STRING"}
    },
    "required": ["user_id", "thoughts", "speech"]
}
# Parliment Structure: 

# Speaker of the House - Presides over debates, decide who speaks, ensures rules are followed, and maintains order.


# Prime Minister - Leader of the goverment, has the final say in decisions.
# Cabinet Ministers - Head various departments, provide advice and implement policies.

# Opposition leader - Leads the opposition party, challenges government policies and decisions.
# Opposition Members - Critique government policies, propose alternatives, and hold the government accountable.

# Load System prompts from text files
with open("Prompts/Speaker_of_the_House_system_instructions.txt", "r", encoding="utf-8") as file:
    speaker_instruction = file.read()

with open("Prompts/Prime_minister_system_instructions.txt", "r", encoding="utf-8") as file:
    prime_minister_instruction = file.read()

with open("Prompts/Opposition_leader_system_instructions.txt", "r", encoding="utf-8") as file:
    opposition_leader_instruction = file.read()


Speaker_of_the_House = client.chats.create(
    model=model_selection, 
    config={"system_instruction": speaker_instruction, 
            "temperature": 0.7, 
            "response_mime_type": "application/json", 
            "response_schema": debate_schema}
)

Prime_Minister = client.chats.create(
    model=model_selection, 
    config={"system_instruction": prime_minister_instruction, 
            "temperature": 0.7, 
            "response_mime_type": "application/json", 
            "response_schema": debate_schema}
)

Opposition_Leader = client.chats.create(
    model=model_selection, 
    config={"system_instruction": opposition_leader_instruction, 
            "temperature": 0.7, 
            "response_mime_type": "application/json", 
            "response_schema": debate_schema}
)

END_Flag = False
next_speaker = "SPK"


helpers.initaliseTranscript()
helpers.show_title_card()
question = input("Enter Prompt: ")

with open("Debate_logs/Transcript.txt", "a", encoding="utf-8") as file:
    file.write(question + "\n")

while not END_Flag:
    # Update transcript 
    with open("Debate_logs/Transcript.txt", "r", encoding="utf-8") as file:
        Transcript = file.read()

    if next_speaker == "SPK":
        response = Speaker_of_the_House.send_message(
            message=Transcript
        )
        response = helpers.parse_response(response.text)
        if response == "END":
            END_Flag = True
        next_speaker = response

    elif next_speaker == "PM1":
        print("Prime Minister is speaking...")
        response = Prime_Minister.send_message(
            message=Transcript
        )
        response = helpers.parse_response(response.text)
        next_speaker = "SPK"
        
    elif next_speaker == "OL1":
        print("Opposition Leader is speaking...")
        response = Opposition_Leader.send_message(
            message=Transcript
        )
        response = helpers.parse_response(response.text)
        next_speaker = "SPK"

# Prime minister concludes with answer.
response = Prime_Minister.send_message(
    message=Transcript
    )
response = helpers.parse_response(response.text, is_END=True)

print("Debate concluded. Final answer from Prime Minister: \n" + response)
