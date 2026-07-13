"""
workout_generator.py
Core engine that combines rule-based safety filtering, ML-based safety
scoring, and goal/fitness-level based ranking into a personalised
weekly workout routine for a user with a given injury.
"""

import random
from collections import defaultdict

from exercise_db import EXERCISES
from ml_model import load_model, predict_safety_score

SETS_REPS_TABLE = {
    "beginner":     {"strength": "2 sets x 10-12 reps", "cardio": "10-15 min", "rehab": "2 sets x 12-15 reps", "flexibility": "3 x 20-30 sec hold"},
    "intermediate": {"strength": "3 sets x 10-12 reps", "cardio": "15-25 min", "rehab": "3 sets x 12-15 reps", "flexibility": "3 x 30-45 sec hold"},
    "advanced":     {"strength": "4 sets x 8-12 reps",  "cardio": "25-35 min", "rehab": "3 sets x 15 reps",   "flexibility": "4 x 45 sec hold"},
}

SPLIT_TEMPLATE = {
    3: ["Full Body A", "Full Body B", "Full Body C"],
    4: ["Upper Body", "Lower Body", "Core & Cardio", "Full Body / Rehab"],
    5: ["Push", "Pull", "Legs", "Core & Cardio", "Active Recovery / Rehab"],
}

DAY_FOCUS_MUSCLES = {
    "Full Body A": ["legs", "chest", "core"],
    "Full Body B": ["back", "shoulders", "core"],
    "Full Body C": ["legs", "glutes", "full_body"],
    "Upper Body": ["chest", "back", "shoulders", "triceps", "forearm"],
    "Lower Body": ["legs", "glutes", "calves"],
    "Core & Cardio": ["core", "full_body"],
    "Full Body / Rehab": ["legs", "back", "shoulders", "core"],
    "Push": ["chest", "shoulders", "triceps"],
    "Pull": ["back", "forearm"],
    "Legs": ["legs", "glutes", "calves"],
    "Active Recovery / Rehab": ["neck", "back", "core", "legs", "full_body"],
}


class WorkoutProfile:
    def __init__(self, injury_zone, severity, fitness_level, goal, days_per_week=3):
        self.injury_zone = injury_zone
        self.severity = severity
        self.fitness_level = fitness_level
        self.goal = goal
        self.days_per_week = days_per_week


def get_safe_exercises(profile, clf, min_confidence=0.55):
    tag = f"{profile.injury_zone}_{profile.severity}" if profile.injury_zone != "none" else "none"
    candidates = []

    for ex in EXERCISES:
        if tag in ex["contraindicated_for"]:
            continue

        score = predict_safety_score(clf, ex, profile.injury_zone, profile.severity)
        if score >= min_confidence:
            candidates.append((ex, score))

    candidates.sort(key=lambda pair: pair[1], reverse=True)
    return candidates


def rank_for_goal(candidates, profile):
    ranked = []
    for ex, safety_score in candidates:
        goal_bonus = 0.3 if profile.goal in ex["goal_tags"] else 0
        rehab_tag = f"{profile.injury_zone}_{profile.severity}"
        rehab_bonus = 0.4 if rehab_tag in ex["rehab_for"] else 0
        difficulty_gap = abs(ex["difficulty"] - {"beginner": 1, "intermediate": 2, "advanced": 3}[profile.fitness_level])
        difficulty_penalty = 0.15 * difficulty_gap

        final_score = safety_score + goal_bonus + rehab_bonus - difficulty_penalty
        ranked.append((ex, final_score))

    ranked.sort(key=lambda pair: pair[1], reverse=True)
    return ranked


def generate_weekly_plan(profile):
    clf = load_model()
    candidates = get_safe_exercises(profile, clf)

    if not candidates:
        return {"error": "No safe exercises found for this profile. Please consult a physiotherapist."}

    ranked = rank_for_goal(candidates, profile)

    days = SPLIT_TEMPLATE.get(profile.days_per_week, SPLIT_TEMPLATE[3])
    plan = {}
    used_names = set()

    for day in days:
        focus_muscles = DAY_FOCUS_MUSCLES.get(day, [])
        day_exercises = [pair for pair in ranked if pair[0]["muscle_group"] in focus_muscles
                          and pair[0]["name"] not in used_names]

        if len(day_exercises) < 3:
            day_exercises = [pair for pair in ranked if pair[0]["name"] not in used_names]

        chosen = day_exercises[:5]
        for ex, _ in chosen:
            used_names.add(ex["name"])

        sets_reps_ref = SETS_REPS_TABLE[profile.fitness_level]
        day_plan = []
        for ex, score in chosen:
            goal_for_sets = profile.goal if profile.goal in sets_reps_ref else ex["goal_tags"][0]
            prescription = sets_reps_ref.get(goal_for_sets, "2-3 sets x 10-12 reps")
            day_plan.append({
                "name": ex["name"],
                "muscle_group": ex["muscle_group"],
                "prescription": prescription,
                "equipment": ex["equipment"],
                "suitability_score": round(score, 2),
            })
        plan[day] = day_plan

        if len(used_names) > len(ranked) * 0.7:
            used_names.clear()

    return plan


def print_plan(profile, plan):
    print("=" * 70)
    print("  AI-GENERATED WORKOUT ROUTINE")
    print("=" * 70)
    print(f"Injury zone      : {profile.injury_zone} ({profile.severity})" if profile.injury_zone != "none" else "Injury zone      : None")
    print(f"Fitness level    : {profile.fitness_level}")
    print(f"Goal             : {profile.goal}")
    print(f"Days per week    : {profile.days_per_week}")
    print("=" * 70)

    if "error" in plan:
        print(plan["error"])
        return

    for day, exercises in plan.items():
        print(f"\n--- {day} ---")
        for i, ex in enumerate(exercises, 1):
            print(f"  {i}. {ex['name']:<32} | {ex['prescription']:<22} | "
                  f"equip: {ex['equipment']:<8} | AI suitability score: {ex['suitability_score']}")

    print("\n" + "=" * 70)
    print("Note: This plan is generated by a rule + ML based system for")
    print("educational purposes and does NOT replace professional medical")
    print("or physiotherapy advice.")
    print("=" * 70)
