from Question import Question

question_prompts=[
    "what color are apples?\n(a) Red\n(b) green\n(c) purple\n(d) Orange\n\n",
    "what color are banana?\n(a) Teal\n(b) Magenta\n(c) green\n(d) Yellow\n\n",
    "what color are strawberries?\n(a) yellow\n(b) red\n(c) purple\n(d) blue\n\n"
]


questions=[
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"d"),
    Question(question_prompts[2],"b"),
]



def run_test(questions):
    print("select one option")
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
            score+=1
    print(f"you got {score}/{len(questions)} correct")

run_test(questions)