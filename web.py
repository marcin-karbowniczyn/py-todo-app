import streamlit as st
import functions
import os
import random

print('            a     aa      a              '.strip())

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

todos = functions.get_todos()


def add_todo(user_input_local):
    todo_local = user_input_local.strip() + '\n'
    todos.append(todo_local)
    functions.write_todos(todos)


st.title('My Todo App')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f'checkbox{index}')
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f'checkbox{index}']
        st.rerun()

with st.form("my_form", clear_on_submit=True):
    user_input = st.text_input(label='Enter a todo that is at least 3 and maximally 30 characters long:',
                               placeholder='Enter a new todo...',
                               key='todo_input')

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        if 3 <= len(user_input.replace(' ', '')) <= 30:
            add_todo(user_input)
            st.rerun()
        else:
            st.error('A todo must contain minimum of 3 and maximum of 30 characters.')

# Check when exactly code app is being refreshed
# st.session_state['random'] = random.randint(1, 100)

# st.session_state
