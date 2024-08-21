from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import os

class ActionInquireHiringPolicy(Action):
    def name(self) -> str:
        return "action_inquire_hiring_policy"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Define the path to the text file
        file_path = "ncrtc_hiring_policy.txt"

        # Check if the file exists
        if not os.path.exists(file_path):
            dispatcher.utter_message(text="Sorry, the hiring policy file is not available.")
            return []

        try:
            # Open the text file and read the hiring policy section
            with open(file_path, "r") as file:
                policy_text = file.read()

            # Extract the specific hiring policy section
            hiring_policy = self.extract_hiring_policy(policy_text)

            if hiring_policy:
                # Respond with the hiring policy details
                dispatcher.utter_message(text=f"Here is the information on our hiring policy: {hiring_policy}")
            else:
                dispatcher.utter_message(text="Sorry, I could not find the hiring policy information.")
        
        except Exception as e:
            dispatcher.utter_message(text=f"An error occurred: {str(e)}")

        return []

    def extract_hiring_policy(self, policy_text: str) -> str:
        # Logic to extract the hiring policy section
        start = policy_text.find("Hiring Policy:")
        end = policy_text.find("Leave Policy:")  # Assuming Leave Policy follows Hiring Policy

        if start == -1:
            return None

        if end == -1:
            end = len(policy_text)  # If "Leave Policy:" is not found, read till the end

        return policy_text[start:end].strip()

