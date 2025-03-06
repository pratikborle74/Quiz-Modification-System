# 🧠 Quiz System  

## 📌 Overview  
The **Quiz System** is a Python-based interactive multiple-choice quiz application designed for users to test their knowledge across different topics. This system provides **an admin dashboard, score visualization, user data management, and quiz modification** functionalities.  

The application supports the following quiz categories:  
- **General Knowledge**  
- **Movie Trivia**  
- **Programming Concepts**  

It uses **CSV files** for data storage and **Matplotlib** for graphical visualization, offering a structured approach to quiz-based learning and assessment.

---

## 🚀 Features  

✅ **Interactive Quiz Gameplay** – Users can take quizzes from different categories.  
✅ **User Score Management** – Tracks user details, quiz attempts, and performance.  
✅ **Admin Panel** – Allows authorized users to modify quizzes and analyze data.  
✅ **Question Management** – Add, delete, or update quiz questions stored in CSV files.  
✅ **Data Persistence** – User progress and quiz questions are saved for future sessions.  
✅ **Graphical Score Visualization** – Generates **bar charts** and **pie charts** for user insights.  

---

## 📂 Project Structure  

```
📁 QuizSystem/
│── 📜 quiz_system.py           # Main script to run the quiz system
│── 📜 general_knowledge_questions.csv  
│── 📜 movie_trivia_questions.csv  
│── 📜 programming_concepts_questions.csv  
│── 📜 user_data.csv            # Stores quiz scores and user details
│── 📜 requirements.txt         # Dependencies list
│── 📜 LICENSE                  # License file
│── 📜 README.md                # Documentation file
```

---

## 🔧 Installation  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-username/quiz-system.git
cd quiz-system
```

### **2️⃣ Install Dependencies**  
Ensure you have **Python 3.7+** installed. Then, install the required dependencies using:  
```bash
pip install -r requirements.txt
```
Or manually install required libraries:  
```bash
pip install pandas matplotlib
```

### **3️⃣ Run the Application**  
```bash
python quiz_system.py
```

---

## 🎮 How to Use  

### 🔹 **User Mode**  
1️⃣ **Select a topic**:  
   - General Knowledge  
   - Movie Trivia  
   - Programming Concepts  

2️⃣ **Answer multiple-choice questions** with four answer options.  
3️⃣ **Receive instant feedback** and view correct answers.  
4️⃣ **Scores are saved** for performance tracking.  

### 🔹 **Admin Mode** *(Password: `P&S`)*  
1️⃣ **View and manage user data**.  
2️⃣ **Modify quiz content** (add/delete/update questions).  
3️⃣ **Visualize score distribution** through **graphs and charts**.  
4️⃣ **Save user data for analysis**.  

---

## 📊 Data Visualization  

The system provides graphical insights using **Matplotlib**:  

📌 **Score Graphs** – Displays user performance by topic.  
📌 **Topic Distribution** – Shows the most selected topics via pie charts.  

Example code snippet for visualization:  
```python
import matplotlib.pyplot as plt
plt.bar(user_names, topic_scores)
plt.xlabel("Users")
plt.ylabel("Scores")
plt.title("General Knowledge Quiz Scores")
plt.show()
```

---

## 📜 Data Sources  

The quiz questions are sourced from **reliable educational platforms**:  

- **General Knowledge**: [IndiaBix](https://www.indiabix.com/general-knowledge/questions-and-answers/)  
- **Movie Trivia**: [JagranJosh](https://www.jagranjosh.com/general-knowledge/gk-questions-and-answers-on-the-indian-cinema-1549443229-1)  
- **Programming Concepts**:  
  - [IncludeHelp](https://www.includehelp.com/mcq/python-mcqs.aspx)  
  - [JavaTpoint](https://www.javatpoint.com/python-mcq)  

---

## 🛠 Technologies Used  

- **Python** – Core programming language  
- **Pandas** – Data processing and storage  
- **Matplotlib** – Data visualization  
- **CSV** – Data storage format  

---

## 🔒 Admin Access  

The **Admin Panel** enables advanced features and requires authentication.  

**Admin Password**:  
```plaintext
P&S
```

### 🔹 **Admin Panel Features**  

- **User Data Analysis** – View and manage user quiz history.  
- **Quiz Modification** – Add, remove, and modify quiz questions.  
- **Performance Graphs** – Display scores in bar and pie charts.  

Example function for admin access:  
```python
def admin_menu():
    password = input("Enter Admin Password: ")
    if password == "P&S":
        print("Access Granted!")
    else:
        print("Incorrect Password!")
```

---

## 🌟 Future Enhancements  

🔹 **Web-Based UI** – Convert the CLI system to a web-based application.  
🔹 **Expanded Quiz Topics** – Add new categories like Science, History, and Sports.  
🔹 **User Authentication** – Implement user login and profile management.  
🔹 **Leaderboard System** – Introduce ranking for top-performing users.  

---

## 👨‍💻 Author  

**Pratik Borle**  
📧 Email: pratikborle64@gmail.com
🔗 GitHub: pratikborle74 (https://github.com/pratikborle74) 

---

## 📄 License  

This project is **open-source** under the [MIT License](LICENSE).  

```
MIT License

Permission is granted to use, copy, modify, and distribute this software for any purpose.
```

---

### ⭐ **If you find this project useful, please Star ⭐ the repository!**  
