import speech_recognition as sr
from gtts import gTTS
import os
import pygame
import datetime
import requests
import random
import webbrowser
import psutil
import urllib.parse
import pywhatkit
import time
from bs4 import BeautifulSoup

# Speak Function
def speak_hindi(text):
    print("\nस्मार्ट असिस्टेंट:", text)
    tts = gTTS(text=text, lang="hi")
    tts.save("response.mp3")

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("response.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.quit()
    os.remove("response.mp3")

# Listen Function
def listen_hindi():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nहिंदी में बोलें... (Speak in Hindi)")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio, language="hi-IN").lower()
            print("\nआपने कहा:", text)
            return text
        except:
            return None

# Greet Function
def greet_user():
    speak_hindi("हेलो, अस्सलामुअलैकुम! मैं आपकी स्मार्ट असिस्टेंट हूँ। मैं आपकी कैसे मदद कर सकती हूँ?")

# Time Function
def tell_time():
    now = datetime.datetime.now()
    speak_hindi(f"अभी समय है {now.strftime('%I:%M %p')}")

# Date Function
def tell_date():
    now = datetime.datetime.now()
    speak_hindi(f"आज की तारीख {now.strftime('%d-%m-%Y')} है")

# Battery Function
def check_battery():
    battery = psutil.sensors_battery()
    if battery:
        speak_hindi(f"आपके डिवाइस की बैटरी {battery.percent} प्रतिशत है।")
    else:
        speak_hindi("मुझे बैटरी की जानकारी नहीं मिल रही है।")

# Play Music Function
def play_music():
    speak_hindi("कृपया गाने का नाम बताएं।")
    song_name = listen_hindi()
    if song_name:
        speak_hindi(f"मैं {song_name} गाना चला रहा हूँ।")
        pywhatkit.playonyt(song_name)
        time.sleep(5)  # Wait for YouTube to load
    else:
        speak_hindi("मुझे गाने का नाम समझ नहीं आया।")

# Open Websites Function
def open_website(query):
    sites = {
        "गूगल": "https://www.google.com",
        "फेसबुक": "https://www.facebook.com",
        "यूट्यूब": "https://www.youtube.com",
        "ट्विटर": "https://www.twitter.com",
        "विकिपीडिया": "https://www.wikipedia.org"
    }
    for key, url in sites.items():
        if key in query:
            speak_hindi(f"मैं {key} खोल रहा हूँ।")
            webbrowser.open(url)
            return
    speak_hindi("मुझे यह वेबसाइट नहीं मिली।")

# Play YouTube Video Function
def play_youtube_video(query):
    if not query:
        speak_hindi("कृपया वीडियो का नाम बताएं।")
        return
    speak_hindi(f"मैं यूट्यूब पर {query} वीडियो चला रहा हूँ।")
    search_url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"
    webbrowser.open(search_url)

# Jokes Function
def tell_tamasha():
    jokes = [
        "टीचर: बच्चों एक अच्छी आदत बताओ? छात्र: खाली बर्तन में पानी भरना चाहिए!",
        "पति: मुझे तुम्हारी चुप रहने की आदत सबसे अच्छी लगती है!",
        "डॉक्टर: आपको आराम की ज़रूरत है, नींद पूरी लेनी चाहिए! मरीज: लेकिन डॉक्टर साहब, मेरी नींद तो लेक्चर में पूरी हो जाती है!"
    ]
    speak_hindi(random.choice(jokes))

# Get News Function
def get_news():
    try:
        url = "https://news.google.com/rss?hl=hi&gl=IN&ceid=IN:hi"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "xml")
        headlines = soup.findAll("title")[1:6]
        speak_hindi("आज की मुख्य खबरें इस प्रकार हैं:")
        for headline in headlines:
            speak_hindi(headline.text)
    except:
        speak_hindi("मुझे समाचार लाने में समस्या हो रही है।")

# Story Function
def tell_story():
    stories = [

        "एक बार की बात है, एक गरीब किसान को एक जादुई हंस मिला। वह हर दिन एक सोने का अंडा देता था। किसान बहुत खुश था, लेकिन वह लालची हो गया और सोचने लगा कि उसके पेट में और अंडे होंगे। एक दिन उसने हंस को मारकर उसके पेट को देखा, लेकिन उसमें कुछ नहीं था। इस तरह, उसकी लालच ने उसे सब कुछ खो दिया।",  
        
        "एक जंगल में एक शेर और चूहा रहते थे। एक दिन शेर ने चूहे को पकड़ लिया और उसे खाने ही वाला था कि चूहे ने कहा, 'अगर आप मुझे छोड़ देंगे तो मैं कभी न कभी आपकी मदद जरूर करूंगा।' शेर हँसा और उसे जाने दिया। कुछ दिनों बाद, शिकारी ने शेर को जाल में फंसा लिया। चूहा आया और अपने तेज़ दांतों से जाल काटकर शेर को आज़ाद कर दिया। इससे शेर को समझ में आया कि कोई भी छोटा नहीं होता।",  
        
        "गांव में एक छोटा लड़का था, जो हमेशा सच बोलता था। एक दिन उसे जंगल में एक गुफा मिली और उसने अंदर जाकर देखा कि वहां ढेर सारा सोना रखा हुआ था। गुफा में एक बूढ़ा संत भी था। संत ने लड़के से कहा, 'अगर तुम यह सोना लेकर जाओगे तो तुम्हें हमेशा झूठ बोलना पड़ेगा।' लड़के ने सोचा और फिर सोने को लेने से इनकार कर दिया। संत उसकी ईमानदारी से खुश हुआ और उसे आशीर्वाद दिया कि वह जीवन में हमेशा सफलता पाएगा।"
    ]
    
    speak_hindi(random.choice(stories))

# Motivational Quotes Function
def tell_motivation():
    quotes = [
        "सफलता की राह में धैर्य और मेहनत सबसे बड़े हथियार होते हैं।",
        "अगर तुम सच में कुछ करना चाहते हो, तो रास्ता खुद बन जाएगा।"
    ]
    speak_hindi(random.choice(quotes))

# Main Loop
while True:
    user_input = listen_hindi()

    if user_input:
        if "नमस्ते" in user_input or "हेलो" in user_input:
            greet_user()
        elif "समय" in user_input:
            tell_time()
        elif "तारीख" in user_input:
            tell_date()
        elif "बैटरी" in user_input:
            check_battery()
        elif "समाचार" in user_input:
            get_news()
        elif "तमाशा" in user_input:
            tell_tamasha()
        elif "कहानी" in user_input:
            tell_story()
        elif "प्रेरणादायक" in user_input or "मोटिवेशन" in user_input:
            tell_motivation()
        elif "खोलो" in user_input:
            open_website(user_input)
        elif "यूट्यूब पर वीडियो चलाओ" in user_input:
            play_youtube_video(user_input.replace("यूट्यूब पर वीडियो चलाओ", "").strip())
        elif "गाना चलाओ" in user_input:
            play_music()
        elif "बंद करो" in user_input or "रुको" in user_input:
            speak_hindi("ठीक है, अलविदा!")
            break
