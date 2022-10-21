import speech_recognition as sr

# Initializing recognizer class for recognizing the speech
recognize = sr.Recognizer()

#using Microphone as source to read speech
with sr.Microphone() as source:
    print("Speak Something..")
    aud_text = recognize.listen(source) #using recognizer, listening to the speech and storing it into a variable
    print("Analyzing your speech, Just a sec!")

    try:
        #using google speech recognition 
        print("Here is the Text: " +recognize.recognize_google(aud_text))
    except:
        print("Oops Something went Wrong, Please speak Again")





