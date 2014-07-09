"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    hand_table = {}
    for dice in hand:
        hand_table[dice] = hand_table.get(dice, 0) + dice
    return max(hand_table.values())


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value of the held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    possible_seq = gen_all_sequences(range(1, num_die_sides+1), num_free_dice)
    total = 0.0
    for seq in possible_seq:
        total += score(seq + held_dice)
    return total/len(possible_seq)

print expected_value((2, 2), 6, 2) #5.83333333333
#expected (3.5, ()) but received (9.9764660493827169, ())


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    choose_set = gen_all_sequences([1,0], len(hand))
    answer_set = set([()])
    for choice in choose_set:
        tmp_sequence = list()
        for choice_n in range(len(choice)):                        
            if choice[choice_n] == 1:
                tmp_sequence.append(hand[choice_n])
        answer_set.add(tuple(tmp_sequence))    
    return answer_set

def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    possi_hold = gen_all_holds(hand)
    best_hold = ()
    best_value = 0
    for hold in possi_hold:
        possi_value = expected_value(hold, num_die_sides, len(hand) - len(hold))
        if possi_value > best_value:
            best_hold = hold
            best_value = possi_value
    return (best_value, best_hold)

def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 2, 3, 4,4) #, 3, 4, 5
    print gen_all_holds(hand)
    print score(hand)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
# run_example()

print expected_value((2, 2), 6, 2)

#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
    
    
    
