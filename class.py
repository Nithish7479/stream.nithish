import streamlit as st
class buttons:
    def __init__(self,num):
        if st.button(f"Button number is{num}"):
            self.calc(num*num)
            
    def calc(self, num):
        if num % 2 == 0:
            st.balloons()
            st.toast("even")
        else:
            st.snow()
            st.toast("odd")
            
for i in range(11):
    buttons(i)
        