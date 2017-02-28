import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','TutorForumProject')

import django
django.setup()
from forum.models import Category, Question


 
def populate():

 math_questions= [
 {"title": "How can i differentiate 1/x ",
 "text field":"I'm blanking on my simple rules here whats the derivative of 1/x... i think its 1 but i could be completely wrong here if you can whats the derivative of f(x)= k/x and x/k where k is a constant ",
 "views":10,"upvotes"=14,"downvotes"=2},
 {"title": "How to Integrate [1/(x^2 + 1)] dx?",
 "text_field":"Hi everyone, Can you tell me how to integrate the following equation? ∫ 1 x 2 + 1   d x ∫1x2+1 dx I've tried the substitution method, u = x^2 + 1, du/dx = 2x. But the x variable is still exist. Also, the trigonometry substitution method, but the denominator is not in √ x 2 + 1 x2+1 form. Thanks in advance",
 "views":3,"upvotes"=1,"downvotes"=1},]
 
 
  Physics_questions= [
 {"title": "Momentum ",
 "text_field":"Can you please remind me the proof of the formula for momentum? i am stack",
 "views":14,"upvotes"=13,"downvotes"=2},
 ]
 
  Computer_questions= [
 {"title": "WAD2 assesed 2 ",
 "text_field":"When is the deadline for assesed 2? Thanks",
 "views":20,"upvotes"=1,"downvotes"=12},
 ]



 categories = {"Maths": {"questions": math_questions},"Physics": {"questions":  Physics_questions},"Computer Science": {"pages": other_pages} }


 for category, category_data in categories.items():
     c = add_cat(category)
     for q in cat_data["questions"]:
         add_question(c, q["title"], q["text_field"],q["views"],q["upvotes"],q["downvotes"])



         
 # Print out the categories we have added.
 for c in Category.objects.all():
     for q in Question.objects.filter(category=c):
         print("- {0} - {1}".format(str(c), str(q)))



def add_question(category, title, text_field,views,upvotes,downvotes])
    q = Question.objects.get_or_create(category=cat, title=title)[0]
    q.text_field=text_field
    q.views=views
	q.upvotes=upvotes
	q.downvotes=downvotes
    q.save()
    return q

def add_cat(name):
    c = Category.objects.get_or_create(title=name)[0]
    c.save()
    return c


 # Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
