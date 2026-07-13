# AI-Generated Workout Routine for Injuries

A hybrid rule-based + machine learning system that generates a personalised, injury-safe weekly workout plan based on injury zone, severity, fitness level, goal, and training days per week.

## How it works

1. Exercise database (src/exercise_db.py) - 30 exercises tagged with muscle group, impact level, difficulty, contraindications, and rehab benefit.
2. Rule-based safety filter - hard-excludes any exercise contraindicated for the user's injury and severity.
3. ML safety-scoring model (src/ml_model.py) - a Random Forest classifier scores exercise suitability.
4. Workout generator (src/workout_generator.py) - ranks safe exercises and builds a day-wise weekly split.
5. CLI (src/main.py) - interactive interface for the end user.

## Run it

pip install -r requirements.txt
cd src
python main.py            (interactive mode)
python main.py --demo     (runs sample profiles, no input needed)

## Disclaimer

This is an academic/educational project. It does not replace advice from a certified physiotherapist or medical professional.
