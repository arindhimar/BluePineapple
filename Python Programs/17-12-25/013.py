s = "In computer science, artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of 'intelligent agents': any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals. Colloquially, the term 'artificial intelligence' is often used to describe machines that mimic cognitive functions that humans associate with the human mind, such as learning and problem solving. As machines become increasingly capable, tasks considered to require 'intelligence' are often removed from the definition of AI, a phenomenon known as the AI effect."

wordCount={}

splitWord=s.split(" ")

for word in splitWord:
    if word in wordCount:
        wordCount[word]=wordCount[word]+1
    else:
        wordCount[word]=1
        
    
rev_count={key:value for key, value in sorted(wordCount.items(), key=lambda item: item[1], reverse=True)}

print(list(rev_count.keys())[0])