from sys import argv


script, user_name= argv
prompt='> '
print(f"Hi {user_name} , I'm the {script} script.")
print("I have some questions.")
print(f"Are you OK??")
OK= input(prompt)

print("Where do you live {user_name}??")
live= input(prompt)
print("What kind of computer do you have??")
computer= input(prompt)

print(f"""
      Alright, so you said {OK} when asked you how are you.
      You live in{live}. Not sure where that is.
      And you have a {computer} computer. Nice
      """)