#-*-coding:utf-8-*-

import streamlit as st
import subprocess



def id_authenticated(username): #괄호 안에 빈칸 있으면 안됨. 괄호의 username은 출력되지 않음. 단순히 return값이랑 대조하는 값임..
    return username == "1234"

def pw_authenticated(password):
    return password == "1234"

def generate_login_block():
    block1 = st.empty()
    block2 = st.empty()
    block3 = st.empty()
    block4 = st.empty()
    return block1, block2, block3, block4

def clean_blocks(blocks):
    for block in blocks:
        block.empty()

def login(blocks):
    blocks[0].markdown("""
        <style>
            input {
                -webkit-text-security: none;
            }
        </style>
        """, unsafe_allow_html=True)

    blocks[0].markdown("""
        <style>
            input {
                -webkit-text-security: none;
            }
        </style>
        """, unsafe_allow_html=True)

    return blocks[1].text_input("Username:"), blocks[3].text_input('Password:', value = "", type = "password")

login_blocks = generate_login_block()
username, password = login(login_blocks)
login_button = st.button("Log In")


if login_button & id_authenticated(username) & pw_authenticated(password):
    st.success("You are logged in")
    subprocess.Popen(["streamlit", "run", "diary.py"])
elif login_button:
    st.error("Please input valid username and/or password")