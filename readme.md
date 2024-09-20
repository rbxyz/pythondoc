# A typical integration of the Assistants API has the following flow:
- 1 - Create an Assistant by defining its custom instructions and picking a model. 
    If helpful, add files and enable tools like Code Interpreter, File Search, 
    and Function calling.
- 2 - Create a Thread when a user starts a conversation.
- 3 - Add Messages to the Thread as the user asks questions.
- 4 - Run the Assistant on the Thread to generate a response by calling the model and the tools.
