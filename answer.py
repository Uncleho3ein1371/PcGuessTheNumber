salam
import random
def answer_range(answer, lower_r, upper_r):

    answer = int(answer)
    lower_r = int(lower_r)
    upper_r = int(upper_r)

    if answer < lower_r:
        answer = input('please_enter_your_on_mind_answer(greater than min): ')
        return answer_range(answer, lower_r, upper_r)

    elif upper_r < answer:
        answer = input('please_enter_your_on_mind_answer(less than max): ')
        return answer_range(answer, lower_r, upper_r)

    else:
        print(f"{lower_r} < {answer} < {upper_r}")
        return answer
        
lower_r = input('please_provide_your_lower_range: ')
lower_r = int(lower_r)
upper_r = input('please_provide_your_upper_range: ')
upper_r = int(upper_r)
while lower_r > upper_r:
    lower_r = input('please_enter_a_lower_number: ')
    lower_r = int(lower_r)


answer = input('please_provide_your_on_mind_answer: ')

answer = answer_range(answer, lower_r, upper_r)
lower_r = int(lower_r)
upper_r = int(upper_r)
print('Answer: ', answer)

guess = random.randint(int(lower_r), int(upper_r))
print("Guess: ", guess)

if {guess} == {answer}:
    print('.....you did it! you rock PC!.....')

print('please provide your guidance with words "higher" or "lower" or "just press ENTER if the answer is equal to '
      'guess"')

guide = input('please provide your guidance: ')

def cguess(guess, guide, lower_r, upper_r, answer):
    while guess != answer:
        if guide == 'higher':
            lower_r = guess + 1
        
        elif guide == 'lower':
            upper_r = guess - 1

        else:
            break

        guess = int((lower_r + upper_r) / 2)
        print("Guess: ", guess)
        guide = input('please provide your guidance: ')
    return guess

guess = cguess(guess, guide, int(lower_r), int(upper_r), answer)
guess = int(guess)

if {guess} == {answer}:
    print('.....you did it! you rock PC!.....')

while answer == guess:
    play_again = input("do you want to play another round: yes or no >>>>> ")
    if play_again == 'yes':
        lower_r = input('please_provide_your_lower_range: ')
        lower_r = int(lower_r)
        upper_r = input('please_provide_your_upper_range: ')
        upper_r = int(upper_r)
        while lower_r > upper_r:
            lower_r = input('please_enter_a_lower_number: ')
            lower_r = int(lower_r)

        answer = input('please_provide_your_on_mind_answer: ')

        answer = answer_range(answer, lower_r, upper_r)
        answer = int(answer)


        guess = random.randint(int(lower_r), int(upper_r))
        print("Guess: ", guess)

        if guess == answer:
            print('.....you did it! you rock PC!.....')

        print(
                'please provide your guidance with words "higher" or "lower" or "just press ENTER if the answer is '
                'equal to guess"')

        guide = input('please provide your guidance: ')

        guess = cguess(guess, guide, int(lower_r), int(upper_r), answer)
        guess = int(guess)

        if {guess} == {answer}:
            print('.....you did it! you rock PC!.....')

    else:
        print('.........GG........')
        break



