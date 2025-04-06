import random

# WElCOME MESSAGE
print ("Welcome to your Daily Mood Journal !! ")
name = input("What is your name?")
print ("Hello", name, "!")

quotes = {
    "happy": [
      "Joy is contagious- thank you for spreading it around.",
      "You're allowed to feel good without feeling guilt"
    ],
    "sad": [
      " Remember...this too shall pass.",
      "Some days are heavy. You don't have to lift them alone."
    ], 
    "anxious": [
      "Take a deep breath. You've got this.",
      "Be kind to yourself.You are doing the best you can."
    ],
    "stressed": [
      "Not everything is urgent, even if it feels like it is.",
      "Remember slow is still moving."
    ],
    "excited": [
      "This is the kind of energy that builds dreams.",
      "Embrace the excitement. It's a gift."
    ],
    "tired": [
      " Even batteries need to be recharged.",
      " You've done enough for today."
    ],
}
  
scriptures = {
    "happy": [
      "Psalms 118:24 - This is the day that Jehovah has made; We will rejoice and be glad in it.",
      "James 1:17 - Every good gift and every perfect gift is from above [...]"
    ],
    "sad": [
      "Psalms 34:18 - Jehovah is close to the brokenhearted; He saves those who are crushed in spirit.",
      "Psalms 55:22 - Throw your burden on Jehovah, and he will sustain you. Never will he allow the righteous one to fall"
    ],
  "stressed":[
     "Psalms 61:2 - From the ends of the earth I will cry to you,when my heart is overwhelmed",
     "Psalms 46:10 - Give in and know that I am God. I will be exalted among the nations, I will be exalted in the earth."
   ],
  "anxious":[
     "Phiippians 4:6 - Do not be anxious over anything, but in everything by prayer and supplication with thanksgiving,let your petitions be made known to God.", 
    "Isaiah 41:10 - Do not be afraid, for I am with you; Do not be anxious, for I am your God. I will fortify you, yes, I will well help you, I will really uphold you with my righteous right hand."
  ],
  "excited":[
     "Psalms 37:4 - Find exquisite delight in Jehovah, and he will grant you the desires of your heart.",
     "Isaiah 55:12 - For you will go out with rejoicing, and in peace you will be brought back. [...]"
  ],
  "tired":[
    " Matthew 11:28 - Come to me, all you who are toiling and loaded down, and I will refresh you,",
    " Isaiah 40:31 - But those hoping in Jehovah will regain power. They will soar on wings like eagles; they will run and not grow weary; They will walk and not faint."
  ],
}
# encouragement function
def give_encouragement(mood,choice):
    if choice == "quote":
       encouragement_list = quotes.get(mood,[ "You are valued. You are enough."])
    elif choice == "scripture":
       encouragement_list = scriptures.get(mood,["Jehovah is with you always."])
    else:
       encouragement_list = ["Sorry, I didn't understand that. Please try again!"]
    return random.choice(encouragement_list)

# main program
mood = input("How are you feeling today? (Happy, Sad, Stressed, Anxious, Excited or Tired? )").lower()
choice = input("Would you like a quote or a scripture?").lower()

print("\nHere's your encouraging thought for today:")
print(give_encouragement(mood,choice))

#loop to get more inputs
while True: 
   again = input("\nWould you like another thought? (yes/no)").lower()
   if again == "yes":
      mood = input("How are you feeling now? (Happy, Sad, Stressed, Anxious, Excited or Tired)"). lower()
      choice = input("Would you like a quote or a scripture?").lower()
      print("\nHere's your encouraging thought for today:")
      print(give_encouragement(mood, choice))
   else:
      print(f"\nThank you,{name}.See you tomorrow!!")
      break


