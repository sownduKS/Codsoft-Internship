# Rule-Based Placement and Career Guidance Chatbot

print("=" * 60)
print("WELCOME TO THE CAREER GUIDANCE CHATBOT")
print("=" * 60)

name = input("Enter your name: ")

print(f"\nHello {name}! I am your Career Guidance Chatbot.")
print("You can ask me about:")
print("- Resume")
print("- Interview")
print("- AI")
print("- Web Development")
print("- Data Science")
print("- Cyber Security")
print("- Projects")
print("- Certifications")
print("- Skills")
print("- Internship")
print("Type 'bye' to exit.\n")

# Create chat history file
file = open("chat_history.txt", "a")
file.write(f"\n\n===== New Session : {name} =====\n")
file.close()

while True:

    user_input = input(f"{name}: ").lower()

    # Save user message
    file = open("chat_history.txt", "a")
    file.write(f"{name}: {user_input}\n")
    file.close()

    if user_input in ["hi", "hello", "hey"]:

        response = f"Hello {name}! How can I help you today?"

    elif "resume" in user_input:

        response = """
Resume Tips:
• Keep your resume to one page.
• Highlight projects and internships.
• Mention technical skills clearly.
• Use a professional format.
• Avoid spelling mistakes.
"""

    elif "interview" in user_input:

        response = """
Interview Preparation Tips:
• Practice self introduction.
• Revise core subjects.
• Prepare HR questions.
• Practice coding problems.
• Attend mock interviews.
"""

    elif "aptitude" in user_input:

        response = """
Aptitude Preparation:
• Percentages
• Profit and Loss
• Time and Work
• Number Series
• Logical Reasoning
"""

    elif "ai" in user_input or "artificial intelligence" in user_input:

        response = """
AI Roadmap:
1. Learn Python
2. Learn NumPy and Pandas
3. Learn Machine Learning
4. Learn Deep Learning
5. Build AI Projects
"""

    elif "web" in user_input:

        response = """
Web Development Roadmap:
1. HTML
2. CSS
3. JavaScript
4. React
5. Backend Development
"""

    elif "data science" in user_input:

        response = """
Data Science Roadmap:
1. Python
2. Statistics
3. SQL
4. Data Visualization
5. Machine Learning
"""

    elif "cyber" in user_input:

        response = """
Cyber Security Roadmap:
1. Networking
2. Linux
3. Ethical Hacking
4. Security Tools
5. Penetration Testing
"""

    elif "project" in user_input:

        response = """
Project Ideas:
• Chatbot
• Recommendation System
• Face Detection
• Library Management System
• Student Management System
"""

    elif "skill" in user_input:

        response = """
Important Skills:
• Communication
• Problem Solving
• Python
• Teamwork
• Time Management
"""

    elif "certification" in user_input:

        response = """
Useful Certifications:
• Google Data Analytics
• AWS Cloud Practitioner
• Microsoft Azure Fundamentals
• Python Certifications
"""

    elif "internship" in user_input:

        response = """
Internship Tips:
• Build projects
• Improve coding skills
• Create LinkedIn profile
• Keep resume updated
• Apply consistently
"""

    elif "thank" in user_input:

        response = "You're welcome! Happy to help."

    elif user_input in ["bye", "exit", "quit"]:

        response = f"Goodbye {name}! All the best for your career."

        print("\nBot:", response)

        file = open("chat_history.txt", "a")
        file.write("Bot: " + response + "\n")
        file.close()

        break

    else:

        response = """
Sorry, I didn't understand that.

Try asking about:
Resume
Interview
AI
Web Development
Data Science
Cyber Security
Projects
Skills
Internship
"""

    print("\nBot:", response)

    file = open("chat_history.txt", "a")
    file.write("Bot: " + response + "\n")
    file.close()