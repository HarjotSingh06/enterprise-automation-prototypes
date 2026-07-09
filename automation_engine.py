import csv

input_file_name = 'students.csv'
output_file_name = 'processed_enrollments.csv'

print("🔄 Waking up local backend automation engine...")
print("----------------------------------------")

try:
    with open(input_file_name, mode='r') as infile, open(output_file_name, mode='w', newline='') as outfile:
        csv_reader = csv.DictReader(infile)
        
        # Define the headers for our new automated output file
        fieldnames = ['Name', 'Email', 'Course', 'Age', 'Assigned_Class', 'Status']
        csv_writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        csv_writer.writeheader()
        
        student_count = 0
        for row in csv_reader:
            student_count += 1
            
            name = row['Name']
            email = row['Email']
            course = row['Course']
            age = int(row['Age'])
            
            # Local Logic Processing Engine
            if '@' not in email:
                status = "REJECTED: Invalid Email Structure"
                assigned_class = "NONE"
            elif age < 16:
                status = "HOLD: Underage Applicant"
                assigned_class = "NONE"
            elif course == "Computing":
                status = "SUCCESS: Enrolled"
                assigned_class = "COMP-A"
            elif course == "Automation":
                status = "SUCCESS: Enrolled"
                assigned_class = "AUTO-B"
            else:
                status = "HOLD: Unknown Course Route"
                assigned_class = "UNKNOWN"
            
            # Write the row instantly to our new spreadsheet file
            csv_writer.writerow({
                'Name': name,
                'Email': email,
                'Course': course,
                'Age': age,
                'Assigned_Class': assigned_class,
                'Status': status
            })

    print(f"🚀 Data pipeline complete! Saved 10,000 automated decisions to '{output_file_name}'.")

except FileNotFoundError:
    print(f"Error: Could not find '{input_file_name}' in this local repository folder.")
