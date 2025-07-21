# CLASS - DB CONTROLLER 

"""
MongoDB Helper

    Database contain Collections
    Collection which contains documents

        Document : Dictionary

        User : name, phone, email, age, gender etc
        Address : adrsLine, city, state, pincodr

        User has an address
        User can have 1 address
        User can have many addresses

    2 Techniques are there :

       1. Refrential Technique

       collection1: users
       {
            '_id' : 'tfghfcgvh345678hashd',
            'name' : 'John Watson'
            etc

            'address_id' : 'gfd654ewqfygv',
       }

       collection2: addresses
       {
            '_id' : 'gfd654ewqfygv',
            'adrsLine' : 'Redwood Shores',
            'city' : 'Ludhiana'
            etc

            'user_id' : 'tfghfcgvh345678hashd',
       }

LOOSE COUPLING : USER AND ADDRESS ARE SAVED DIFFERENTLY AND THEY HAVE REFRENCE SAVED INSIDE THEM

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   
     2. Containerized Technique   (TIGHT COUPLING)

     collection1: users
       {
            '_id' : 'tfghfcgvh345678hashd',
            'name' : 'John Watson'
            etc
       }

       collection2: addresses
       {
            '_id' : 'gfd654ewqfygv',
            'adrsLine' : 'Redwood Shores',
            'city' : 'Ludhiana'
            etc
       }

 # ONE USER CAN HAVE MANY ADDRESSES (LIST OF DICTIONARIES )

    'addresses' : [

        {
                'adrsLine' : 'Redwood Shores',
                'city' : 'Ludhiana'
        }

        {
                'adrsLine' : 'Redwood Shores',
                'city' : 'Jalandhar'
        }

    ]



########## WE HAVE TO CHECK IN CONTAINERIZATION, THERE IS A FIX LIMIT (SIZE OF DOCUMENT IS FIXED AND LESS ALSO) 
"""