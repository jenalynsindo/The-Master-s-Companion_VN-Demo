## The game starts here.

label start:
    $ mc_name = renpy.input('This book belongs to:', default='Mili', length=8)
    if mc_name == '':
        $ mc_name = 'Mili'

    # Make this as NVL mode with opened book as background.

    'Author\'s Note'

    'Greetings.'

    'If you\'re able to read this, then I peg you as someone who\'s
        incredibly lucky or unbelievably unfortunate for no ordinary person
        can find this book.'

    'I made this book a very long time ago. I was always by myself and he was
        my only companion all through my lonely life.'

    'This book will give you utter happiness but it will also give you heartache.
        So I\'m writing this as a warning:'

    'If you\'ve really decided to go on, then I applaud your courage but if not,
        this is your chance to close this book and never open it again.'

    'If you choose to carry on, I hope he\'ll give you enough smiles all through
        the year.'

    '- The Master'

    jump first_leaf
