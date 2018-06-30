'''
Jessie Covington

the shuffle fn takes a sequence of integers and implements a riffle shuffle
it returns a sequence of shuffled integers

input of shuffle is a list or array
(if input is not an np.array we'll change it to one - just because I prefer np.arrays to work with)

The top card in the deck is the first integer of the sequence and the card at the bottom of the deck is the last number
in the sequence

'''

import numpy as np
from random import randint

def shuffle(D):
    ## input: sequence of integers D that we want to shuffled, list or array
    ## output: sequence of shuffled integers shuffled_deck, np.array
    
    deck = np.array(D)  
    ## if not already numpy array, convert to one - if this is already a np.array, will not change
    
    n = len(deck) ## how many cards are in our deck?
    
    shuffled_deck = np.zeros(n) ## allocate new deck for our shuffled cards
    ## so we can maintain our original sequence
    
    n_right_orig = get_random_number_for_right_deck(n) 
    ## print("How many cards in RHD: ", n_right_orig)
    
    ## want to keep track of how many cards we start with in our right deck - will use later
    
    ## n_left = number of total cards - number of cards in right deck
    n_right = n_right_orig
    n_left = n - n_right_orig
    
    ## We need to drop a total of num_cards cards onto the top of our shuffled_deck
    ## Dropping from the BOTTOM of the subdecks !!
    ## cards from top of original deck become right subdeck - like if I was shuffling a deck of cards for real 
    ## so beginning of sequence
    ## cards at end of sequence are bottom of deck
    
    back = n-1
    for i in range(n):
        
        drop_right = should_drop_from_right_deck(n_left, n_right)
        ## print("n_left %s, n_right %s" %(n_left, n_right)) --> was making sure these actually decreased
        
        if drop_right == True:
            ## print("RIGHT")
            ## print(back-i)
            shuffled_deck[back-i] = deck[n_right-1] ## working from bottom of right deck
            n_right -= 1 # one less card in our right subdeck since it's on shuffled deck now
            
            ## need to be dropping into the back of the new array too!! 
            ## what is dropped first ends up at the bottom of the deck as more is dropped
            ## print("\nCard that SHOULD be dropped: ", deck[n_right-1])
            ## print("Card dropped: ", shuffled_deck[back-i])
            
        else:
            ## print("LEFT")
            ## print(back-i)
            next_card = n_right_orig + n_left - 1 # index of next card to drop from left subdeck
            shuffled_deck[back-i] = deck[next_card]
            n_left -= 1 ## we now have one less card in our left subdeck
            ## print("\nCard that SHOULD be dropped: ", deck[next_card])
            ## print("Card dropped: ", shuffled_deck[back-i])
            
        
    return shuffled_deck

##
## below are the functions used in shuffle to determine size of subdecks and from which subdeck to drop
##

'''

Should this one be based on binomial distribution?? I think so... 
Every time (in real life) that we cut a deck of cards, we get roughly an equal number,
but will rarely get exactly half, the cards in each subdeck

Update: yes, see https://www.stat.berkeley.edu/~aldous/150/Lectures/lecture_37_shuffling.pdf
http://tcs.nju.edu.cn/wiki/index.php/%E9%9A%8F%E6%9C%BA%E7%AE%97%E6%B3%95_(Fall_2011)/Card_Shuffling
'''

def get_random_number_for_right_deck(n): 
    
    ## input: n total number of cards and the highest number that can be returned by this fn  
    ## output: int, how many cards should be split into the right subdeck
    
    ## when shuffling a real deck of cards, we split the deck roughly in half - want the same to happen here, so:
    ## should be (n, 0.5) whre n is the total number of cards
    p = 0.5 ## 'probability of success' - in gsr model should be 1/2
    
    num_right = np.random.binomial(n, p)
    ## print(num_right)
    return num_right

'''
Should be
Based on probability of card actually coming from right deck: R / (R+L) 
where L and R are num cards in left and right deck respectively
so:
n_right / (n_left + n_right)

Bernoulli distribution, yeah? 
Update: Yes. From Wikipedia: 
"the probability distribution of any single experiment that asks a yes–no question; 
the question results in a boolean-valued outcome, a single bit of information whose 
value is success/yes/true/one with probability p and failure/no/false/zero with probability q"
'''

def should_drop_from_right_deck(n_left, n_right): 
    ## input: n_left, n_right ints - how many cards are in the left and right subdecks, respectively
    ## output: Boolean - tells us whether we should drop a card from the right subdeck (True) or left (False)
    
## or if the subdecks are empty
    ## determine if we should drop a card from the right or left subdeck onto the shuffled pile
    
    if (n_left > 0 and n_right > 0):
        ## num = randint(0, 1)  ## remember to change this one!!
        ## bc this is not correct way to do it but it's giving us a random-ish subdeck for the time being
        ## so I can at least see if shuffling is working
        
        p = n_right / (n_right + n_left) ## probability that a card comes from right deck
        ## q = 1 - p ## probability that card comes from left deck
        
        num = np.random.binomial(1, p) ## bernoulli \equiv binomial with just a single trial
    
        ## print("\n n_right %s and n_left %s" %(n_right, n_left))
        ## print("p is %s and num %s" %(p, num))
        
        drop_right_bool = num == 1
        return drop_right_bool
    
    ## the rest is fine though
    elif (n_left == 0 and n_right > 0): ## left subdeck empty so we have to drop from the right deck
        ## print("\n n_right %s and n_left %s" %(n_right, n_left))
        return True
    
    elif (n_left > 0 and n_right == 0): ## right subdeck empty so we have to drop from the left deck
        ## print("\n n_right %s and n_left %s" %(n_right, n_left))
        return False 
    
    else: ## n_left and n_right = 0, empty subdecks
        ## print("\n n_right %s and n_left %s" %(n_right, n_left))
        raise ValueError("The subdecks are empty") ## can't drop from empty deck, n_right and/or n_left have to be >0


## total variation distance - a way to see how many shuffles are needed 
## This is NOT actually working correctly!!! Was curious, tried, didn’t manage to finish
## alg from: https://www.dartmouth.edu/~chance/teaching_aids/Mann.pdf
## norm(R^k - U) = 0.5 * sum_(r=1)^n [ A_(n,r) * abs( binomial(2^k + n - r, n) / 2^(nk) - 1/n! )]
## where A_(n,r) are the Eulerian numbers, A_(n,1) = 1, A_(n,r) = r^n - sum_(j=1)^(r-1) [ binomial(n+r-j, n) * A_(n,j)]
## r is number of rising sequences
## k is number of shuffles
## n is number of cards

k = 7 ## number of shuffles

def A(n,r):
    if r == 1:
        return 1
    else:
        a = r**n - innersum(n,r)
        return a
    
def innersum(n,r):
    s1 = 0
    for j in range(1, r-1):
        b = choose(n+r-j, n) * A(n,j)
        s1 += b
    return s1

def total_var_dist(n,k):
    tvd = 0
    for r in range(1,n):
        tvd += A(n,r) * abs(choose(2^k +n-r, n) / 2**(n*k) - 1/factorial(n))  
    return 0.5 * tvd
        
def factorial(n):
    if n==1:
        return 1
    else: 
        return factorial(n-1)
    
def choose(n, k):
    ## got this method from:
    ## https://stackoverflow.com/questions/3025162/statistics-combinations-in-python/3027128	
    ## A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0
        
