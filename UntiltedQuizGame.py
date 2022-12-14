print('Welcome to Oliwier´s Short Quiz ;)')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Question 1: What is Oliwier´s Language To Code This?')
    if answer.lower()=='python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer u kaka')
 
 
    answer=input('Question 2: Is Oliwier 11 Years Old? ')
    if answer.lower()=='yes':
        score += 1
        print('GUT')
    else:
        print('...... bruh')
 
    answer=input('Question 3: Is Pizza Good???')
    if answer.lower()=='yes':
        score += 1
        print('Thats Right Is YUMMY')
    else:
        print('I Will Kill You ;)')
 
print('Thankyou for Playing this small quiz game, you did',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE BYE SEE YOU NEXT TIME!')
print('click this link to see how i learned this! https://www.youtube.com/watch?v=O91DT1pR1ew')
