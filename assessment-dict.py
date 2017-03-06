"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    #split string into words, create dictionary
    words = phrase.split()
    word_counter = {}
    #iterate through the string and if word is unique it will have the value of 1 by itself, if pre-existing then add 1 to the existing value.
    for word in words:
        word_counter[word] = word_counter.get(word, 0) + 1

    return word_counter

print count_words("each word appears once")
print count_words("rose is a rose is a rose")
print count_words("Porcupine see, porcupine do.")

def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """
  
    melons = {

        'Watermelon': 2.95, 
        'Cantaloupe': 2.50, 
        'Musk': 3.25, 
        'Christmas': 14.25
        }
    #if melon is found, return the price, if not, return 'No price found'

    return melons.get(melon_name, "No price found")

print get_melon_price('Watermelon')
print get_melon_price('Cantaloupe')
print get_melon_price('Musk')
print get_melon_price('Christmas')
print get_melon_price('Nothing')




def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """

    words_lengths = {}
    #create dictionary, add a new word into the dict whenever the length exists but the word does not. if lengths exists, add all words to list
    for word in words:
        if len(word) not in words_lengths:
            words_lengths[len(word)] = [word]
        else:
            words_lengths[len(word)] = words_lengths[len(word)] + [word]

    #because we had to sort both the lengths of words AND the actual words in the list of values, we had to create the for i loop to access the list (value side) for sorting at [i][1]       
    isorted = sorted(words_lengths.items())
    for i in range(len(isorted)):
        isorted[i][1].sort()
    return isorted


# print word_length_sorted(["ok", "an", "apple", "a", "day"])
print word_length_sorted(["porcupine", "ok"])

def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    #create pirate key value pairs
    pirate_translator = {
                        'sir': 'matey',
                        'hotel': 'fleabag inn',
                        'student': 'swabbie',
                        'man': 'matey',
                        'professor': 'foul blaggart',
                        'restaurant': 'galley',
                        'your': 'yer',
                        'excuse': 'arr',
                        'students': 'swabbies',
                        'are': 'be',
                        'restroom': 'head',
                        'my': 'me',
                        'is': 'be',

    }

    #split string into words, create dictionary container.
    phrases = phrase.split()
    pirate_dict = []
    
    #iterate through the string, if word exists in pirate translator, add the value to the output, if not, add the not translated word (to see the fault). Return the re-joined back together words that were split up.
    for word in phrases:
        if word in pirate_translator:
            pirate_dict.append(pirate_translator[word])
        else:
            pirate_dict.append(word)

    return " ".join(pirate_dict)


print translate_to_pirate_talk("my student is not a man")
print translate_to_pirate_talk("my student is not a man!")
             

def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    #Use a dictionary. Capture the last character of the first word[-1] and initialize the next word by searching for the same letter located at last word's last character in the beginning of the next word.

    # initialize dictionary, set first value and reference last character in the first value. Create new for output.
#     my_dict = {}
#     first_word = names[0]
#     last_char = first_word[-1]
#     words = [first_word]
    
#     #create dictionary
#     for name in names:
#         if name[0] in my_dict:
#             my_dict[name[0]].append(name)
#         else:
#             my_dict[name[0]] = [name]
#     # return my_dict

#     #there's something wrong with the logic in my while loop, I spent 5 hours on this I'm going give up for now. 
#     while True:
#         if my_dict[last_char] not in my_dict:
#             break
#         else: 
#             sec_word = my_dict[last_char][0]
#             words.append(sec_word)
            
#             first_word = sec_word
#             last_char = first_word[-1]

#     return words

# print kids_game(["bagon", "baltoy", "yamask", "starly", "nosepass", "kalob", "nicky", "booger"])
# print kids_game(["apple", "berry", "cherry"])
# print kids_game(["noon", "naan", "nun"])
    

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
