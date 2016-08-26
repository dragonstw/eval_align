system_alignment = [
    [ 'βιβλοσ γενεσεωσ', 'of', 0.352 ],
    [ 'ιησου χριστου', 'jesus christ', 0.316 ],
    [ 'υιου', 'the', 0.92 ],
    [ 'δαυιδ', 'david', 0.268 ],
    [ 'υιου', 'the', 0.92 ],
    [ 'αβρααμ', 'abraham', 0.326 ] ]

manual_alignment = [
    [ 'Βίβλος', 'The book' ],
    [ 'γενέσεως', 'of the genealogy' ],
    [ 'Ἰησοῦ', 'of Jesus' ],
    [ 'Χριστοῦ', 'Christ' ],
    [ 'υἱοῦ', 'son' ],
    [ 'Δαυὶδ', 'of David' ],
    [ 'υἱοῦ', 'son' ],
    [ 'Ἀβραάμ', 'of Abraham' ] ]


def precision_lax():
    pass

# start with comparing the alignments by groupings in system
if __name__ == "__main__":

    manual_english_words = []

    word_count = 0

    phrase = 0
    while phrase < len(system_alignment):
        for index in range(0, len(system_alignment[phrase][0])):
            if system_alignment[phrase][0][index] == ' ':
                first_phrase = system_alignment[phrase][0][0:index]
                second_phrase = system_alignment[phrase][0][index + 1:len(system_alignment[phrase][0])]
                system_alignment[phrase][0] = first_phrase
                system_alignment.insert(phrase + 1, second_phrase)
                phrase += 1
                break

        phrase += 1

        
    print(system_alignment)

    for phrase in range(0, len(manual_alignment)):
        manual_alignment[phrase][0] = manual_alignment[phrase][0].lower()
        manual_english_words.append(manual_alignment[phrase][1])

    print(manual_alignment)
    manual_cat = ' '.join(manual_english_words).lower()
    print(manual_cat)

    for i in range(0, len(system_alignment)):
        if system_alignment[i] != manual_alignment[i]:
            print("ERROR")
            break
        
    for phrase in range(0, len(system_alignment)):
        if system_alignment[phrase][1] in manual_cat:
            word_count += 1

    print(word_count)
            

        # /split the Greek phrase on whitespace
        # get the manual alignment Greek words that correspond
        #  should keep in sync
        #  /transform to lowercase
        #  /check to make sure the words match
        # /concatenate the manual alignment English words
        # /calculate whether there are word overlaps between the:
        #  - system alignment English words
        #  - manual alginment English words
        # /count whether there was a match or not
    #return count_of_matches / len(system_alignment)

        

    
