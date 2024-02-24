import streamlit as st
from aes import encrypt_aes
from caeser import encrypt_caeser

# Main function to run the Streamlit application
def main():
    st.title("Text Encryption App")
    
    # Text input box for user input
    text_input = st.text_area("Enter your text:")

    # Dropdown box to select encryption method
    encryption_method = st.selectbox("Select Encryption Method", ["AES", "Caesar"])


    if text_input:
        if encryption_method == "AES":
            # Call AES encryption function
            if st.button("Encrypt"):
                encrypted_text,test = encrypt_aes(text_input)
                st.success("Text Encrypted Successfully!")
                st.write("Encrypted Text:", encrypted_text)
                st.write("Generated key:",test)
        elif encryption_method == "Caesar":
            # Call Caesar encryption function
            shift = st.number_input("Enter the key:",step=1)
            if st.button("Encrypt"):
                encrypted_text = encrypt_caeser(text_input, shift)
                st.success("Text Encrypted Successfully!")
                st.write("Encrypted Text:", encrypted_text)
        else:
            st.error("Encryption method not supported yet.")

if __name__ == "__main__":
    main()
