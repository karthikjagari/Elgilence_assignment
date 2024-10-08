import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Load the Excel file, specifying that the first row should be the header
file_path = 'C:/Users/dontp/Engilence assignment/Made up date for Kartik.xlsx'  # Replace with the actual path to your Excel file
df = pd.read_excel(file_path, header=1)  # Use the second row (index 1) as the header

# Function to create group performance graphs for specific skill areas
def create_group_performance_by_skill(df, skill):
    # Sort by student names for better readability
    df_sorted = df.sort_values('Name')
    
    # Extract names and the specific skill's scores
    student_names = df_sorted['Name']
    skill_scores = df_sorted[skill]
    
    # Create a larger figure for better name visibility
    plt.figure(figsize=(12, 8))
    
    # Bar graph for skill scores
    plt.bar(student_names, skill_scores, color='skyblue')
    plt.title(f'Group Performance: {skill} Scores', fontsize=16)
    plt.ylabel('Scores', fontsize=12)
    
    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=60, ha='right', fontsize=10)
    
    # Set a clear range for y-axis (0 to 100)
    plt.ylim(0, 100)
    
    # Add value labels above the bars
    for i, score in enumerate(skill_scores):
        plt.text(i, score + 1, str(score), ha='center', fontsize=9)

    plt.tight_layout()

# Generate the graphs and save them directly into a PDF
with PdfPages('group_performance.pdf') as pdf:
    # Create Listening performance page
    create_group_performance_by_skill(df, 'Listening')
    pdf.savefig()  # Save the current figure into the PDF
    plt.close()    # Close the current plot

    # Create Speaking performance page
    create_group_performance_by_skill(df, 'Speaking')
    pdf.savefig()  # Save the current figure into the PDF
    plt.close()

    # Create Writing performance page
    create_group_performance_by_skill(df, 'Writing')
    pdf.savefig()  # Save the current figure into the PDF
    plt.close()

print("PDF generated successfully as 'group_performance.pdf'")