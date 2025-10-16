# Trivia game
#1 list of questions dict
#2 store answers dict
#3 randomly pick questions rdm gen with random module 
#4 ask questions to user
#5 check if user is correct
#6 track score
#7 tell user score

import random


Questions = { "what is the famous opening quote from warhammer 40,000? ":"in the grim darkness of the far future there is only war",
            "what is the faction leader of the necrons called?": "the silent king", 
            "what is the faction leader of the imperium called?": "the emperor Of mankind", 
            "what ancient war were the necrons involved in?":"the war in heaven", 
            "what was the great unification campaign of the galaxy called under the emperor of mankind?":"the great crusade"
            }



def trivia_game():
    ques_list = list(Questions.keys())
    total = 5
    score = 0
    
    selected_ques = (random.sample(ques_list, total))
    #print(selected_ques)

    for index, question in enumerate(selected_ques, start= 1):
        print(index, ":", question)
        user_answer = input("Your answer: ").lower().strip()

        correct_answer = Questions[question]
        if user_answer == correct_answer.lower():
            print("correct!\n")
            score += 1 
        else:
            print(f"wrong! the correct answer is......{correct_answer}.\n")

    print(f"Game over! your final score is {score}/{total}!\n")



trivia_game()
