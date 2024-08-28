import streamlit as st # streamlit is a library that is used for web apps

import functions


todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'  # session_state is some kind of dictionary
    todos.append(todo)
    functions.write_todos(todos)


st.title('My Todo App')  # order matters here, which is first and which one is below
st.subheader("This is AlShenzo's Todo app")
st.write('This app is to increase your productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
       todos.pop(index)
       functions.write_todos(todos)
       del st.session_state[todo]
       st.rerun() # we need to we rerun to update the list


st.text_input(label='Enter a todo: ', placeholder="Add here... ",
              on_change=add_todo, key='new_todo')


# http://localhost:8501/
# lines should not be more than 79 characters long
# cause if they are most computer cannot see the IDE
# we create the public URL we need to make sure we have that app in the project of that IDE. So we need a new directory
# Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows
#
# (venv) PS C:\Users\alans\PycharmProjects\webProject1> streamlit run web.py
#
#   You can now view your Streamlit app in your browser.
#
#   Local URL: http://localhost:8501
#   Network URL: http://192.168.1.31:8501
#
# ctrl + c to stop it
#   Stopping...
# (venv) PS C:\Users\alans\PycharmProjects\webProject1> pip freeze > requirements.txt
# the requirements allow the service to know which packages are needed
# essentiall the pip freeze we write the requirements in the requirement txt file