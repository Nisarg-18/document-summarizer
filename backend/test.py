from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

ARTICLE = """ Problem Identification Report 

Title: IntelliTutor - An Intelligent Tutoring System (ITS) for enhanced learning  

Objective: To research and identify a specific problem or opportunity within the  Intelligent 
Tutoring Systems domain that can be addressed through a software solution. 

Content:  

PROBLEM/OPPORTUNITY STATEMENT: 

The traditional education system  lacks the touch of adaptive learning experience, where the 
student  guides  their  own  education.  Some  students  have  good  grasping  power  and  can 
understand the topic in one go, but some need more than one explanation to understand the 
basics  of  any  particular  topic.  The  traditional  education  system  is  not  a  one-size-fits-all 
approach. Intelligent Tutoring Systems (ITS) addresses the challenge – ‘all people are different’ 
and has the  ability to  develop  personalized learning  bases and  feedback  based on their skill 
level. Another advantage of ITS over traditional systems is its ability to grade assignments or 
exams, reducing the time spent on it by the teacher. This in turn allows the teacher to be more 
available to the students and help them with the confusing material. 

Currently, there are multiple Intelligent tutoring systems present in today’s market, from course 
platforms  like  Coursera,  which  provide  multiple  courses  in  many  domains,  to  Carnegie 
Learning, which acts as a type of one-to-one coach for math, to SAP Litmos, which can be used 
by companies for employee training. Each of these Intelligent tutoring systems are used for a 
specific purpose, and their target audience is limited to a certain domain. IntelliTutor is going 
to be designed in such a way that it can be used by a large group of learners, age range spanning 
for  around  15  years,  and  the  plan  is  to  design  it  in  such  a  way  that  it  can  guide  the  child 
throughout all of their development phases in life.  

Considering  the  current  ITS  available  in  the  market,  though  being  able  to  personalize  the 
content according to the students’ needs and giving the feedback in real-time, they do come 
with  some  limitations.  Firstly,  most  of  the  ITS  are  focused  on  one  specific  subject  in  the 
curriculum which makes it challenging to analyze the overall performance of the student. And 
if there are different ITS for all the subjects, it will become a financial burden for the students. 
The second issue is  that it may reduce the social interaction of the students  with  each other 
which can foster social anxiety among them. And lastly, IntelliTutor will address the language 
barrier by providing tutoring in multiple languages. 
 
"""
print(summarizer(ARTICLE, do_sample=False))
