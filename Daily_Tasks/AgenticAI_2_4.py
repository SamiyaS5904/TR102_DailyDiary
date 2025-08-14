# AI RESPONSE FUNCTION
from openai import OpenAI

def ai_response(user_message):
    tools = [
        {
            "type" : "function",
            "name" : "add_patient",
            "description" : "Add a new patient in the system in  MongoDB",
            "parameters" : {
                "type" : "object",
                "properties" : {

                    "name" : {"type" : "string"}
                    "phone" : {"type" : "string"}
                    "email" : {"type" : "string"}
                    "gender" : {"type" : "string"}
                    "age" : {"type" : "int"}
                    "symptoms" : {"type" : "string"}

                "required" : [
                    "name", "phone"
                ],
                "additionalProperties" : False
            }
        }   
        },


        {
            "type" : "function",
            "name" : "save_consultation",
            "description" : "Add a new Consultation of the patint in MongoDB",
            "parameters" : {
                "type" : "object",
                "properties" : {

                    "name" : {"type" : "string"}
                    "phone" : {"type" : "string"}
                    "email" : {"type" : "string"}
                    "gender" : {"type" : "string"}
                    "age" : {"type" : "int"}
                    "symptoms" : {"type" : "string"}

                "required" : [ "name", "phone","email", "gender", "age"],
                "additionalProperties" : False
            }
        }   
        },
    ]

    OPEN_AI_KEY = ""

    selected_model ='gpt-4o-mini'
    client = OpenAI(api_key=OPEN_AI_KEY)

    response = client.responses.create(
        model=selected_model,
        input=[
            {"role" : "system", "content" : "You are a Doctor Agent who can create consulations in DB"}]
            {"role" : "user", "content" : user_message}
            ]
    tools = tools
        )
        print(response.output_text)
    