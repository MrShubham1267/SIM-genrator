import streamlit as st
import pandas as pd

# Function to read SIM numbers from Excel
def read_sim_data():
    df = pd.read_excel('sims.xlsx')  # Update with your Excel file path
    sims = df['SIM'].tolist()  # Assuming 'SIM' is the column header
    return sims

# Function to delete a SIM number from Excel
def delete_sim(sim):
    df = pd.read_excel('sims.xlsx')  # Update with your Excel file path
    df = df[df['SIM'] != sim]
    df.to_excel('sims.xlsx', index=False)

def main():
    st.title('SIM Viewer and Deleter')

    sims = read_sim_data()

    if not sims:
        st.write("No SIMs left.")
    else:
        current_sim = sims[0]
        st.write(f"Current SIM: {current_sim}")
        if st.button('Delete'):
            delete_sim(current_sim)
            st.write("Deleted successfully!")
            # Refresh the SIM list after deletion
            sims = read_sim_data()

    if st.button('Refresh'):
        if sims:
            current_sim = sims[0]
            #st.write(f"Current SIM: {current_sim}")
            sims.pop(0)  # Remove the first SIM number
            if not sims:
                st.write("No SIMs left.")
            #else:
                #st.write("Remaining SIMs:", sims)
        else:
            st.write("No SIMs left.")

if __name__ == "__main__":
    main()
