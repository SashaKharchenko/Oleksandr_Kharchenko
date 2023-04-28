from tkinter import *
import json

class QuizGui:

    def __init__(self, gui, questions):

        self.n=len(questions)
        self.frame=gui
        self.count_correct=0
        self.count=0
        self.correct_answers=questions["Answers"]
        self.questions=questions["Questions"]
        self.options=questions["Options"]
        self.user_answer=IntVar()
        self.opts=[]

        startButton=Button(self.frame,text="Start", command=self.start)
        startButton.pack()

        closeButton=Button(self.frame,text="Close", command=self.frame.destroy)
        closeButton.pack()

    def start(self):
        if self.count<len(self.questions):
        
            question_window=Tk()
            self.display_question( question_window,
                                    self.questions[self.count],
                                    self.options[self.count],
                                    self.correct_answers[self.count]
                                    )
            
            question_window.mainloop()
            question_window.destroy()
        else:
            
            result=Label(self.frame,
                         text=f"Your result is {self.count_correct}")
            result.pack()
      
    def display_question(self, question_window, que, opts, ans):

        quiz=Label(question_window,
                   text=que
                   )

        quiz.pack()
        
        for opt in opts:
            radio=Radiobutton(question_window,
                              text=opt,
                              variable=self.user_answer,
                              value=opt
                              )
            
            radio.pack()
            radio.deselect()
        
        nextButton=Button(question_window ,text="next",
                          command=lambda: self.nextButton(question_window))
        nextButton.pack()
        
    def nextButton(self, question_window):
        print(self.user_answer.get())
        if self.user_answer.get()== self.correct_answers[self.count]:
            self.count_correct +=1

        self.count += 1
        question_window.destroy()
        self.start()
if __name__=="__main__":

    fname="quizes.json"
    questions = json.load(open(fname))
    print(questions)

    gui=Tk()
    QuizGui(gui,questions)
    gui.mainloop()
