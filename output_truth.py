"""
    This code generates the truth, the full truth, and nothing but the truth,
    so help it Great Kirby in the Sky.
"""
import random
import operator

characters = [
                'luigi',
                'mario',
                'dk',
                'link',
                'samus',
                'falcon',
                'ness',
                'yoshi',
                'kirby',
                'fox',
                'pikachu',
                'puff'
            ]


def generate_shears_tier_list():
    char_ranks = { x:random.uniform(1,10) for x in characters }
    char_ranks['pikachu'] = 0  # last, obviously
    char_ranks['fox'] = 11 + random.uniform(1,2)  # the best?
    char_ranks['yoshi'] = 11 + random.uniform(1,2)  # sometimes the best, too
    char_ranks['luigi'] = 5.5  # not as bad as people think
    
    sorted_x = sorted(char_ranks.items(), key=operator.itemgetter(1), reverse=True)
    print("\nTier List by Shears\n")
    for idx, char_tuple in enumerate(sorted_x):
        print("{:<3} {:>15}".format(str(idx+1), char_tuple[0]) )
        
        
def generate_kero_tier_list():
    char_ranks = { x:random.uniform(1,10) for x in characters }
    char_ranks['fox'] = 0  # last, obviously
    char_ranks['pikachu'] = 11  # the best
    char_ranks['falcon'] = 10 - random.uniform(1,2)  # can taunt cancel short hop from side to top plat
    char_ranks['kirby'] = 5.5  # not as good as people think
    
    sorted_x = sorted(char_ranks.items(), key=operator.itemgetter(1), reverse=True)
    print("\nTier List by Kero\n")
    for idx, char_tuple in enumerate(sorted_x):
        print("{:<3} {:>15}".format(str(idx+1), char_tuple[0]) )