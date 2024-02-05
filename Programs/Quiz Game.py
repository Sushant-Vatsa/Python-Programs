#Quiz Game
print("This is a Quiz Game ! \nYou'll Get Points for Every Correct Answer")
points = 0
questions = [
    "Who Was The Founder of Google?",
    "Who was The First President of India?",
    "Who Wrote the National Anthem?",
    "Who was the first prime minister of India?",
    "Which is the Most Soft Organ of Human Body?"
]

options = [
    ["A. Harry Gross", "B. Bid Edden", "C. Sean Doom", "D. Niger harry", "E. Larry Page"],
    ["A. Ramanujan", "B. kumar sanu", "C. Rajendra prasad", "D. Sam curran", "E. Virat Kohli"],
    ["A. Tagore", "B. Bankim Chandra Chatterjee", "C. Vande Mataram", "D. Jana Gana Mana", "E. Bharat Mata ki Jai"],
    ["A. Jawaharlal Nehru", "B. Sardar Patel", "C. Indira Gandhi", "D. Rajiv Gandhi", "E. Lal Bahadur Shastri"],
    ["A. Skin", "B. Brain", "C. Liver", "D. Heart", "E. Lungs"]
]

answers = ["E", "C", "A", "A", "A"]

for i in range(len(questions)):
    print("----------------------")
    print(questions[i])
    print(options[i])
    user_answer = input("Enter You Answer (A,B,C,D,E) : ").upper()

    if user_answer == answers[i] :
        print("Correct !")
        points += 1
    else:
        print("Incorrect !")

#Result
print("----------------------")
total = print(f'CONGRATULATIONS ! \nYour Got {points} points')

