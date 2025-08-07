# AI RESPONSE FUNCTION

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
                    "location"
                ],
                "additionalProperties" : False
            }

        }
    ]