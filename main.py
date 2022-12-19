#!/usr/bin/python3

import re
import long_responses as long
import subprocess
import sys

highest_prob_list = {}

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0



def check_all_messages(message):

    # Simplifies response creation / adds it to the dict

    highest_prob_list={}
    
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)


    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello! This is Med-ex chatbot. How can I help you.', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'med', 'ex'], required_words=['med', 'ex'])
    response('You can find these medicines in your nearest pharmacies like CVS Pharmacy, Walgreen Pharmacy or Walmart.', ['where', 'can', 'I', 'find', 'these', 'medicines'], required_words=['find', 'these'])
    response('What are your symptoms?', ['suffering', 'from', 'fever'], required_words=['suffering', 'fever'])
    response('May I know your symptoms?', ['suffering', 'from', 'dehydration'], required_words=['suffering', 'dehydration'])
    response('What are the symptoms you are experiencing?', ['suffering', 'from', 'cold', 'and', 'cough'], required_words=['suffering', 'cold', 'cough'])
    response('Can you explain about your symptoms?', ['suffering', 'from', 'diarrhea'], required_words=['suffering', 'diarrhea'])
    response('You can take Tylenol, Advil or Aspirin for fever.', ['suffering', 'from', 'headache', 'and', 'shivering'], required_words=['headache', 'shivering'])
    response('You can take Hi-Lyte Electrolyte Replacement Tablets for dehydration.', ['suffering', 'from', 'dizziness'], required_words=['dizziness'])
    response('You can take Tylenol cold+flu, DayQuil or NyQuil, Theraflu for cold and cough.', ['suffering', 'from', 'cough', 'and', 'runny_nose'], required_words=['cough', 'runny_nose'])
    response('You can take Pepto Bismol, Imodium or Anti-Diarrheal for diarrhea.', ['suffering', 'from', 'bloating', 'nausea', 'vomiting'], required_words=['bloating', 'nausea', 'vomiting'])
    response('Loss of Appetite, swelling of face and itching', ['effects', 'of', 'tylenol'], required_words=['effects', 'tylenol'])   
    response('Dizziness, Stomachache and Heartburn', ['effects', 'of', 'advil'], required_words=['effects', 'advil'])   
    response('Difficult breathing, Chest pain and change in consciousness', ['effects', 'of', 'aspirin'], required_words=['effects', 'aspirin'])   
    response('Fast Heartbeat, Muscle twitching and Convulsions', ['effects', 'of', 'electrolyte'], required_words=['effects', 'electrolyte'])   
    response('Upset stomach, Blurred vision and Dry mouth', ['effects', 'of', 'cold+flu'], required_words=['effects', 'cold+flu'])
    response('Lightheadedness, Nausea and Nervousness', ['effects', 'of', 'dayquil'], required_words=['effects', 'dayquill'])
    response('Nausea, Dry mouth and Drowsiness', ['effects', 'of', 'nyquil'], required_words=['effects', 'nyquil'])
    response('Nausea, Blackened tongue and Bitter taste', ['effects', 'of', 'pepto'], required_words=['effects', 'pepto'])
    response('Irregular Heartbeat, Loosening of skin', ['effects', 'of', 'imodium'], required_words=['effects', 'imodium'])
    response('Fatigue, Constipation and Abdominal pain', ['effects', 'of', 'anti'], required_words=['effects', 'anti'])

    

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


''' Testing the response system
while True:
    print('Bot: ' + get_response(input('You: '))) '''
