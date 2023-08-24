from wonderwords import RandomSentence

generator_sentences = RandomSentence()


# generate a bare-bone sentence
bare_bone_sentence = generator_sentences.bare_bone_sentence()
print(bare_bone_sentence)


# generate a simple sentence
simple_sentence = generator_sentences.simple_sentence()
print(simple_sentence)


# a sentence with a subject, predicate, adjective and direct object
sentence = generator_sentences.simple_sentence()
print(sentence)