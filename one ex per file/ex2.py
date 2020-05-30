# part 2
# Task: Break s into sentences (which end in a .), count them and print them out using a loop:
# result: (I truncated them with ...)
# there are 4 sentences:
# Python is an interpreted, high-level, general-purpose programming language
#  Created by Guido van Rossum and first released in 1991, Python ...
#  Its language constructs and object-oriented approach aim to help programmers ...
print("start of part 2") # set breakpoint here
s = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."
# your code here

sen = s.split(".")
print("there are ", len(sen)," sentences:")
for i in sen:
    print(i)


#hi chris, i have a question here: actually there are only 3 sentences in s. I checked the list "sen" I created and I found the last string is an empty one. 
#what's the reason behind it? how can we avoid this? I would like to know your suggestions. thank you!!

print("end of 2") # set breakpoint here 
'''


























s = "Python is an interpreted, high-level, general-purpose programming language."
sentence_list = s.split('.')
print("there are", len(sentence_list), "sentences:")
for e in sentence_list:
    print(e)
'''
