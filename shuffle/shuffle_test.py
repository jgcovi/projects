""" 
Jessie Covington

Testing of shuffles(list: deck)

"""

import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
from sys import argv
## %matplotlib inline

from shuffles import shuffle

## not the most sophisticated, but will tell us if we have a grouping of three consecutive cards in our decks
## unfortunately will also return higher numbers when there is a grouping of more than 3, so not quite correct
## ex: [1, 2, 3, 4, 5] --> 3 consecutive groups of 3 cards - but since it is ordered
def three_consecutive(deck):
    count = 0
    for i in range(len(deck)-2):
        diff = deck[i+1] - deck[i]
        if (abs(deck[i+2] - deck[i+1]) == diff) and (abs(deck[i+1] - deck[i]) == diff):
            count += 1
        else:
            count = count
    return count

def repeated(deck):
    count = 0
    for i in range(len(deck)-1):
        if deck[i] == deck[i+1]:
            count+=1
        else:
            count = count
    return count

## f = open('shuffles_notes.txt', 'r') 
## contents = f.read()
## print(contents)


## some initial things that will be used throughout:
## this won't be used, but
D0 = np.array(range(0,0)) ## I just want to make sure we won't get an error with an empty list as input, you never know
S0 = shuffle(D0) ## works no problem
## print(S0) --> [] - as it should

## now the decks we'll actually be considering:
D13 = list(range(0, 13))
D26 = list(range(0, 26))
D52 = list(range(0, 52))
D104 = list(range(0, 104))

deck_list = np.array([D13, D26, D52, D104]) ## keep all our original decks in one place together
n = len(deck_list)  ## this will be used throughout - number of original and shuffled decks

num_shuffles = 10 ## how many shuffles do we want to try?

### so we can keep track of what the deck looks like after each individual shuffle:
deck1_shuffles = np.zeros((num_shuffles+1, len(D13)))
deck2_shuffles = np.zeros((num_shuffles+1, len(D26)))
deck3_shuffles = np.zeros((num_shuffles+1, len(D52)))
deck4_shuffles = np.zeros((num_shuffles+1, len(D104)))

deck1_shuffles[0] = D13
deck2_shuffles[0] = D26
deck3_shuffles[0] = D52
deck4_shuffles[0] = D104

print("Let's consider where the original top and bottom cards of the unshuffled deck end up after %s shuffles." %(num_shuffles))
print()

top_card_num_arr = np.zeros(n) ## keep track of our first to see where it ends up - in this case they're all 0
## but might have a case where it's not later, so.
bottom_card_num_arr = np.zeros(n) ## keep track of last element so we can see where it ends up

init_top_card_index = np.zeros(n) ## so we can compare later - all will remain zero since first index
init_bottom_card_index = np.zeros(n)

new_top_card_index = np.zeros(n) ## store the index of where the original top card ends up
new_bottom_card_index = np.zeros(n) ## '' '' bottom '' ''

## so we can keep our original decks if we need to use them later and bc otherwise Si won't be recognized
S1 = D13
S2 = D26
S3 = D52
S4 = D104

## shuffle each deck however many times we wanted to shuffle (declared above)
for i in range(1, num_shuffles):
    S1 = shuffle(S1).tolist()
    S2 = shuffle(S2).tolist()
    S3 = shuffle(S3).tolist()
    S4 = shuffle(S4).tolist()

    deck1_shuffles[i] = S1
    deck2_shuffles[i] = S2
    deck3_shuffles[i] = S3
    deck4_shuffles[i] = S4

## putting them in a list to make easier and shorter to access
shuffled_deck_list = [S1, S2, S3, S4]

for i in range(n):
    ## store the first and last elements(top and bottom cards) of each deck
    top_card_num_arr[i] = deck_list[0][0]
    bottom_card_num_arr[i] = deck_list[i][-1]

    ## find indices of bottom card of deck (doing this way in case we change our deck sizes later)
    init_bottom_card_index[i] = len(deck_list[i]) - 1

    ## store the index of where the first and last cards moved
    new_top_card_index[i] = shuffled_deck_list[i].index(top_card_num_arr[i])
    new_bottom_card_index[i] = shuffled_deck_list[i].index(bottom_card_num_arr[i])

    ## shuffled_deck_list[i] = shuffled_deck_list[i].tolist()
    ## print("The shuffled deck %s is: \n %s \n" %(i+1, shuffled_deck_list[i]) )

        
## print(init_top_card_index, init_bottom_card_index)
## print(new_top_card_index, new_bottom_card_index)
for i in range(len(deck_list)):
    print("%s cards: \n%s" %(len(deck_list[i]), shuffled_deck_list[i]))
    print()
    print("%s cards, initial index %s (top card) --> index %s" %(len(deck_list[i]), init_top_card_index[i], new_top_card_index[i]))
    print("Top card moved %s positions" %(new_top_card_index[i] - init_top_card_index[i]))
    print("%s cards, initial index %s (bottom card) --> index %s" %(len(deck_list[i]), init_bottom_card_index[i], new_bottom_card_index[i]))
    print("Bottom card moved %s positions" %(init_bottom_card_index[i] - new_bottom_card_index[i]))
    print()

       
