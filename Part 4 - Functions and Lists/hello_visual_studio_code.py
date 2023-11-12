
"""
Please write a program which asks the user which editor they are using. 
The program should keep on asking until the user types in Visual Studio Code.
"""

# Write your solution here


while True:

    editor = input("Editor: ")
    editor = editor.lower()

    if editor == 'word' or editor == 'notepad':
        print('awful')

    elif editor == 'visual studio code' or editor == 'vscode':
        print('an excellent choice!')
        break

    else:
        print('not good')