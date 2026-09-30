"""Command-line interface for the Password Strength Analyzer."""

from getpass import getpass
from password_analyzer import analyze_password


def main() -> None:
    print("=" * 48)
    print("          PASSWORD STRENGTH ANALYZER")
    print("=" * 48)
    print("Your password is analyzed locally and is not stored.\n")

    password = getpass("Enter password: ")
    result = analyze_password(password)

    print(f"\nPassword Strength: {result['strength']}")
    print(f"Score: {result['score']}/100")

    print("\nAnalysis:")
    for item in result["checks"]:
        print(f"  - {item}")

    print("\nRecommendations:")
    for item in result["recommendations"]:
        print(f"  - {item}")


if __name__ == "__main__":
    main()