## if enough time, try to do a few more, graph, and compare to see how many spaces it moves more generally
## ideally, would also be able to make a histogram or something of how many times each element appears in a certain position

print("Let's look at whether there are still groups of consecutive cards.")
print("We'll consider a consecutive group to be 3 ordered cards in a row.")
print()   

print("Let's compare consecutive shuffles of 26 cards:")
print()
grps = np.zeros(num_shuffles)
for row in range(num_shuffles):
    print("Shuffle %s: %s\n" %(row, deck2_shuffles[row]))
    grps[row] = three_consecutive(deck2_shuffles[row])
print("List of number of ordered sequences at each iteration: ", grps)
plt.plot(grps)
plt.show()

print("Let's compare consecutive shuffles of 52 cards:")
print()
grps = np.zeros(num_shuffles)
for row in range(num_shuffles):
    print("Shuffle %s: %s\n" %(row, deck3_shuffles[row]))
    grps[row] = three_consecutive(deck3_shuffles[row])
print("List of number of ordered sequences at each iteration: ", grps)
print("And we can see that at around 7 shuffles, we stop seeing two number groupings as much as well.")
plt.plot(grps)
plt.show()

print("Let's compare consecutive shuffles of 104 cards:")
print()
grps = np.zeros(num_shuffles)
for row in range(num_shuffles):
    ## print("Shuffle %s: %s\n" %(row, deck4_shuffles[row]))
    grps[row] = three_consecutive(deck4_shuffles[row])
print("List of number of ordered sequences at each iteration: ", grps)
plt.plot(grps)
plt.show()

print("So we can see from the graphs that the number of sequences of consecutive cards decreases quickly and remains near 0")
print("In all cases, it looks like after about 4 shuffles, we have reached zero consecutive cards.")
print("However, it will still take more than these shuffles to fully randomize a deck of more than 52 cards")
print("This does not take into consideration this distribution of the cards - such as whether those from the bottom half of the deck are still largely dispersed through the bottom half of the deck, just less ordered now - would need to check that as well")

print("It should take about 7 shuffles for a deck of 52 cards in order to fully randomize the deck.")
print("In general, it should take ~3/2*log_2(n) shuffles to fully randomize a deck of n cards.")

print("As for small changes to the shuffling model, suppose we fix a single card (one single card that is so bent it doesn't incorporate well when shuffling and just flops back on top.)")
print("This has now made a restriction on the possible orderings of the cards, as one position is permanently taken and we are now left with (n-1)! possible permutations, each of which should be equally likely given the rest of the conditions stay the same and the appropriate number of shuffles are done.")
print("If we repeat elements, we can see that the more duplicate elements there are in a deck, it still seems to randomize well (based purely on visual observation and comparison).")

## set up decks with some number of repeated elements
## deck with single repeated element:
R52_1 = np.zeros(52)
R52_2 = np.zeros(52)
for i in range(len(R52_1)):
    if i%51 == 1:
        R52_1[i] = i+1
    else:
        R52_1[i] = i

## deck with 2 of every card:
for i in range(len(R52_2)):
    if i%2 == 0:
        R52_2[i] = i+1
    else:
        R52_2[i] = i

## print(R52_1)
## print(R52_2)

shuff = 7
Sdeck = D52
shuff_R52_1 = R52_1
shuff_R52_2 = R52_2
rpts = np.zeros(shuff)
grps_Sdeck = np.zeros(shuff)
grps_R52_1 = np.zeros(shuff)
grps_R52_2 = np.zeros(shuff)

for i in range(shuff):
    rpts[i] = repeated(shuff_R52_2)
    grps_Sdeck[i] = three_consecutive(Sdeck)
    grps_R52_1[i] = three_consecutive(shuff_R52_1)
    grps_R52_2[i] = three_consecutive(shuff_R52_2)
    ## print(repeated(shuff_R52_2))
    Sdeck = shuffle(Sdeck)
    shuff_R52_1 = shuffle(shuff_R52_1)
    shuff_R52_2 = shuffle(shuff_R52_2)
    

print("The original shuffled deck of 52 cards after 7 shuffles: \n", np.array(Sdeck))
print("List of number of ordered sequences at each iteration: ", grps_Sdeck)
plt.plot(grps_Sdeck)
plt.show()
print()

print("The deck with a single repeated card after 7 shuffles: \n", shuff_R52_1)
print()
print("List of number of ordered sequences at each iteration: ", grps_R52_1)
plt.plot(grps_R52_1)
plt.show()

print("The deck with 52 cards and 2 of every element after 7 shuffles: \n", shuff_R52_2)
print()
print("Pairs of repeated elements (side by side): ", rpts)
plt.plot(rpts)
plt.show()

print("List of number of ordered sequences at each iteration: ", grps_R52_2)
plt.plot(grps_R52_2)
plt.show()

print("Actually here, we don't see repeated elements immediately next to one another, that quickly gets taken care of.")
print("Instead, the number of ordered sequences actually increases, much unlike the other cases.")