import json
from datetime import datetime

def show_title_card():
    # Using raw strings (r"") so the backslashes format perfectly without escaping
    title = r"""
           |                                                                                  |>
          -+-                                                                                 |
         /   \                                                                              |/\/\|
        /_____\                _______________________________________________________      | || |
       |==_==_==|             |                                                       |     | || |
       | ( o )  |             |     _   ___    _  _  ___  _  _  ___  ___    ___  ___  |     | || |
       |========|             |    /_\ |_ _|  | || |/ _ \| || |/ __|| __|  / _ \| __| |     | || |
       | ||  || |             |   / _ \ | |   | __ | (_) | \/ |\__ \| _|  | (_) | _|  |     | || |
       | ||  || |             |  /_/ \_\___|  |_||_|\___/ \__/ |___/|___|  \___/|_|   |     | || |
       | ||  || |             |                                                       |     | || |
       | ||  || |             |       ___  ___  __  __  __  __  ___  _  _  ___        |     | || |
       | ||  || |             |      / __|/ _ \|  \/  ||  \/  |/ _ \| \| |/ __|       |     | || |
       | ||  || |             |     | (__| (_) | |\/| || |\/| | (_) | .` |\__ \       |     | || |
       | ||  || |             |      \___|\___/|_|  |_||_|  |_|\___/|_|\_||___/       |     | || |
       | ||  || |             |_______________________________________________________|     | || |
       | ||  || |               /||\ /||\ /||\ /||\ /||\ /||\ /||\ /||\ /||\ /||\           | || |
      /| ||  || |\              |||| |||| |||| |||| |||| |||| |||| |||| |||| ||||          /| || |\
     /_|_||__||_|_\=============||||=||||=||||=||||=||||=||||=||||=||||=||||=||||=========/_|_||_|_\
    ___|_||__||_|_|_____________||||_||||_||||_||||_||||_||||_||||_||||_||||_||||_________|_|_||_|_|___
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~
    ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~
      ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ .by Luca Tilyard.
"""
    # Print in bright green for a classic terminal look
    print("\033[92m" + title + "\033[0m")
    print("=" * 100)
    print("  Type 'Exit' to adjourn, or type a motion to debate...".center(100))
    print("=" * 100)
    print("\n")

def parse_response(response, is_END=False):

    # Parse the string into a Python dictionary
    response_JSON = json.loads(response)

    if isinstance(response_JSON, list):
        response_JSON = response_JSON[0]

    with open("Debate_logs/Entire_log.txt", "a", encoding="utf-8") as file:
        file.write("\n" + response + "\n")

    with open("Debate_logs/Transcript.txt", "a", encoding="utf-8") as file:
        file.write("\n" + response_JSON["user_id"] + ": " + response_JSON["speech"] + "\n")

    if response_JSON["user_id"] == "SPK":
        return response_JSON["speech"]

    if is_END:
        return response_JSON["speech"]
    
    return 1

def initaliseTranscript():
    with open("Debate_logs/Transcript.txt", "w", encoding="utf-8") as file:
        file.write("TRANSCRIPT BEGIN \n \n Question from citizens: ")