import re

import spacy
#  python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")


text = """
[Verse 1]
Hello, it's me
I was wondering if after all these years you'd like to meet
To go over everything
They say that time's supposed to heal ya, but I ain't done much healing
Hello, can you hear me?
I'm in California dreaming about who we used to be
When we were younger and free
I've forgotten how it felt before the world fell at our feet

[Pre-Chorus]
There's such a difference between us
And a million miles

[Chorus]
Hello from the other side
I must've called a thousand times
To tell you I'm sorry for everything that I've done
But when I call, you never seem to be home
Hello from the outside
At least, I can say that I've tried
To tell you I'm sorry for breaking your heart
But it don't matter, it clearly doesn't tear you apart anymore

[Verse 2]
Hello, how are you?
It's so typical of me to talk about myself, I'm sorry
I hope that you're well
Did you ever make it out of that town where nothing ever happened?

[Pre-Chorus]
It's no secret that the both of us
Are running out of time

[Chorus]
So hello from the other side
I must've called a thousand times
To tell you I'm sorry for everything that I've done
But when I call, you never seem to be home
Hello from the outside
At least, I can say that I've tried
To tell you I'm sorry for breaking your heart
But it don't matter, it clearly doesn't tear you apart anymore

[Bridge]
(Highs, highs, highs, highs, lows, lows, lows, lows)
Ooh, anymore
(Highs, highs, highs, highs, lows, lows, lows, lows)
Ooh, anymore
(Highs, highs, highs, highs, lows, lows, lows, lows)
Ooh, anymore
(Highs, highs, highs, highs, lows, lows, lows, lows)
Anymore

[Chorus]
Hello from the other side
I must've called a thousand times
To tell you I'm sorry for everything that I've done
But when I call, you never seem to be home
Hello from the outside
At least, I can say that I've tried
To tell you I'm sorry for breaking your heart
But it don't matter, it clearly doesn't tear you apart anymore

[Produced by Greg Kurstin]
[Music Video]
"""

def search(keywords):
    res = []
    keywords = keywords.split(" ")
    sentences = re.sub("\n", ".", text)
    sentences = re.sub("\[", "", sentences)
    sentences = re.sub("]", "", sentences)
    doc = nlp(sentences)
    for sentence in doc.sents:
        for i, token in enumerate(sentence):
            if len(sentence) - i > len(keywords):
                if match(sentence[i:], keywords):
                    res.append(sentence)
    return res


def match(tokens, keywords):
    testlist = tokens[:len(keywords)]
    for i in range(len(keywords)):
        keywords[i] = str(keywords[i])
        if testlist[i].pos_ == keywords[i]:
            continue
        elif keywords[i].startswith("\"") and keywords[i].endswith("\""):
            if keywords[i][1:-1] != testlist[i].text:
                return False
        elif "+" in keywords[i]:
            word, pos = keywords[i].split("+")
            if testlist[i].pos_ != pos or testlist[i].text != word:
                return False
            else:
                continue
        elif testlist[i].lemma_ != next(nlp(keywords[i]).sents)[0].lemma_:
            return False
    return True

print(search('"breaking" DET heart+NOUN'))
print(search('lower'))






