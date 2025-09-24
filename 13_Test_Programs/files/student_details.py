import csv

def calculate_average(csv_file):
    total_marks = 0
    student_count = 0

    try:
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            
            # Skip header if exists
            header = next(reader, None)
            if header and "name" in header[0].lower():
                pass  # header exists, already skipped
            
            for row in reader:
                if len(row) >= 2:
                    try:
                        marks = float(row[1])
                        total_marks += marks
                        student_count += 1
                    except ValueError:
                        print(f"Skipping invalid marks: {row[1]}")
        
        if student_count == 0:
            print("No valid student records found.")
            return 0
        
        average = total_marks / student_count
        return average
    
    except FileNotFoundError:
        print(f"CSV file '{csv_file}' not found!")
        return 0

# Example usage
csv_filename = "students.csv"  # CSV file should have format: Name,Marks
average_marks = calculate_average(csv_filename)
print(f"Average Marks: {average_marks:.2f}")
