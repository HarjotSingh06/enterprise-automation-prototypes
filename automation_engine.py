
import csv

# The script looks at the exact same local folder for your data
input_file_name = 'students.csv'

print("🔄 Waking up local backend automation engine...")
print("----------------------------------------")

try:
    with open(input_file_name, mode='r') as file:
        csv_reader = csv.DictReader(file)
        
        student_count = 0
        for row in csv_reader:
            student_count += 1
            
            name = row['Name']
            email = row['Email']
            course = row['Course']
            age = int(row['Age'])
            
            # Local Logic Processing Engine
            if '@' not in email:
                status = "❌ REJECTED: Invalid Email Structure"
                assigned_class = "NONE"
            
            elif age < 16:
                status = "⚠️ HOLD: Underage Applicant (Requires Human Review)"
                assigned_class = "NONE"
                
            elif course == "Computing":
                status = "✅ SUCCESS: Enrolled"
                assigned_class = "COMP-A"
                
            elif course == "Automation":
                status = "✅ SUCCESS: Enrolled"
                assigned_class = "AUTO-B"
                
            else:
                status = "⚠️ HOLD: Unknown Course Route"
                assigned_class = "UNKNOWN"
            
            # Print output directly to your local terminal console
            print(f"Student #{student_count} | Name: {name}")
            print(f" -> Allocation: {assigned_class} | Status: {status}")
            print("-" * 40)

    print(f"🚀 Local pipeline complete! Total processed: {student_count} students.")

except FileNotFoundError:
    print(f"Error: Could not find '{input_file_name}' in this local repository folder.")
