## story_00000000
* greet
 - utter_greet
 - utter_default
 - utter_ask_howcanhelp
* inform{"make_appointment": "True"}
 - utter_on_it
 - utter_ask_details
* inform{"contact_name": "Nikhil", "contact_age": "26", "contact_gender": "Male", "contact_phone": "1234567890"}
 - utter_on_it
 - utter_ask_institution
* inform{"institution_type":"hospital"}
 - utter_on_it
 - utter_ask_location
* inform{"location_institution":"Paderborn"}
 - utter_on_it
 - utter_askdate_and_time
* inform{"date":"28 May", "time": "10 AM"}
 - utter_on_it
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
* affirm
 - utter_ack_makeappointment
* thankyou
 - utter_goodbye

## story_00000001
* greet
 - utter_default
 - utter_ask_howcanhelp
* get_diagnose
 - utter_on_it
 - utter_ask_symptoms
* inform{"symptom1": "fever", "symptom2": "stomach aches", "symptom3": "sore muscles"}
 - utter_on_it
 - utter_ask_details
* inform{"contact_name": "Utsav", "contact_age": "26", "contact_gender": "Male", "contact_phone": "45221330034"}
 - utter_on_it
 - action_analyse_symptoms
* affirm
 - action_greet_user
* thankyou
 - utter_goodbye


## story_000000002
* greet
 - utter_greet
 - utter_howcanhelp
* make_appointment
 - utter_ask_date_and_time
* inform{"date":"25.03", "time":"2pm"}
 - utter_on_it
 - utter_ask_details
* inform{"contact_name": "John", "contact_age": "26", "contact_gender": "Male", "contact_phone": "445623167892"}]
 - utter_ask_location
* inform{"contact_location":"Aachen"}
 - utter_ask_institution
* inform{"institution_type":"pharmacy"}
 - utter_on_it
 - action_search_institution
 - action_make_appointment
* affirm
* request_info
 - utter_give_info_institution
* affirm
 - utter_goodbye
