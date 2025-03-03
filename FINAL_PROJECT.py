
import pandas as pd
import matplotlib.pyplot as plt
import os

class QuizSystem:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.total_questions = 0
        self.user_name = ""
        self.user_class = ""
        self.user_data = []
        self.topic = ""

    def show_topic_distribution(self):
        topic_count = {}
        for entry in self.user_data:
            topic = entry["Topic"]
            if topic in topic_count:
                topic_count[topic] += 1
            else:
                topic_count[topic] = 1

        labels = topic_count.keys()
        sizes = topic_count.values()
    
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
        plt.title("Topic Selection Distribution")
        plt.show()

    def show_score_graph(self):
        if not self.user_data:
            print("No user data available.")
            return
        
        topics = ["general_knowledge", "movie_trivia", "programming_concepts"]
        
        for topic in topics:
            topic_scores = [data["Score"] for data in self.user_data if data["Topic"] == topic]
            user_names = [data["Name"] for data in self.user_data if data["Topic"] == topic]
    
            plt.figure()
            plt.bar(user_names, topic_scores)
            plt.xlabel("User Names")
            plt.ylabel("Scores")
            plt.title(f"Scores for {topic.capitalize()} Topic")
            plt.xticks(rotation=45)
            plt.tight_layout()
    
        plt.show()

    def load_questions_from_csv(self, topic):
        file_path = f"{topic}_questions.csv"
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            if not df.empty:
                self.questions = df.to_dict("records")
                for question in self.questions:
                    question["options"] = eval(question["options"])
        else:
            print(f"No questions available for the {topic} topic.")

    def save_questions_to_csv(self, topic):  # Corrected method name
        file_path = f"{topic}_questions.csv"
        df = pd.DataFrame(self.questions)
        df.to_csv(file_path, index=False)


    def add_question(self, topic, question, options, answer):
        self.questions.append({
            "topic": topic,
            "question": question,
            "options": options,
            "answer": answer
        })

    def delete_question(self, topic, question_number):
        questions_in_topic = [q for q in self.questions if q['topic'] == topic]
        if 1 <= question_number <= len(questions_in_topic):
            del self.questions[self.questions.index(questions_in_topic[question_number - 1])]
            print("Question deleted successfully.")
        else:
            print("Invalid question number.")

    def get_user_details(self):
        self.user_name = input("Enter your name: ")
        self.user_class = input("Enter your class: ")

    def display_question(self, q):
        print("Q.)",q["question"])
        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")

    def select_topic(self):
        print("\nSelect a Topic:")
        print("1. General Knowledge")
        print("2. Movie Trivia")
        print("3. Programming Concepts")
        topic_choice = input("Enter your choice (1, 2, or 3): ")

        if topic_choice == "1":
            self.topic = "general_knowledge"
        elif topic_choice == "2":
            self.topic = "movie_trivia"
        elif topic_choice == "3":
            self.topic = "programming_concepts"
        else:
            print("Invalid choice. Starting with General Knowledge.")
            self.topic = "general_knowledge"

        self.load_questions_from_csv(self.topic)
        return self.topic

    def take_quiz(self):
        for q in self.questions:
            self.display_question(q)

            user_choice = input("Enter the number of your answer (1, 2, 3, or 4): ")

            if user_choice.isdigit():
                user_choice = int(user_choice)
                if user_choice >= 1 and user_choice <= 4:
                    if q["answer"] == q["options"][user_choice - 1]:
                        self.score += 1
                    
                else:
                    print("Invalid input. Please enter a valid number.")

        print("\nQuiz completed!")
        print(f"{self.user_name}, you scored {self.score} out of {self.total_questions} in {self.topic} topic.")

        # Save user data to list
        self.user_data.append({
            "Name": self.user_name,
            "Class": self.user_class,
            "Score": self.score,
            "Topic": self.topic
        })

        print("\nSolutions:")
        for i, q in enumerate(self.questions, 1):
            print(f"{i}. {q['question']} - Correct Answer: {q['answer']}")

    def save_user_data_to_csv(self):
        if self.user_data:
            df = pd.DataFrame(self.user_data)
            custom_index = [i + 1 for i in range(len(df))]
            df.index = custom_index
            df.to_csv("user_data.csv", index=False)
            print("User data saved to CSV.")
        else:
            print("No user data to save.")

    def quiz_modification(self):
        while True:
            print("\nQuiz Modification:")
            if not self.topic:
                print("1. Select Topic")
                print("2. Go back to Admin Menu")
                mod_choice = input("Enter your choice (1 or 2): ")
                if mod_choice == "1":
                    self.topic = self.select_topic()
                elif mod_choice == "2":
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")
            else:
                print("1. Add Question to Topic")
                print("2. Delete Question from Topic")
                print("3. Show All Questions in Topic")
                print("4. Save Questions to CSV")
                print("5. Go back to Admin Menu")
                mod_choice = input("Enter your choice (1, 2, 3, 4, or 5): ")

                if mod_choice == "1":
                    question = input("Enter the question: ")
                    options = [input(f"Enter option {i}: ") for i in range(1, 5)]
                    answer = input("Enter the correct option (1, 2, 3, or 4): ")
    
                    if answer.isdigit():
                        answer = int(answer)
                        if 1 <= answer <= 4:
                            self.add_question(self.topic, question, options, options[answer - 1])
                            print("Question added successfully!")
                        else:
                            print("Invalid input. Please enter a number between 1 and 4.")
                    else:
                        print("Invalid input. Please enter a valid number.")
                elif mod_choice == "2":
                    question_number = int(input("Enter the question number to delete: "))
                    self.delete_question(self.topic, question_number)
                elif mod_choice == "3":
                    questions_in_topic = [q for q in self.questions if q['topic'] == self.topic]
                    if not questions_in_topic:
                        print("No questions available for this topic.")
                    else:
                        print(f"\nAll Questions in {self.topic}:")
                        for i, q in enumerate(questions_in_topic, 1):
                            print(f"{i}. {q['question']} - Correct Answer: {q['answer']}")
                elif mod_choice == "4":
                    self.save_questions_to_csv(self.topic)
                    print("Questions saved to CSV.")
                elif mod_choice == "5":
                    self.topic = ""  # Reset topic to empty
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")


    def admin_menu(self, topic):
        self.topic = topic  # Set the 'topic' attribute
        while True:
            print("\nAdmin Menu:")
            print("1. Show User Data")
            print("2. Show Score Graph")
            print("3. Show Topic Distribution")
            print("4. Quiz Modification")
            print("5. Save User Data to CSV")
            print("6. Exit Admin Menu")
            self.topic = "" #Reset the topic before entering the quiz modification loop
            choice = input("Enter your choice (1, 2, 3, 4, or 5): ")

            if choice == "1":
                if not self.user_data:
                    print("No user data available.")
                else:
                    print("\nUser Data:")
                    df = pd.DataFrame(self.user_data)
                    custom_index = [i + 1 for i in range(len(df))]
                    df.index = custom_index
                    print(df)
            elif choice == "2":
                self.show_score_graph()
            elif choice == "3":
                self.show_topic_distribution()
            elif choice == "4":
                self.quiz_modification()
            elif choice == "5":
                self.save_user_data_to_csv()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please enter either 1, 2, 3, or 4.")

    def load_previous_user_data(self):
        if os.path.exists("user_data.csv"):
            df = pd.read_csv("user_data.csv")
            self.user_data = df.to_dict("records")

    def start(self):
        print("Welcome to the Quiz System!")
        while True:
            print("\nOptions:")
            print("1. Play Quiz")
            print("2. Admin Page")
            print("3. Exit")
            choice = input("Enter your choice (1, 2, or 3): ")

            if choice == "1":
                self.topic = self.select_topic()
                self.get_user_details()
                self.total_questions = len(self.questions)
                self.score = 0
                self.take_quiz()
            elif choice == "2":
                admin_choice = input("\nEnter the Admin Password: ")  # Set your admin password here
                if admin_choice == "P&S":
                    self.admin_menu(self.topic)  # Pass 'topic' to the admin_menu
                else:
                    print("Incorrect password. Access denied.")
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please enter either 1, 2, or 3.")

if __name__ == "__main__":
    quiz = QuizSystem()
    quiz.load_previous_user_data()
    quiz.start()

# Source for questions of General Knowledge:- https://www.indiabix.com/general-knowledge/questions-and-answers/
# Source for questions of Movie Trivia:- https://www.jagranjosh.com/general-knowledge/gk-questions-and-answers-on-the-indian-cinema-1549443229-1
# Source for questions of Programming Concepts:- https://www.includehelp.com/mcq/python-mcqs.aspx & https://www.javatpoint.com/python-mcq
