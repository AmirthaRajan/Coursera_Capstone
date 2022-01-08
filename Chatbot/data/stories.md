## story_1_chennai_chinese_low_response_email
* greet
    - utter_greet
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - utter_ask_location
* location{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"check_results": true}
    - slot{"ask_email":true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "phoenixprince15@gmail.com"}
    - slot{"email": "phoenixprince15@gmail.com"}
    - action_send_mail
* goodbye
    - utter_goodbye
    - action_restart

## story_2_bangalore_south_moderate_response_email
* greet
    - utter_greet
* location
    - utter_ask_location
* location{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - slot{"ask_email":true}
    - utter_ask_top10list
* email{"email": "phoenixprince15@gmail.com"}
    - slot{"email": "phoenixprince15@gmail.com"}
    - action_send_mail
    - action_restart

## story_3_allahabad_chinese_high_response_email    
* greet
    - utter_greet
* location
    - utter_ask_location
* location{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
    - slot{"ask_email":true}
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
    - action_restart
## story_4_kolkata_american_low_no_response_no_email
* greet
    - utter_greet
* location{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
* thank
    - utter_goodbye_no_result
    - action_restart
## story_5_ooty_south_high_response_no_email    
* greet
    - utter_greet
* location
    - utter_ask_location
* location{"location": "Ooty"}
    - slot{"location": "Ooty"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
    - slot{"ask_email":false}
* goodbye
    - utter_goodbye
    - action_restart
## story_6_mumbai_american_low_no_response_no_email
* greet
    - utter_greet
* location
    - utter_ask_location
* location{"location": "mubmai"}
    - slot{"location": "mubmai"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "mumbai"}
* affirm
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
* thank
    - utter_goodbye_no_result
    - action_restart
## story_7_chennai_mexican_moderate_no_response_no_email
* greet
    - utter_greet
* location
    - utter_ask_location
* location{"location": "chenai"}
    - slot{"location": "chenai"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "chennai"}
* affirm
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
* thank
    - utter_goodbye_no_result
    - action_restart
## story_8_japan_no_cuisine_no_price_no_response_no_email
* greet
    - utter_greet
* location
    - utter_ask_location
* location{"location": "japan"}
    - slot{"location": "japan"}
    - action_check_location
    - slot{"check_location": false}
* thank
    - utter_goodbye_no_result
    - action_restart
## story_9_chennai_south_high_response_no_email
* greet
    - utter_greet
* location
    - utter_ask_location
* location{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_10_delhi_north_moderate_response_no_email
* greet
    - utter_greet
* location{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_11_chandigarh_chinese_low_response_no_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_12_vizag_misspelled_north_high_response_email
* greet
    - utter_greet
* location{"location": "vizak"}
    - slot{"location": "vizak"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "vizag"}
* affirm
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price": "2000"}
    - slot{"price": "2000"}
    - action_check_price
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "phoenixprince15@gmail.com"}
    - slot{"email": "phoenixprince15@gmail.com"}
    - action_send_mail
    - action_restart

## story_13_Ghaziabad_misspelled_north_moderate_response_email
* greet
    - utter_greet
* location{"location": "Ghaziaba"}
    - slot{"location": "Ghaziaba"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "Ghaziabad"}
* affirm
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_14_Ranchi_misspelled_south_moderate_response_email
* greet
    - utter_greet
* location{"location": "Ranch"}
    - slot{"location": "Ranch"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "Ranchi"}
* affirm
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "above 300"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* email{"email": "phoenixprince15@gmail.com"}
    - slot{"email": "phoenixprince15@gmail.com"}
    - action_send_mail
    - action_restart

## story_15_Amritsar_misspelled_mexican_moderate_no_response_no_email
* greet
    - utter_greet
* location{"location": "Amirtsar"}
    - slot{"location": "Amirtsar"}
    - action_check_location
    - slot{"check_location": false}
* location{"location": "amristar"}
    - slot{"location": "amristar"}
    - action_check_location
    - slot{"check_location": false}
* location{"location": "Amritsar"}
    - slot{"location": "Amritsar"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price": "below 700"}
    - slot{"price": "moderate"}
    - action_check_price
    - slot{"price": "moderate"}
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_16_delhi_chinese_moderate_response_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price": "below 399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "below 399"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_price
    - slot{"price": "moderate"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "phoenixprince15@ymail.com"}
    - slot{"email": "phoenixprince15@ymail.com"}
    - action_send_mail
    - action_restart

## story_17_mumbai_italian_high_response_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "bombay", "price": "below 999"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - slot{"price": "below 999"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_price
    - slot{"price": "high"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "phoenixprince15@ymail.com"}
    - slot{"email": "phoenixprince15@ymail.com"}
    - action_send_mail
    - action_restart

## story_18_mumbai_misspelled_"italian_high_response_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "bombay", "price": "above 999"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - slot{"price": "above 999"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_price
    - slot{"price": "high"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "phoenixprince15@ymail.com"}
    - slot{"email": "phoenixprince15@ymail.com"}
    - action_send_mail
    - action_restart

## story_19_shimla_north_moderate_response_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "north-indian", "location": "shimla", "price": "greater than 500"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "shimla"}
    - slot{"price": "greater than 500"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_price
    - slot{"price": "moderate"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "amirtha-rajan.pks@live.com"}
    - slot{"email": "amirtha-rajan.pks@live.com"}
    - action_send_mail
    - action_restart
    
## story_20_Kanpur_misspelled_italian_low_no_response_no_email
* greet
    - utter_greet
* location{"location": "kanapur"}
    - slot{"location": "kanapur"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "Kanpur"}
* affirm
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - utter_ask_price
* restaurant_search{"price": "between 200 and 500"}
    - slot{"price": "between 200 and 500"}
    - action_check_price
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_21_Agraamerican_low_no_response_no_email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "Agra"}
    - slot{"location": "Agra"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - utter_ask_price
* restaurant_search{"price": "300"}
    - slot{"price": "300"}
    - action_check_price
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_22_nagpur_chinese_moderate_response_email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "nagpur"}
    - slot{"location": "nagpur"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "phoenixprince15@gmail.com"}
    - slot{"email": "phoenixprince15@gmail.com"}
    - action_send_mail
    - action_restart

## story_23_Guwahat_chinese_moderate_response_no_email
* greet
    - utter_greet
* restaurant_search{"price": "700"}
    - slot{"price": "700"}
    - action_check_price
    - slot{"price": "moderate"}
    - utter_ask_location
* location{"location": "Guwahat"}
    - slot{"location": "Guwahat"}
    - action_check_location
    - slot{"check_location": true}
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_24_Jaipur_chinese_high_response_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Jaipur"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Jaipur"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_check_price
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_25_Nashik_mexican_moderate_no_response_no_email
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - utter_ask_location
* location{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* restaurant_search{"price": "300"}
    - slot{"price": "300"}
    - action_check_price
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
* thank
    - utter_goodbye_no_result
    - action_restart

## story_26_puducherry_misspelled_south_moderate_no_response_no_email
* restaurant_search
    - utter_ask_location
* location{"location": "pondicherry"}
    - slot{"location": "pondicherry"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "puducherry"}
* affirm
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
* thank
    - utter_goodbye_no_result
    - action_restart

## story_27_Indore_american_high_no_response_no_email
* greet
    - utter_greet
* restaurant_search{"price": "high", "location": "Indore"}
    - slot{"location": "Indore"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_price
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
* thank
    - utter_goodbye_no_result
    - action_restart

## story_28_Mumbai_chinese_low_no_response_email
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai", "cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
* thank
    - utter_goodbye_no_result
    - action_restart

## story_29_goa_Mexican_mhigh_no_response_no_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "goa"}
    - slot{"cuisine": "Mexican"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - slot{"location": "goa"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
* thank
    - utter_goodbye_no_result
    - action_restart

## story_30_Varanasi_north_low_no_response_no_email
* restaurant_search{"price": "low", "cuisine": "north-indian", "location": "Varanasi"}
    - slot{"cuisine": "north-indian"}
    - slot{"location": "Varanasi"}
    - slot{"price": "low"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_price
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
* thank
    - utter_goodbye_no_result
    - action_restart

## story_31_surat_misspelled_italian_moderate_response_email
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - utter_ask_location
* location{"location": "Suret"}
    - slot{"location": "Suret"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "surat"}
* affirm
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine" : true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* email{"email": "amirtha-rajan.pks@geim.wolong.com"}
    - slot{"email": "amirtha-rajan.pks@geim.wolong.com"}
    - action_send_mail
    - action_restart


## Start with Goodbye
* goodbye
    - utter_goodbye
    - action_restart

## Start with Deny
* deny
    - utter_goodbye
    - action_restart


## story_32_location_invalid_rerun_right_location
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "madurai"}
    - slot{"location": "madurai"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "gurgaon"}
    - slot{"location": "gurgaon"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
* thank
    - utter_goodbye
    - action_restart

## story_34_location_invalid_deny_location_rerun
* greet
    - utter_greet
* location{"location": "Newyork"}
    - slot{"location": "Newyork"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* deny
    - utter_deny
    - utter_goodbye
    - action_restart

## story_35_location_valid_cuisine_valid_deny_email
* greet
    - utter_greet
* location{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price   
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_36_location_invalid_rerun_right_location_deny_mail
* greet
    - utter_greet
* location{"location": "india"}
    - slot{"location": "india"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "faridabad"}
    - slot{"location": "faridabad"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "ITALIAN"}
    - slot{"cuisine": "ITALIAN"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_37_location_out_of_scope_deny
* greet
    - utter_greet
* location{"location": "finland"}
    - slot{"location": "finland"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* deny
    - utter_deny
    - utter_goodbye
    - action_restart

<!-- location + cuisine-->
## story_39_location_cuisine_combined_price_valid_with_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "bhubaneshwar"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "bhubaneshwar"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "701"}
    - slot{"price": "701"}
    - action_check_price
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
* goodbye
    - utter_goodbye
    - action_restart

## story_40_location_cuisine_combined_price_valid_deny_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "Mangalore"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Mangalore"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "400"}
    - slot{"price": "400"}
    - action_check_price
    - slot{"price": "moderate"}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_41_location_valid_cuisine_invalid_retry_with_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "punjabi", "location": "Mysore"}
    - slot{"cuisine": "punjabi"}
    - slot{"location": "Mysore"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_rerun
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "500"}
    - slot{"price": "500"}
    - action_check_price
    - slot{"price": "moderate"}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## story_42_location_valid_cuisine_invalid_retry_deny_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "french", "location": "puducherry"}
    - slot{"cuisine": "french"}
    - slot{"location": "puducherry"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_rerun
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
* restaurant_search{"price": "550"}
    - slot{"price": "550"}
    - action_check_price
    - slot{"price": "moderate"}    
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_44_cuisine_invalid_retry_deny
* greet
    - utter_greet
* restaurant_search{"cuisine": "morocan", "location": "Aurangabad"}
    - slot{"cuisine": "morocan"}
    - slot{"location": "Aurangabad"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_rerun
* deny
    - utter_goodbye
    - action_restart

<!-- no greet, location + cuisine -->
## story_45_no_greet_location_cuisine_price_valid_deny_email
* restaurant_search{"cuisine": "north indian", "location": "varanasi"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "varanasi"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "600"}
    - slot{"price": "600"}
    - action_check_price
    - slot{"price": "moderate"}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_46_no_greet_location_cuisine_price_valid_with_email
* restaurant_search{"cuisine": "south indian", "location": "Nagpur"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Nagpur"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "200"}
    - slot{"price": "200"}
    - action_check_price
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
* goodbye
    - utter_goodbye
    - action_restart

## story_47_no_greet_location_cuisine_invalid_retry_no_email
* restaurant_search{"cuisine": "barbeque", "location": "Vadodara"}
    - slot{"cuisine": "barbeque"}
    - slot{"location": "Vadodara"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_rerun
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "MEXICAN"}
    - slot{"cuisine": "MEXICAN"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "1000"}
    - slot{"price": "1000"}
    - action_check_price
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_49_no_greet_location_valid_cuisine_invalid_retry_deny
* restaurant_search{"cuisine": "fast food", "location": "Amritsar"}
    - slot{"cuisine": "fast food"}
    - slot{"location": "Amritsar"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_rerun
* deny
    - utter_deny
    - utter_goodbye
    - action_restart

## story_50_no_greet_location_cuisine_invalid_retry_with_email
* restaurant_search{"cuisine": "mughlai", "location": "dehradun"}
    - slot{"cuisine": "mughlai"}
    - slot{"location": "dehradun"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_rerun
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

<!-- queries with cuisine only -->

<!-- start with greet, followed by question -->
## story_51_greet_cuisine_valid_with_email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "Vizag"}
    - slot{"location": "Vizag"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## story_52_greet_cuisine_valid_deny_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_location
* location{"location": "agra"}
    - slot{"location": "agra"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_53_greet_cuisine_invalid_retry_deny_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "rajastani"}
    - slot{"cuisine": "rajastani"}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_rerun
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": ">300"}
    - slot{"price": ">300"}
    - action_check_price
    - slot{"price": "moderate"}
    - utter_ask_location
* location{"location": "Vadodara"}
    - slot{"location": "Vadodara"}
    - action_check_location
    - slot{"check_location": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_54_greet_cuisine_invalid_retry_with_email
* restaurant_search{"cuisine": "Continental"}
    - slot{"cuisine": "Continental"}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_rerun
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_location
* location{"location": "kanpur"}
    - slot{"location": "kanpur"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## story_56_greet_cuisine_valid_location_invalid_retry_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_location
* location{"location": "newjersey"}
    - slot{"location": "newjersey"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "luckNow"}
    - slot{"location": "luckNow"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
* thank
    - utter_goodbye
    - action_restart

## story_57_Chennai_south_low_no_response_no_email
* restaurant_search{"cuisine": "south indian", "location": "Chennai", "price": "low"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Chennai"}
    - slot{"price": "low"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
* thank
    - utter_goodbye_no_result
    - action_restart

## story_58_bhopal_italian_moderate_response_email
* greet
    - utter_greet
* restaurant_search{"location": "bhopal", "price": "moderate"}
    - slot{"location": "bhopal"}
    - slot{"price": "moderate"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_price
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* email{"email": "phoenixprince15@gmail.com"}
    - slot{"email": "phoenixprince15@gmail.com"}
    - action_send_mail
    - action_restart

## story_59_hyderabad_misspelled_chinese_high_response_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_location
* location
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "hyderabad"}
* affirm
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_61_hyderabad_misspelled_american_moderate_no_response_no_email
* greet
    - utter_greet
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - utter_ask_location
* location
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "hyderabad"}
* affirm
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_62_Gangtok_American_moderate_no_response_no_email
* greet
    - utter_greet
* location{"location": "Hosur"}
    - slot{"location": "Hosur"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "Gangtok"}
    - slot{"location": "Gangtok"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart


## story_63_Ghaziabad_chinese_low_no_response_no_email
* greet
    - utter_greet
* restaurant_search{"price": "low", "location": "Ghaziabad"}
    - slot{"location": "Ghaziabad"}
    - slot{"price": "low"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_price
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
* thank
    - utter_goodbye_no_result
    - action_restart

## story_64_jaipur_misspelled_mexican_low_no_response_no_email
* greet
    - utter_greet
* restaurant_search{"price": "low", "cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "low"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - utter_ask_location
* location{"location": "jaipor"}
    - slot{"location": "jaipor"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "jaipur"}
* affirm
    - action_check_location
    - slot{"check_location": true}
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_65_Coimbatore_italian_high_no_response_no_email
* greet
    - utter_greet
* restaurant_search{"price": "high", "cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - slot{"price": "high"}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_rerun
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - utter_ask_location
* location{"location": "Coimbatore"}
    - slot{"location": "Coimbatore"}
    - action_check_location
    - slot{"check_location": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* email{"email": "amirtha-rajan.pks@capgemini.com"}
    - slot{"email": "amirtha-rajan.pks@capgemini.com"}
    - action_send_mail
    - action_restart

## story_67_Allahaba_american_moderate_response_no_email
* greet
    - utter_greet
* location{"location": "Allahaba"}
    - slot{"location": "Allahaba"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "allahabad"}
* affirm
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_68_indore_north_moderate_response_no_email
* greet
    - utter_greet
* restaurant_search{"price": "of 500"}
    - slot{"price": "of 500"}
    - action_check_price
    - slot{"price": "moderate"}
    - utter_ask_location
* location{"location": "indore"}
    - slot{"location": "indore"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_69_bangalore_invalid_italian_low_no_response_no_email
* greet
    - utter_greet
* restaurant_search{"price": "low", "cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - slot{"price": "low"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - utter_ask_location
* location{"location": "bangalure"}
    - slot{"location": "bangalure"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "bangalore"}
* location{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"check_location": true}
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
* thank
    - utter_goodbye_no_result
    - action_restart

## story_70_Nashik_American_high_response_email
* greet
    - utter_greet
* restaurant_search{"price": "high", "location": "Nashik"}
    - slot{"location": "Nashik"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_price
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "phoenixprince15@hotmail.com"}
    - slot{"email": "phoenixprince15@hotmail.com"}
    - action_send_mail
    - action_restart

## story_71_Mangalore_invalid_chinese_low_no_response_no_email
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - utter_ask_location
* location{"location": "Cuttack"}
    - slot{"location": "Cuttack"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "Mangalore"}
    - slot{"location": "Mangalore"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
* thank
    - utter_goodbye_no_result
    - action_restart
* greet
    - utter_greet
* location{"location": "Solapur"}
    - slot{"location": "Solapur"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* deny
    - utter_deny
    - utter_goodbye
    - action_restart

## story_72_chennai_invalid_american_low_no_response_no_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "price": "low"}
    - slot{"cuisine": "american"}
    - slot{"price": "low"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - utter_ask_location
* location{"location": "Vellore"}
    - slot{"location": "Vellore"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "chennei"}
    - slot{"location": "chennei"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "chennai"}
    - action_check_location
    - slot{"check_location": true}
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_74_faridabad_invalid_south_high_response_no_email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "rampur"}
    - slot{"location": "rampur"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "faridabad"}
    - slot{"location": "faridabad"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_75_Dehradun_south_high_no_response_no_email
- utter_ask_location
* location{"location": "Dehradun"}
    - slot{"location": "Dehradun"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "1500"}
    - slot{"price": "1500"}
    - action_check_price
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

<!-- ## story_76_chennai_invalid_chinese_low_response_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "madurai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "madurai"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "chennoi"}
    - slot{"location": "chennoi"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location": "chennai"}
* location{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* restaurant_search{"price": "1099"}
    - slot{"price": "1099"}
    - action_check_price
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* email{"email": "phoenixprince15@hotmail.com"}
    - slot{"email": "phoenixprince15@hotmail.com"}
    - action_send_mail
    - action_restart -->

## story_77_Noida_north_moderate_response_no_email
* greet
    - utter_greet
* location{"location": "Noida"}
    - slot{"location": "Noida"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "below 700"}
    - slot{"price": "below 700"}
    - action_check_price
    - slot{"price": "moderate"}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_79_Kolkata_invalid_south_low_no_response_no_email
* greet
    - utter_greet
* location{"location": "culcatta"}
    - slot{"location": "culcatta"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
* affirm
    - utter_goodbye_no_result
    - action_restart

## story_80_pune_invalid_south_low_no_response_no_email
* greet
    - utter_greet
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - utter_ask_location
* greet{"location": "puna"}
    - slot{"location": "puna"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "pune"}
* affirm
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
* thank
    - utter_goodbye_no_result
    - action_restart

## story_81_Bhopal_invalid_American_low_no_response_no_email
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - utter_ask_location
* location{"location": "chandigar"}
    - slot{"location": "chandigar"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "chandigarh"}
* deny
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "Bhopal"}
    - slot{"location": "Bhopal"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_82_noida_invalid_american_moderate_response_no_email
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_location
* location{"location": "mysor"}
    - slot{"location": "mysor"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "mysore"}
* deny{"location": "Mysore"}
    - slot{"location": "Mysore"}
    - utter_ask_location_rerun
* location{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_83_ooty_invalid_north_moderate_response_email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "Aagra"}
    - slot{"location": "Aagra"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "agra"}
* deny{"location": "agra"}
    - slot{"location": "agra"}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "ooty"}
    - slot{"location": "ooty"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "amirtharajanpks@gmail.com"}
    - slot{"email": "amirtharajanpks@gmail.com"}
    - action_send_mail
    - action_restart

## story_84_puducherry_italian_low_no_response_no_email
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - utter_ask_location
* location{"location": "delli"}
    - slot{"location": "delli"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "delhi"}
* deny
    - utter_ask_location_rerun
* location{"location": "puducherry"}
    - slot{"location": "puducherry"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_85_bangalore_invalid_south_low_no_response_no_email
* restaurant_search{"price": "low", "location": "bangaloru"}
    - slot{"location": "bangaloru"}
    - slot{"price": "low"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "mangalore"}
* location{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_price
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
* thank
    - utter_goodbye_no_result
    - action_restart

## story_87_Vizag_invalid_south_moderate_response_no_email
* greet
    - utter_greet
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - utter_ask_location
* location{"location": "nodia"}
    - slot{"location": "nodia"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "noida"}
* deny
    - utter_ask_location_rerun
* location{"location": "Vizag"}
    - slot{"location": "Vizag"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart


## story_88_greet_valid_cuisine_invalid_location_retry_deny_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_location
* location{"location": "thane"}
    - slot{"location": "thane"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "surat"}
    - slot{"location": "surat"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

<!-- no greet, start with cuisine -->
## story_89_no_greet_cuisine_valid_email
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_location
* location{"location": "Kochi"}
    - slot{"location": "Kochi"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## story_90_no_greet_cuisine_valid_no_email
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_location
* location{"location": "indore"}
    - slot{"location": "indore"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_91_no_greet_cuisine_invalid_retry_no_email
* restaurant_search{"cuisine": "arabian"}
    - slot{"cuisine": "arabian"}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_rerun
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_location
* location{"location": "Ahmedabad"}
    - slot{"location": "Ahmedabad"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_92_no_greet_cuisine_invalid_retry_email
* restaurant_search{"cuisine": "Lebanese"}
    - slot{"cuisine": "Lebanese"}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_rerun
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_location
* location{"location": "Guwahati"}
    - slot{"location": "Guwahati"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "abcd.abcd@yahoo.co.in"}
    - slot{"email": "abcd.abcd@yahoo.co.in"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## story_93_no_greet_cuisine_valid_location_invalid_retry_email
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_location
* location{"location": "akola"}
    - slot{"location": "akola"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "abcd@edu.in"}
    - slot{"email": "abcd@edu.in"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## story_95_no_greet_cuisine_valid_location_invalid_retry_no_email
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_location
* location{"location": "jhansi"}
    - slot{"location": "jhansi"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

<!-- queries with location only -->

<!-- start with greet, followed by question -->
## story_96_greet_location_valid_email
* greet
    - utter_greet
* location{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "abcd12@edu.co"}
    - slot{"email": "abcd12@edu.co"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## story_97_greet_location_valid_no_email
* greet
    - utter_greet
* location{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_98_greet_location_invalid_retry_no_email
* location{"location": "koltaka"}
    - slot{"location": "koltaka"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

<!-- no greet, start with location -->
## story_99_no_greet_location_cuisine_price_valid_email
* location{"location": "bhopal"}
    - slot{"location": "bhopal"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "abc12@12abc.co.in"}
    - slot{"email": "abc12@12abc.co.in"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## story_100_no_greet_location_cuisine_price_valid_no_email
* location{"location": "goa"}
    - slot{"location": "goa"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_101_no_greet_location_invalid_retry_no_email
* location{"location": "sagar"}
    - slot{"location": "sagar"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "Chandigarh"}
    - slot{"location": "Chandigarh"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_102_no_greet_location_invalid_retry_email
* location{"location": "kollam"}
    - slot{"location": "kollam"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "Ghaziabad"}
    - slot{"location": "Ghaziabad"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "abcd@domain.net"}
    - slot{"email": "abcd@domain.net"}
    - action_send_mail
    - utter_goodbye
    - action_restart

<!-- cuisine + location, both invalid -->

<!-- greet, followed by question -->
## story_104_greet_cuisine_and_location_invalid_retry_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "hyderabadi", "location": "bilaspur"}
    - slot{"cuisine": "hyderabadi"}
    - slot{"location": "bilaspur"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "ooty"}
    - slot{"location": "ooty"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## story_105_greet_cuisine_and_location_invalid_deny_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "arabian", "location": "alwar"}
    - slot{"cuisine": "arabian"}
    - slot{"location": "alwar"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "Shimla"}
    - slot{"location": "Shimla"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_106_greet_location_cuisine_valid_with_email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "Vizag"}
    - slot{"location": "Vizag"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

<!-- no greet -->
## story_107_no_greet_cuisine_and_location_invalid_retry_no_email
* restaurant_search{"cuisine": "street food", "location": "tumkur"}
    - slot{"cuisine": "street food"}
    - slot{"location": "tumkur"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "Coimbatore"}
    - slot{"location": "Coimbatore"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

<!-- no result in search -->
## story_108_location_cuisine_valid_search_no_result
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_110_location_misspelt_retry_search_no_result
* greet
    - utter_greet
* location{"location": "bengalor"}
    - slot{"location": "bengalor"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "bangalore"}
* affirm
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_111_location_cuisine_price_valid_search_no_result
* restaurant_search{"cuisine": "chinese", "location": "Chennai", "price": "low"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Chennai"}
    - slot{"price": "low"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_112_location_cuisine_valid_search_no_result
* restaurant_search{"cuisine": "chinese", "location": "Chennai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_113_location_valid_cuisine_invalid_retry_search_no_result
* restaurant_search{"cuisine": "hyderabadi", "location": "Chennai"}
    - slot{"cuisine": "hyderabadi"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_rerun
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_115_no_greet_location_cuisine_valid_search_no_result
* restaurant_search{"cuisine": "american", "location": "Amritsar"}
    - slot{"cuisine": "american"}
    - slot{"location": "Amritsar"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_116_no_greet_location_valid_cuisine_invalid_retry_search_no_result
* restaurant_search{"cuisine": "lebanese", "location": "noida"}
    - slot{"cuisine": "lebanese"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_rerun
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_117_greet_cuisine_location_valid_search_no_result
* greet
    - utter_greet
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_location
* location{"location": "ludiana"}
    - slot{"location": "ludiana"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "ludhiana"}
* affirm
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_119_greet_cuisine_valid_search_no_result
* greet
    - utter_greet
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_location
* location{"location": "ludhiana"}
    - slot{"location": "ludhiana"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_120_no_greet_cuisine_invalid_location_misspelt_retry_search_no_result
* restaurant_search{"cuisine": "arabin"}
    - slot{"cuisine": "arabin"}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_rerun
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_location
* location{"location": "panta"}
    - slot{"location": "panta"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "patna"}
* affirm
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_121_greet_cuisine_valid_location_invalid_retry_search_no_result
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_location
* location{"location": "panipat"}
    - slot{"location": "panipat"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "faridabad"}
    - slot{"location": "faridabad"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_122_no_greet_cuisine_valid_search_no_result
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_location
* location{"location": "bhubaneshwar"}
    - slot{"location": "bhubaneshwar"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_123_no_greet_cuisine_invalid_retry_search_no_result
* restaurant_search{"cuisine": "babeque"}
    - slot{"cuisine": "babeque"}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_rerun
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_location
* location{"location": "agra"}
    - slot{"location": "agra"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_125_no_greet_cuisine_valid_location_invalid_retry_search_no_result
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_location
* location{"location": "satara"}
    - slot{"location": "satara"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "agra"}
    - slot{"location": "agra"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_126_greet_location_valid_search_no_result
* greet
    - utter_greet
* location{"location": "agra"}
    - slot{"location": "agra"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_127_greet_location_misspelt_search_no_result
* greet
    - utter_greet
* location{"location": "gurgon"}
    - slot{"location": "gurgon"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "gurgaon"}
* affirm
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_128_greet_location_invalid_search_no_result
* greet
    - utter_greet
* location{"location": "madurai"}
    - slot{"location": "madurai"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "agra"}
    - slot{"location": "agra"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_130_no_greet_location_cuisine_budget_valid_search_invalid
* location{"location": "agra"}
    - slot{"location": "agra"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_131_no_greet_location_invalid_retry_search_invalid
* location{"location": "rampur"}
    - slot{"location": "rampur"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "agra"}
    - slot{"location": "agra"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_132_no_greet_cuisine_and_location_invalid_retry_search_invalid
* restaurant_search{"cuisine": "french", "location": "rampur"}
    - slot{"cuisine": "french"}
    - slot{"location": "rampur"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "agra"}
    - slot{"location": "agra"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_rerun
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_133_greet_cuisine_and_location_invalid_retry_search_invalid
* greet
    - utter_greet
* restaurant_search{"cuisine": "french", "location": "rampur"}
    - slot{"cuisine": "french"}
    - slot{"location": "rampur"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "agra"}
    - slot{"location": "agra"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_rerun
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

<!-- stop conversation with denial-->
## story_134_location_invalid_retry
* restaurant_search{"cuisine": "mexican", "location": "buxar"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "buxar"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* deny
    - utter_deny
    - utter_goodbye
    - action_restart

## story_135_location_valid_cuisine_invalid_retry
* restaurant_search{"cuisine": "arabian", "location": "noida"}
    - slot{"cuisine": "arabian"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_rerun
* deny
    - utter_deny
    - utter_goodbye
    - action_restart

## story_136_no_greet_location_invalid_retry
* location{"location": "siwan"}
    - slot{"location": "siwan"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* deny
    - utter_deny
    - utter_goodbye
    - action_restart

## story_137_greet_location_invalid_retry
* greet
    - utter_greet
* location{"location": "rampur"}
    - slot{"location": "rampur"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* deny
    - utter_deny
    - utter_goodbye
    - action_restart

## story_139_no_greet_cuisine_invalid_retry
* restaurant_search{"cuisine": "barbeque"}
    - slot{"cuisine": "barbeque"}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_rerun
* deny
    - utter_deny
    - utter_goodbye
    - action_restart

## story_140_no_greet_cuisine_invalid_retry
* greet
    - utter_greet
* restaurant_search{"cuisine": "arabian"}
    - slot{"cuisine": "arabian"}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_rerun
* deny
    - utter_deny
    - utter_goodbye
    - action_restart

<!-- drop out of conversation with bye-->

<!-- ## story_66_greet_drop
* greet
    - utter_greet
* goodbye
    - utter_goodbye
    - action_restart

## story_67_restaurant_search_drop
* restaurant_search
    - utter_ask_location
* goodbye
    - utter_goodbye
    - action_restart 

## story_68_no_greet_location_invalid_drop
* location{"location": "rampur"}
    - slot{"location": "rampur"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* goodbye
    - utter_goodbye
    - action_restart
-->
## story_141_no_greet_location_valid_retry_cuisine_drop
* restaurant_search
    - utter_ask_location
* location{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* goodbye
    - utter_goodbye
    - action_restart

## story_143_no_greet_location_invalid_retry_cuisine_drop
* restaurant_search
    - utter_ask_location
* location{"location": "newyork"}
    - slot{"location": "newyork"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* goodbye
    - utter_goodbye
    - action_restart

<!-- ## story_71_no_greet_location_invalid_retry_cuisine_drop
* location{"location": "newyork"}
    - slot{"location": "newyork"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
    - action_restart

## story_72_no_greet_location_invalid_retry_affirm_drop
* restaurant_search
    - utter_ask_location
* location{"location": "newyork"}
    - slot{"location": "newyork"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
    - action_restart

## story_73_ask_location_drop
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* goodbye
    - utter_goodbye
    - action_restart -->

## story_144_no_greet_location_invalid_retry_email_drop
* location{"location": "newjersey"}
    - slot{"location": "newjersey"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* goodbye
    - utter_goodbye
    - action_restart

## story_145_no_greet_location_invalid_retry_email_drop
* restaurant_search
    - utter_ask_location
* location{"location": "arizona"}
    - slot{"location": "arizona"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* goodbye
    - utter_goodbye
    - action_restart

## story_147_location_cuisine_budget_valid_no_result
* greet
    - utter_greet
* restaurant_search{"price": "low", "cuisine": "south indian", "location": "Chennai"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Chennai"}
    - slot{"price": "low"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_148_location_cuisine_budget_valid_with_email
* greet
    - utter_greet
* restaurant_search{"price": "high", "cuisine": "south indian", "location": "Chennai"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Chennai"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## Story_149_Test_story_3
* greet
    - utter_greet
* location{"location": "Agra"}
    - slot{"location": "Agra"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "jddk.2jmd@kdl.co.in"}
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## Story_150_Test_story_4_no_result
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "mumbai"}
* location{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## Story_151_Test_story_4_with_result
* greet
    - utter_greet
* location{"location": "agre"}
    - slot{"location": "agre"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "agra"}
    - slot{"location": "agra"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "jddk.2jmd@kdl.co.in"}
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## Story_152_Test_story_5
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Agra"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Agra"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## Story_153_Test_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* email{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_send_mail
    - action_restart

## Story_154_Test_story_2
* greet
    - utter_greet
* location{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* email{"email": "xyz@sth.edu"}
    - slot{"email": "xyz@sth.edu"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## Story_155
* restaurant_search{"price": "high", "location": "chenai"}
    - slot{"location": "chenai"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "chennai"}
* affirm
    - action_check_location
    - slot{"check_location": true}
    - action_check_price
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "phoenixprince15@ymail.com"}
    - slot{"email": "phoenixprince15@ymail.com"}
    - action_send_mail
* thank
    - utter_goodbye
    - action_restart

## Story_156
* restaurant_search{"price": "high", "location": "chenna"}
    - slot{"location": "chenna"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "chennai"}
* affirm
    - action_check_location
    - slot{"check_location": true}
    - action_check_price
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## Story_157
* restaurant_search{"price": "high", "location": "madurai"}
    - slot{"location": "madurai"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* deny
    - utter_deny
    - utter_goodbye_no_result
    - action_restart

## Story_158
* greet
    - utter_greet
* location{"location": "agra"}
    - slot{"location": "agra"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## Story_159
- utter_ask_location
* restaurant_search{"cuisine": "chinese", "location": "Mumbai", "price": "moderate"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - slot{"price": "moderate"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## Story_160
* location{"location": "Ludhian"}
    - slot{"location": "Ludhian"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "ludhiana"}
* deny
    - utter_ask_location_rerun
* location{"location": "Vadodara"}
    - slot{"location": "Vadodara"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_161_greet_location_price_combined_with_email
* greet
    - utter_greet
* restaurant_search{"price": "high", "location": "Chennai"}
    - slot{"location": "Chennai"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_price
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## story_162_greet_location_price_combined_deny_email
* greet
    - utter_greet
* restaurant_search{"price": "low", "location": "gurgaon"}
    - slot{"location": "gurgaon"}
    - slot{"price": "low"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_price
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_163_greet_location_price_combined_location_invalid_with_email
* greet
    - utter_greet
* restaurant_search{"price": "moderate", "location": "madrs"}
    - slot{"location": "madrs"}
    - slot{"price": "moderate"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## story_164_greet_location_price_combined_location_invalid_deny_email
* greet
    - utter_greet
* restaurant_search{"price": "moderate", "location": "arge"}
    - slot{"location": "arge"}
    - slot{"price": "moderate"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "Agra"}
    - slot{"location": "Agra"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_165_location_price_combined_location_invalid_deny_email
* greet
    - utter_greet
* restaurant_search{"price": "high", "location": "faridabd"}
    - slot{"location": "faridabd"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "faridabad"}
* affirm
    - action_check_location
    - slot{"check_location": true}
    - action_check_price
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_166_no_greet_location_price_combined_with_email
* restaurant_search{"price": "high", "location": "Chennai"}
    - slot{"location": "Chennai"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_price
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## story_167_no_greet_location_price_combined_deny_email
* restaurant_search{"price": "low", "location": "gurgaon"}
    - slot{"location": "gurgaon"}
    - slot{"price": "low"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_price
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_168_no_greet_location_price_combined_location_invalid_with_email
* restaurant_search{"price": "moderate", "location": "madrs"}
    - slot{"location": "madrs"}
    - slot{"price": "moderate"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## story_169_no_greet_location_price_combined_location_invalid_deny_email
* restaurant_search{"price": "moderate", "location": "arge"}
    - slot{"location": "arge"}
    - slot{"price": "moderate"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "Agra"}
    - slot{"location": "Agra"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_170_no_greet_location_price_combined_location_invalid_deny_email
* restaurant_search{"price": "high", "location": "faridabd"}
    - slot{"location": "faridabd"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "faridabad"}
* affirm
    - action_check_location
    - slot{"check_location": true}
    - action_check_price
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_171_greet_location_price_combined_location_invalid_with_email
* greet
    - utter_greet
* restaurant_search{"price": "moderate", "location": "madrs"}
    - slot{"location": "madrs"}
    - slot{"price": "moderate"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_price
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## story_172_greet_price_valid_location_valid_no_result
* greet
    - utter_greet
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - utter_ask_location
* location{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_173_no_greet_price_valid_location_valid_no_result
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - utter_ask_location
* location{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

## story_174_greet_price_valid_location_valid_with_email
* greet
    - utter_greet
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - utter_ask_location
* location{"location": "gurgaon"}
    - slot{"location": "gurgaon"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## story_175_no_greet_price_valid_location_valid_with_email
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - utter_ask_location
* location{"location": "gurgaon"}
    - slot{"location": "gurgaon"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## story_176_greet_price_valid_location_valid_deny_email
* greet
    - utter_greet
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - utter_ask_location
* location{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_177_greet_price_valid_location_invalid_with_email
* greet
    - utter_greet
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - utter_ask_location
* location{"location": "gurgon"}
    - slot{"location": "gurgon"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "gurgaon"}
* affirm
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* email{"email": "gjsudarsaan@gail.com"}
    - slot{"email": "gjsudarsaan@gail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## story_178_greet_price_valid_location_invalid_deny_email
* greet
    - utter_greet
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - utter_ask_location
* location{"location": "gurgon"}
    - slot{"location": "gurgon"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "gurgaon"}
* location{"location": "gurgaon"}
    - slot{"location": "gurgaon"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## story_179_no_greet_price_valid_location_invalid_with_email
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - utter_ask_location
* location{"location": "gurgon"}
    - slot{"location": "gurgon"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "gurgaon"}
* location{"location": "gurgaon"}
    - slot{"location": "gurgaon"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## story_180_greet_price_cuisine_valid_location_invalid_with_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "madres", "price": "high"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "madres"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## story_181_greet_price_cuisine_valid_location_invalid_deny_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "madres", "price": "high"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "madres"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart


## story_182_no_greet_price_cuisine_valid_location_invalid_with_email
* restaurant_search{"cuisine": "chinese", "location": "agre", "price": "high"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "agre"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "agra"}
    - slot{"location": "agra"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## story_183_no_greet_price_cuisine_valid_location_invalid_deny_email
* restaurant_search{"cuisine": "chinese", "location": "agre", "price": "high"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "agre"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "agra"}
    - slot{"location": "agra"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart    

## story_184_no_greet_price_cuisine_valid_location_invalid_deny
* restaurant_search{"cuisine": "chinese", "location": "madres", "price": "high"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "madres"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* deny
    - utter_deny
    - utter_goodbye
    - action_restart

<!-- ## story_184_no_greet_price_cuisine_valid_location_invalid_twice
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "madres", "price": "high"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "madres"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "chena"}
    - slot{"location": "chena"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location": "chennai"}
    - utter_ask_location_rerun
* location{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart -->


* greet
    - utter_greet
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - utter_ask_location
* location{"location": "madrs"}
    - slot{"location": "madrs"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "phoenixprince15@gmail.com"}
    - slot{"email": "phoenixprince15@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

* restaurant_search{"price": "low budget", "location": "Prayagra"}
    - slot{"location": "Prayagra"}
    - slot{"price": "low"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_price
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

* restaurant_search{"cuisine": "chinese", "location": "Gurugran", "price": "moderate"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Gurugran"}
    - slot{"price": "moderate"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "Gurgaon"}
    - slot{"location": "Gurgaon"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

* restaurant_search{"price": "high", "cuisine": "mexican", "location": "Bombey"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Bombey"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

* restaurant_search{"price": "low", "location": "Gulsanabad"}
    - slot{"location": "Gulsanabad"}
    - slot{"price": "low"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_price
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

* greet
    - utter_greet
* restaurant_search{"price": "1500"}
    - slot{"price": "1500"}
    - action_check_price
    - slot{"price": "high"}
    - utter_ask_location
* location{"location": "Benaras"}
    - slot{"location": "Benaras"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "Varanasi"}
    - slot{"location": "Varanasi"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

* restaurant_search{"cuisine": "chinese", "location": "madres", "price": "higher"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "madres"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "amirtharajanpks@hotmail.com"}
    - slot{"email": "amirtharajanpks@hotmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

* restaurant_search{"cuisine": "italian", "location": "Borada", "price": "moderate"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Borada"}
    - slot{"price": "moderate"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "Vadodara"}
    - slot{"location": "Vadodara"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - utter_ask_location
* location{"location": "Vizag"}
    - slot{"location": "Vizag"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

* restaurant_search{"price": "below 700"}
    - slot{"price": "below 700"}
    - action_check_price
    - slot{"price": "moderate"}
    - utter_ask_location
* location{"location": "Poducherry"}
    - slot{"location": "Poducherry"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "puducherry"}
* affirm
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - utter_ask_location
* location{"location": "Patne"}
    - slot{"location": "Patne"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "patna"}
* deny
    - utter_ask_location_rerun
* location{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - action_restart

* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "cochi", "price": "higher"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "cochi"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "Kochi"}
    - slot{"location": "Kochi"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

* restaurant_search{"price": "moderate", "location": "Covei"}
    - slot{"location": "Covei"}
    - slot{"price": "moderate"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "Coimbatore"}
    - slot{"location": "Coimbatore"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_price
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - action_restart

* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - utter_ask_location
* location{"location": "Nagpor"}
    - slot{"location": "Nagpor"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": false}
    - slot{"location": "nagpur"}
* location{"location": "Nagpur"}
    - slot{"location": "Nagpur"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "abcd@gmail.com"}
    - slot{"email": "abcd@gmail.com"}
    - action_send_mail
* thank
    - utter_goodbye
    - action_restart

* restaurant_search{"cuisine": "chinese", "location": "madres", "price": "higher"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "madres"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

* restaurant_search{"price": "high", "location": "pandy"}
    - slot{"location": "pandy"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "Puducherry"}
    - slot{"location": "Puducherry"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

* greet
    - utter_greet
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - utter_ask_location
* location{"location": "Cyberabed"}
    - slot{"location": "Cyberabed"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - action_restart

* restaurant_search{"cuisine": "chinese", "location": "allahabed", "price": "high"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "allahabed"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location": "allahabad"}
    - slot{"location_rerun": false}
* affirm
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart


## Story_greet_location_invalid_price_valid_cuisine_valid_with_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "price": "moderate", "location": "nodia"}
    - slot{"cuisine": "italian"}
    - slot{"location": "nodia"}
    - slot{"price": "moderate"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location": "noida"}
    - slot{"location_rerun": false}
* deny
    - utter_ask_location_rerun
* location{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## Story_no_greet_location_invalid_price_valid_cuisine_valid_with_email
* restaurant_search{"cuisine": "italian", "price": "moderate", "location": "agre"}
    - slot{"cuisine": "italian"}
    - slot{"location": "agre"}
    - slot{"price": "moderate"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location": "agra"}
    - slot{"location_rerun": false}
* deny
    - utter_ask_location_rerun
* location{"location": "agra"}
    - slot{"location": "Agra"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "gjsudarsaan@gmail.com"}
    - slot{"email": "gjsudarsaan@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## Story_greet_location_invalid_price_valid_cuisine_valid_deny_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "price": "moderate", "location": "puna"}
    - slot{"cuisine": "italian"}
    - slot{"location": "puna"}
    - slot{"price": "moderate"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location": "pune"}
    - slot{"location_rerun": false}
* deny
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

## Story_no_greet_location_invalid_price_valid_cuisine_valid_deny_email
* restaurant_search{"cuisine": "italian", "price": "moderate", "location": "patan"}
    - slot{"cuisine": "italian"}
    - slot{"location": "patan"}
    - slot{"price": "moderate"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location": "patna"}
    - slot{"location_rerun": false}
* deny
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "patna"}
    - slot{"location": "patna"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart


* restaurant_search{"cuisine": "north indian", "location": "ranche", "price": "high"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "ranche"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location": "ranchi"}
    - slot{"location_rerun": false}
* deny
    - utter_ask_location_rerun
* location{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "dummy@gmail.com"}
    - slot{"email": "dummy@gmail.com"}
    - action_send_mail
    - action_restart

* restaurant_search{"price": "low budget", "cuisine": "italian", "location": "ranche"}
    - slot{"cuisine": "italian"}
    - slot{"location": "ranche"}
    - slot{"price": "low"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location": "ranchi"}
    - slot{"location_rerun": false}
* deny
    - utter_ask_location_rerun
* location{"location": "Surat"}
    - slot{"location": "Surat"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

* restaurant_search{"cuisine": "american", "location": "indure", "price": "below 700"}
    - slot{"cuisine": "american"}
    - slot{"location": "indure"}
    - slot{"price": "moderate"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location": "indore"}
    - slot{"location_rerun": false}
* deny
    - utter_ask_location_rerun
* location{"location": "lucknow"}
    - slot{"location": "lucknow"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - slot{"price": "moderate"}
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

* restaurant_search{"cuisine": "chinesee", "price": "high", "location": "ludhian"}
    - slot{"cuisine": "chinesee"}
    - slot{"location": "ludhian"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location": "ludhiana"}
    - slot{"location_rerun": false}
* deny
    - utter_ask_location_rerun
* location{"location": "shimla"}
    - slot{"location": "shimla"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - action_restart

* restaurant_search{"cuisine": "north indian", "price": "high", "location": "coimbator"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "coimbator"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location": "coimbatore"}
    - slot{"location_rerun": false}
* deny
    - utter_ask_location_rerun
* location{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - action_restart

* restaurant_search{"cuisine": "mexican", "location": "gangtak", "price": "low"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "gangtak"}
    - slot{"price": "low"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location": "gangtok"}
    - slot{"location_rerun": false}
* deny
    - utter_ask_location_rerun
* location{"location": "ooty"}
    - slot{"location": "ooty"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - action_restart

* restaurant_search{"cuisine": "south indian", "price": "low", "location": "coimbator"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "coimbator"}
    - slot{"price": "low"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location": "coimbatore"}
    - slot{"location_rerun": false}
* deny
    - utter_ask_location_rerun
* location{"location": "Vadodara"}
    - slot{"location": "Vadodara"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - action_restart

* restaurant_search{"cuisine": "italian", "price": "moderate", "location": "nodia"}
    - slot{"cuisine": "italian"}
    - slot{"location": "nodia"}
    - slot{"price": "moderate"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location": "noida"}
    - slot{"location_rerun": false}
* deny{"location": "noida"}
    - slot{"location": "noida"}
    - utter_ask_location_rerun
* location{"location": "Mysore"}
    - slot{"location": "Mysore"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

* restaurant_search{"cuisine": "north indian", "price": "moderate", "location": "dehradon"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "dehradon"}
    - slot{"price": "moderate"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location": "dehradun"}
    - slot{"location_rerun": false}
* deny
    - utter_ask_location_rerun
* location{"location": "dehradun"}
    - slot{"location": "dehradun"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

* restaurant_search{"cuisine": "mexican", "price": "low", "location": "deli"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "deli"}
    - slot{"price": "low"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location": "delhi"}
    - slot{"location_rerun": false}
* deny
    - utter_ask_location_rerun
* location{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

* restaurant_search{"cuisine": "chinese", "location": "madrs"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "madrs"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* affirm
    - utter_ask_location
* location{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* affirm
    - utter_ask_email
* email{"email": "abcde@hotmail.com"}
    - slot{"email": "abcde@hotmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

* restaurant_search{"cuisine": "chinese", "location": "Hosuru"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "texas"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "surat"}
    - slot{"location": "surat"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - action_restart

* restaurant_search{"cuisine": "chinese", "location": "madrs"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "madrs"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": false}
    - utter_no_result
    - utter_goodbye_no_result
    - action_restart

* restaurant_search{"cuisine": "chinese", "location": "Jabalpur"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Jabalpur"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart


* restaurant_search{"cuisine": "southindian", "location": "Kumbakonam"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Kumbakonam"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "Kochi"}
    - slot{"location": "Kochi"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart

* restaurant_search{"cuisine": "northindian", "location": "Nagercoil"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "Nagercoil"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "Nagpur"}
    - slot{"location": "Nagpur"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart


* restaurant_search{"location": "Suryapet","cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Suryapet"}
    - action_check_location
    - slot{"check_location": false}
    - slot{"location_rerun": true}
    - utter_ask_location_rerun
* location{"location": "Surat"}
    - slot{"location": "Surat"}
    - action_check_location
    - slot{"check_location": true}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_check_price
    - action_search_restaurants
    - slot{"check_results": true}
    - utter_ask_top10list
* deny
    - utter_goodbye
    - action_restart