"""
main.py
Command-line interface for the AI-Generated Workout Routine for Injuries system.

Run: python main.py
"""

from exercise_db import INJURY_ZONES, SEVERITY_LEVELS, GOALS, FITNESS_LEVELS
from workout_generator import WorkoutProfile, generate_weekly_plan, print_plan


def ask_choice(prompt, options):
    print(f"\n{prompt}")
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    while True:
        choice = input(f"Enter choice [1-{len(options)}]: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print("Invalid input, try again.")


def run_cli():
    print("Welcome to the AI-Generated Workout Routine for Injuries system\n")

    injury_zone = ask_choice("Select your injury area:", INJURY_ZONES)
    severity = "mild"
    if injury_zone != "none":
        severity = ask_choice("Select injury severity:", SEVERITY_LEVELS)

    fitness_level = ask_choice("Select your fitness level:", FITNESS_LEVELS)
    goal = ask_choice("Select your primary goal:", GOALS)
    days_choice = ask_choice("How many workout days per week?", ["3", "4", "5"])

    profile = WorkoutProfile(
        injury_zone=injury_zone,
        severity=severity,
        fitness_level=fitness_level,
        goal=goal,
        days_per_week=int(days_choice),
    )

    plan = generate_weekly_plan(profile)
    print_plan(profile, plan)


def run_demo():
    """Non-interactive demo used for report screenshots / testing."""
    demo_profiles = [
        WorkoutProfile("knee", "moderate", "beginner", "rehab", 3),
        WorkoutProfile("shoulder", "mild", "intermediate", "strength", 4),
        WorkoutProfile("none", "mild", "advanced", "cardio", 5),
    ]
    for profile in demo_profiles:
        plan = generate_weekly_plan(profile)
        print_plan(profile, plan)
        print("\n\n")


if __name__ == "__main__":
    import sys
    if "--demo" in sys.argv:
        run_demo()
    else:
        run_cli()
