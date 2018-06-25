import re
#ques1
emails = ["zuck26@facebook.com","page33@google.com","jeff42@amazon.com"]
l=[]

for i in emails:

    x=re.findall("[\w]+",i)
    y=tuple(x)
    l.append(y)
print(l)

#ques2


text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
name=re.findall("([B,b][\w]+)",text)
print(name)


#ques3

sentence = "A, very very; irregular_sentence"
x=re.compile("[,;_]")
y=x.sub("",sentence)
print(y)

#ques4

tweet ="Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstat"
tweet = re.sub('http\S+\s*', '', tweet)
tweet = re.sub('RT|cc', '', tweet)
tweet = re.sub('#\S+', '', tweet)
tweet = re.sub('@\S+', '', tweet)
tweet = re.sub('[%s]' % re.escape(""":!"""), '', tweet)
tweet = re.sub('\s+', ' ', tweet)




print(tweet)
