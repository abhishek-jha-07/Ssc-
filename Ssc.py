print("Welcome To SSC { Student System Controller }\n")

students = []


def choose():
    print("\n" + "=" * 35)
    print("1. Add student")
    print("2. Show all")
    print("3. Search by Roll no.")
    print("4. Show Topper")
    print("5. Exit")
    print("=" * 35)

    try:
        return int(input("Input :- "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        return 0


def add_student():
    name = input("Enter student name: ").strip()

    try:
        roll = int(input("Enter roll no: "))
        science = float(input("Enter science marks: "))
        math = float(input("Enter math marks: "))
        hindi = float(input("Enter hindi marks: "))
    except ValueError:
        print("Invalid number entered! Operation cancelled.")
        return

    total = science + math + hindi
    percentage = total / 3

    student = {
        "name": name,
        "roll": roll,
        "science": science,
        "math": math,
        "hindi": hindi,
        "total": total,
        "percentage": percentage,
    }

    students.append(student)
    print(f"\nData successfully stored for {name}!")


def show_all():
    if not students:
        print("\nNo student records found.")
        return

    print("\n--- All Student Records ---")
    for s in students:
        print(
            f"Name: {s['name']} | Roll: {s['roll']} | Science: {s['science']} | "
            f"Math: {s['math']} | Hindi: {s['hindi']} | Total: {s['total']} | %: {s['percentage']:.2f}"
        )


def search_by_roll():
    if not students:
        print("\nNo student records found.")
        return

    try:
        roll_search = int(input("Enter Roll No to search: "))
    except ValueError:
        print("Invalid Roll Number.")
        return

    for s in students:
        if s["roll"] == roll_search:
            print(
                f"\nFound Record -> Name: {s['name']} | Science: {s['science']} | "
                f"Math: {s['math']} | Hindi: {s['hindi']} | Total: {s['total']} | %: {s['percentage']:.2f}"
            )
            return

    print(f"No student found with Roll No: {roll_search}")


def show_topper():
    if not students:
        print("\nNo student records found.")
        return

    topper = max(students, key=lambda s: s["total"])
    print(f"\n--- TOPPER ---")
    print(
        f"Name: {topper['name']} | Roll: {topper['roll']} | Total: {topper['total']} | %: {topper['percentage']:.2f}"
    )


# Main Application Loop
def main():
    while True:
        choice = choose()

        if choice == 1:
            add_student()
        elif choice == 2:
            show_all()
        elif choice == 3:
            search_by_roll()
        elif choice == 4:
            show_topper()
        elif choice == 5:
            print("\nThanks For Using SSC... Goodbye!")
            break


if __name__ == "__main__":
    main()
                  
