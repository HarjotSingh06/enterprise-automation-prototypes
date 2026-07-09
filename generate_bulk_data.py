
import csv
import random

output_file = "students.csv"
total_students = 10000

courses = ["Computing", "Automation", "Business", "Unknown"]
domains = ["email.com", "gmail.com", "invalid-email", "student.ac.uk"]

print(f"⚡ Generating {total_students} mock student records automatically...")

# Open the file and write the headers
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Email", "Course", "Age"])
    
    # Run a loop 10,000 times to create the rows instantly
    for i in range(1, total_students + 1):
        name = f"Student_{i}"
        
        # Randomly break some emails to test our engine's validation logic
        domain = random.choice(domains)
        email = f"user_{i}@{domain}" if domain != "invalid-email" else f"user_{i}.email.com"
        
        course = random.choice(courses)
        age = random.randint(14, 45) # Generates random ages between 14 and 45
        
        writer.writerow([name, email, course, age])

print(f"✅ Successfully wrote 10,000 records directly into '{output_file}'!")
