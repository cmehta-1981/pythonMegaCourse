date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10: ")
thought = input("lets your thoughts flow: ")

with open(f"files/{date}.txt", "w") as file:  # create & open the file from files directory
    file.write(mood + 2 * '\n')  # getting the text from mood variable & also next line times
    file.write(thought)  # getting the text from thought variable
