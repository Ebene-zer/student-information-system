print("Welcome to Student info")

#Take user details
full_name = input("Enter your full name: ")
student_id = input("Enter your ID: ")
programme = input("Enter program of study: ")
level = input("Enter your level: ")
age = input("Enter your age: ")
fav_programming_language = input("Which programming language is your favourite? ")

#first 4 letters of name + id to generate student username
username = full_name[:4] + student_id

#generated username + @st.ug.edu.gh to get student email
email = username + "@st.ug.edu.gh"

#line
border_line = "="

#Display everything to user
print(border_line * 50)
print("                 Student info")
print(border_line * 50)

print("Full Name:            " + full_name)
print("Student ID:           " + student_id)
print("Programme:            " + programme) 
print("Level:                " + level)
print("Age:                  " + age)
print("Favourite             " + fav_programming_language)
print("Generated Username:   " + username)
print("Generated Email:      " + email.lower())

print(border_line * 50)


