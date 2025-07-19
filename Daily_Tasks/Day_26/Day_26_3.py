# SHA 265 --> Secure Hash Implementation
# ENCRYPTION 

from Day_26_1 import MongoDBHelper
from Day_26_2 import User

def main():
    db_helper = MongoDBHelper()
    db_helper.select_db(db_name='Agentic_AI',collection = 'training')

    user = User()
    user.input_user_details()
    user.show()

    result = db_helper.insert(document=user.to_document())
    print('User Saved in MongoDB with _id as : ', result.insert_id)


if __name__ == 'main':
    main()
