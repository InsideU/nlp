import nltk
from nltk.tokenize import TweetTokenizer
texts = '''
just setting up my twttr
tm help
Wondering if I should quit work and become a monk who secretly writes serial murder thriller novels.
Going to bed.
gary coleman sighting by Zoom. The rumors were true
Festmob. In The Signal premiere. Lotsa buyers. Good luck gang
listening to the pocast net@nite while setting up twitter
watching windows 386 promo video, lol
getting ready for work
going to work
in vista training, this is boring
just came back from supper, now to go back to boring vista training
just finished my last break now for an office 2007 module
i have to get up in 6 hours to drive my sister so i am going to catch some z's
just finished an office 2007 test and got 100%
i am in vista training, yeah another day of it, and this is so dry and boring so half of us are on other sites
lol i work at dell and i do not know how much more microsoft i can take
i jsut finished vista training yeah!!!
Just set up phone connection to twitter.  Am so going to bed now have a long day tomorrow
Mmmmm quad venti caramel macciato with extra caramel  and a shot of vanilla
In shaw looking for family
Holy holy holy is the lord God almighty
Wow she finally finished.....now for elective 1....audio 101
Waiting in longggggggggggg line for food, the only question is what to eat?
Lunch time, yeah!  With cara
Lunch time, yeah!  With friends
Elective 2;  audio 102
Session 3 micing
Supper time!!!! Yeah!!! japanese
I am backstage for a large concert.   Get to watch video production!!!!!!!
Lol technical difficulties and the crowd is singing for joy
Main session is over.  Time to find people
I am sitting waitng for the session......I HATE NEGATIVE SPACE....People  sqeuazing me in
at work, wow i haven't updated in a while...oops!
Discovering twitter in a purple sofa...
Why isn't Wii released in Singapore yet?!
surfing the net
playing around on twitter
At work
Watching the valentine's day pillowfight sans pillow, camera crack'd, feathers in hair, copters o'erhead. Here and not here.
Talking about 24 in the cars, we pass Bauer's  limo service.
Aww, I'm sorry about your camera EC! If it makes you feel better mine cracked on valentine's.'''

for text in texts:
    sentences= nltk.sent_tokenize(text)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(words)
        #print(tagged,end)

#Using the tweet tokenizer 
text1 = 'The pary was soooooo fun :D # superfun'
tw = TweetTokenizer()
print(tw.tokenize(text1))
