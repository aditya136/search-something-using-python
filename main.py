#imported wikipedia module that makes easy to access date/informations from wikipedias
import wikipedia

#imported the pyttsx3 module to convert texts to voice
import pyttsx3  


#made a variable & gave it a input() function which gonna take the search topic from the user
search = input("Search what you want: ")  

#here is the result variable which gonna store the informations taken from wikipedias through the module wikipedia
#the summary() function will collect a summary on the topic from wikipedias 
result = wikipedia.summary(search) 


#the print(result) gonna show the result
print(result)


#the variable voice will initialize the pyttsx3 module through the init() function
voice = pyttsx3.init()

#now the bulit in function say() from pyttsx3 toke an argument and says it through the computer's speacker
voice.say(result)

#the runAndWait() function commanded the code to wait till it ends the work of speech. After that, go to the next code/line 
voice.runAndWait()