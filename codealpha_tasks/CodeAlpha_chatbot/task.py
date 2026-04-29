def chatbot():
    while True:
        user=input("you: ").lower().strip()
        if user in ["hello","hi","hlo"]:
            print("bot:hi")
        elif user=="how are you":
            print("bot:I'm fine,thanks!")
        elif user=="bye":
            print("bot:Goodbye!")
            break
        elif user=="":
            print("bot:please say something")
            
        else:
            print("bot:I don't understand")
            
chatbot()