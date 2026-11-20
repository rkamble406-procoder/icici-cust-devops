from fastapi import FastAPI
app= FastAPI()

@app.get("/home")

def WelcomePrompt():
    return {"message" :  "Welcome to ICICI Bank - TSG 6"  }

@app.get("/login")

def LoginPage():
    return {"message" :  "Welcome to Login Page of ICICI Bank - TSG 6"  }




     

