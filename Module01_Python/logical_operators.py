def check_eligibility(age, nationality):
    nationality = nationality.strip().title()

    if age < 0:
        return "Invalid age entered."

    if age >= 18 and nationality == "Nepal":
        return "Eligible to Vote"
    else:
        return "Not Eligible to Vote"


def main():
    print("=" * 40)
    print("NEPAL VOTER ELIGIBILITY CHECKER")
    print("=" * 40)

    try:
        age = int(input("Enter your age: "))
        nationality = input("Enter your nationality: ")

        result = check_eligibility(age, nationality)

        print("\nResult:")
        print(result)

    except ValueError:
        print("Please enter a valid numeric age.")


if __name__ == "__main__":
    main()