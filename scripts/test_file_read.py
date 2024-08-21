file_path = "/Users/avirajahalawat/Desktop/rasa_project/rasa_project/ncrtc_hiring_policy.txt"

try:
    with open(file_path, "r") as file:
        policy_text = file.read()
    print("File content read successfully:")
    print(policy_text)
except Exception as e:
    print(f"Error reading file: {e}")

