from wonderwords import RandomWord

generator_words = RandomWord()


############                .word()                ############
#   generates a random word under given conditions            #
#   starts_with            ends_with              char        #
#   word_min_length        word_max_length        int         #
#   regex=                                                    #
#   include_categories=adjective || noun || verb              #
###############################################################
word = generator_words.word(starts_with='f', include_categories=["verb"], word_min_length=5)
print(word)


print("+"*25)


############               .filter()               ############
#   generates a list of random words under given conditions   #
#   starts_with            ends_with              char        #
#   word_min_length        word_max_length        int         #
#   regex=                                                    #
#   include_categories=adjective || noun || verb              #
###############################################################
dict = generator_words.filter(starts_with='f', include_categories=["verb"], word_min_length=5)
print(dict)


print("+"*25)


############               .filter()               ############
#   generates a list of random words under given conditions   #
#   first argument is an int and it sets how many words       #
#   You want, when not given, it returns list of one word     #
#   starts_with            ends_with              char        #
#   word_min_length        word_max_length        int         #
#   regex=                                                    #
#   include_categories=adjective || noun || verb              #
#   return_less_if_necessary                      boolean     #
###############################################################
list = generator_words.random_words(5, starts_with='f', include_categories=["verb"], word_min_length=5)
print(list)
