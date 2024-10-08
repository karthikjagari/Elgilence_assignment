import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Load the Excel file
file_path = 'C:/Users/dontp/Engilence assignment/Made up date for Kartik.xlsx'  # Replace with the actual path to your Excel file
df = pd.read_excel(file_path, header=1)  # Use the second row (index 1) as the header

# Function to create individual performance graphs for each student and save them to a PDF
def create_individual_performance_pdf(df):
    with PdfPages('individual_performance.pdf') as pdf:
        for index, row in df.iterrows():
            student_name = row['Name']

            # LSRW Scores
            lsrw_scores = {
                'Listening': row['Listening'],
                'Speaking': row['Speaking'],
                'Writing': row['Writing'],
                'Written Grammar': row['Written Grammar']
            }

            # Listening Sub-scores
            listening_subscores = {
                'Speed': row['Speed'],
                'Fluency': row['Fluency'],
                'Intonation': row['Intonation'],
                'Pronunciation': row['Pronunciation'],
            }

            # Writing Skills
            writing_skills = {
                'Comprehension': row['Comprehension'],
                'Written Grammar': row['Written Grammar'],
            }

            # Create a figure
            plt.figure(figsize=(10, 12))

            # Bar graph for LSRW Scores
            plt.subplot(3, 1, 1)
            plt.bar(lsrw_scores.keys(), lsrw_scores.values(), color='blue')
            plt.title(f'Individual Performance: LSRW Scores ({student_name})')
            plt.ylabel('Scores')
            plt.ylim(0, 100)  # Set y-axis limit for better visualization

            # Bar graph for Listening Sub-scores
            plt.subplot(3, 1, 2)
            plt.bar(listening_subscores.keys(), listening_subscores.values(), color='green')
            plt.title(f'Individual Performance: Listening Sub-scores ({student_name})')
            plt.ylabel('Scores')
            plt.ylim(0, 100)  # Set y-axis limit for better visualization

            # Bar graph for Writing Skills
            plt.subplot(3, 1, 3)
            plt.bar(writing_skills.keys(), writing_skills.values(), color='orange')
            plt.title(f'Individual Performance: Writing Skills ({student_name})')
            plt.ylabel('Scores')
            plt.ylim(0, 100)  # Set y-axis limit for better visualization

            # Adjust layout and save to PDF
            plt.tight_layout()
            pdf.savefig()  # Save the current figure to the PDF
            plt.close()  # Close the figure to avoid memory issues

        print(f"Individual performance PDF created for all students.")

# Call the function to generate the PDF
create_individual_performance_pdf(df)