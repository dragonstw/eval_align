system_alignment = [
    [ u'βιβλοσ γενεσεωσ', 'of', 0.352 ],
    [ u'ιησου χριστου', 'jesus christ', 0.316 ],
    [ u'υιου', 'the', 0.92 ],
    [ u'δαυιδ', 'david', 0.268 ],
    [ u'υιου', 'the', 0.92 ],
    [ u'αβρααμ', 'abraham', 0.326 ] ]

manual_alignment = [
    [ u'Βίβλος', 'The book' ],
    [ u'γενέσεως', 'of the genealogy' ],
    [ u'Ἰησοῦ', 'of Jesus' ],
    [ u'Χριστοῦ', 'Christ' ],
    [ u'υἱοῦ', 'son' ],
    [ u'Δαυὶδ', 'of David' ],
    [ u'υἱοῦ', 'son' ],
    [ u'Ἀβραάμ', 'of Abraham' ] ]


def precision_lax():
    pass

# start with comparing the alignments by groupings in system
if __name__ == "__main__":

    for phrase in system_alignment:
        # split the Greek phrase on whitespace
        # get the manual alignment Greek words that correspond
        #  should keep in sync
        #  transform to lowercase
        #  check to make sure the words match
        # concatenate the manual alignment English words
        # calculate whether there are word overlaps between the:
        #  - system alignment English words
        #  - manual alginment English words
        # count whether there was a match or not
    return count_of_matches / len(system_alignment)

        

    
