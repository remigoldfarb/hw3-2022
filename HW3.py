# Your name: Remi Goldfarb
# Your student id: 26407687
# Your email: remgold@umich.edu
# List who you have worked with on this homework:


# import the random module for use in this program
import random

class Fortune_Teller:
    def __init__(self, fortunes_list):
        self.fortunes_list = fortunes_list
        self.questions_list = []
        self.fortunes_history_list = []


def __str__ (self):
    return str(self.fortunes_list)

def get_fortune(self):
    index = random.randint(0, len(self.fortunes_list) - 1)
    self.fortunes_history_list.append(index)
    return self.fortunes_list[index]
  
    
def question_check(self, question):
    for x in range(len(self. questions_list)):
        if question == self.questions_list[x]:
            return "I've already answered that question" 
    self.questions_list.append(question)
    return self.get_fortune()



def print_questions_history(self):
    if len(self.questions_list) == 0:
            print ("None yet")
    else:
        for x in range(len(self.fortunes_history_list)):
            print('[' + str(x) + ']' + self.questions_list[x] + '-' + self.fortunes_list[x] + '\n')
       

def most_common(self, num):
    self.num = num
    end_result = []
    for x in range(self.num):
        end_result.append(self.get_fortune())
    for y in self.fortunes_list:
        common = self.fortunes_list[0]
        current = end_result.count(common)
        final = end_result.count(y)
        print(y + ": " + str(final))
        if final > current:
            current = final
            common = y
    print("The most common frequent answer after " + str(num) + " was " + common)
        
def main():


    fortunes_list = ["Yes", "No", "Ask again", "Maybe", "Not clear"]
    bot = Fortune_Teller(fortunes_list)

    question = input("Ask a question or type quit: ")

    while question != 'quit':
        answer = bot.question_check(question)
        print(question + " - " + answer)
        question = input("Ask a question or type  quit: ") 

def test():

    fortunes_list = ["Yes", "No", "Ask again", "Maybe", "Not clear"]

    print()
    print("Testing Fortune Teller:")
    bot2 = Fortune_Teller(fortunes_list)

    print("Testing the __str__ method")
    print(bot2)
    print()

    print("Printing the history when no answers have been generated yet")
    bot2.print_questions_history()
    print()

    print("Asking the Question: Will I pass this semester?")
    print(bot2.question_check("Will I pass this semester?"))
    print()

    print("Asking the Question: Should I study today?")
    print(bot2.question_check("Should I study today?"))
    print()

    print("Asking the Question: Should I study today? (again)")
    print(bot2.question_check("Should I study today?"))
    print()

    print("Asking the Question: Is SI 206 the best class ever?")
    print(bot2.question_check("Is SI 206 the best class ever?"))
    print()

    print("Printing the history")
    bot2.print_questions_history()
    print()
if __name__ == "__main__":
    main()
    test()