"""
exercise_db.py
Master exercise database for the AI-Generated Workout Routine system.

Each exercise is tagged with:
  - muscle_group   : primary body part trained
  - goal_tags      : which fitness goals it serves (strength, cardio, flexibility, rehab)
  - difficulty     : 1 (beginner) - 3 (advanced)
  - impact_level   : "low", "medium", "high"  -> joint/tissue stress
  - contraindicated_for : list of injury zones where this exercise is UNSAFE
  - rehab_for      : list of injury zones this exercise actively HELPS rehabilitate
  - equipment      : equipment needed
"""

EXERCISES = [
    # ---------------- LOWER BODY ----------------
    dict(name="Bodyweight Squat", muscle_group="legs", goal_tags=["strength", "rehab"],
         difficulty=1, impact_level="low", contraindicated_for=["knee_severe"],
         rehab_for=["knee_mild"], equipment="none"),
    dict(name="Barbell Back Squat", muscle_group="legs", goal_tags=["strength"],
         difficulty=3, impact_level="high", contraindicated_for=["knee_mild", "knee_moderate", "knee_severe", "lower_back_moderate", "lower_back_severe"],
         rehab_for=[], equipment="barbell"),
    dict(name="Wall Sit", muscle_group="legs", goal_tags=["strength", "rehab"],
         difficulty=1, impact_level="low", contraindicated_for=["knee_severe"],
         rehab_for=["knee_mild", "knee_moderate"], equipment="none"),
    dict(name="Straight Leg Raise", muscle_group="legs", goal_tags=["rehab"],
         difficulty=1, impact_level="low", contraindicated_for=[],
         rehab_for=["knee_mild", "knee_moderate", "knee_severe"], equipment="none"),
    dict(name="Glute Bridge", muscle_group="glutes", goal_tags=["strength", "rehab"],
         difficulty=1, impact_level="low", contraindicated_for=[],
         rehab_for=["lower_back_mild", "lower_back_moderate"], equipment="none"),
    dict(name="Walking Lunge", muscle_group="legs", goal_tags=["strength", "cardio"],
         difficulty=2, impact_level="medium", contraindicated_for=["knee_moderate", "knee_severe", "ankle_moderate", "ankle_severe"],
         rehab_for=[], equipment="none"),
    dict(name="Calf Raise", muscle_group="calves", goal_tags=["strength", "rehab"],
         difficulty=1, impact_level="low", contraindicated_for=["ankle_severe"],
         rehab_for=["ankle_mild", "ankle_moderate"], equipment="none"),
    dict(name="Box Jump", muscle_group="legs", goal_tags=["cardio", "strength"],
         difficulty=3, impact_level="high", contraindicated_for=["knee_mild", "knee_moderate", "knee_severe", "ankle_mild", "ankle_moderate", "ankle_severe", "lower_back_moderate", "lower_back_severe"],
         rehab_for=[], equipment="box"),
    dict(name="Seated Leg Extension (light)", muscle_group="legs", goal_tags=["rehab"],
         difficulty=1, impact_level="low", contraindicated_for=["knee_severe"],
         rehab_for=["knee_mild", "knee_moderate"], equipment="machine"),
    dict(name="Ankle Alphabet", muscle_group="calves", goal_tags=["rehab", "flexibility"],
         difficulty=1, impact_level="low", contraindicated_for=[],
         rehab_for=["ankle_mild", "ankle_moderate", "ankle_severe"], equipment="none"),

    # ---------------- UPPER BODY - PUSH ----------------
    dict(name="Push-up", muscle_group="chest", goal_tags=["strength"],
         difficulty=2, impact_level="medium", contraindicated_for=["wrist_moderate", "wrist_severe", "shoulder_severe"],
         rehab_for=[], equipment="none"),
    dict(name="Incline Push-up", muscle_group="chest", goal_tags=["strength", "rehab"],
         difficulty=1, impact_level="low", contraindicated_for=["wrist_severe"],
         rehab_for=["shoulder_mild"], equipment="bench"),
    dict(name="Overhead Dumbbell Press", muscle_group="shoulders", goal_tags=["strength"],
         difficulty=2, impact_level="medium", contraindicated_for=["shoulder_mild", "shoulder_moderate", "shoulder_severe", "neck_moderate", "neck_severe"],
         rehab_for=[], equipment="dumbbell"),
    dict(name="Resistance Band Pull-apart", muscle_group="shoulders", goal_tags=["rehab", "strength"],
         difficulty=1, impact_level="low", contraindicated_for=[],
         rehab_for=["shoulder_mild", "shoulder_moderate"], equipment="band"),
    dict(name="Pendulum Swing", muscle_group="shoulders", goal_tags=["rehab"],
         difficulty=1, impact_level="low", contraindicated_for=[],
         rehab_for=["shoulder_mild", "shoulder_moderate", "shoulder_severe"], equipment="none"),
    dict(name="Triceps Dip (bench)", muscle_group="triceps", goal_tags=["strength"],
         difficulty=2, impact_level="medium", contraindicated_for=["shoulder_moderate", "shoulder_severe", "wrist_moderate", "wrist_severe"],
         rehab_for=[], equipment="bench"),

    # ---------------- UPPER BODY - PULL ----------------
    dict(name="Resistance Band Row", muscle_group="back", goal_tags=["strength", "rehab"],
         difficulty=1, impact_level="low", contraindicated_for=[],
         rehab_for=["shoulder_mild", "lower_back_mild"], equipment="band"),
    dict(name="Bent-over Barbell Row", muscle_group="back", goal_tags=["strength"],
         difficulty=3, impact_level="high", contraindicated_for=["lower_back_mild", "lower_back_moderate", "lower_back_severe", "wrist_moderate", "wrist_severe"],
         rehab_for=[], equipment="barbell"),
    dict(name="Lat Pulldown (light)", muscle_group="back", goal_tags=["strength"],
         difficulty=2, impact_level="low", contraindicated_for=["shoulder_severe"],
         rehab_for=[], equipment="machine"),
    dict(name="Wrist Curl (light band)", muscle_group="forearm", goal_tags=["rehab"],
         difficulty=1, impact_level="low", contraindicated_for=["wrist_severe"],
         rehab_for=["wrist_mild", "wrist_moderate"], equipment="band"),

    # ---------------- CORE ----------------
    dict(name="Plank", muscle_group="core", goal_tags=["strength", "rehab"],
         difficulty=1, impact_level="low", contraindicated_for=["wrist_moderate", "wrist_severe", "lower_back_severe"],
         rehab_for=["lower_back_mild"], equipment="none"),
    dict(name="Dead Bug", muscle_group="core", goal_tags=["rehab", "strength"],
         difficulty=1, impact_level="low", contraindicated_for=[],
         rehab_for=["lower_back_mild", "lower_back_moderate"], equipment="none"),
    dict(name="Bird Dog", muscle_group="core", goal_tags=["rehab", "strength"],
         difficulty=1, impact_level="low", contraindicated_for=[],
         rehab_for=["lower_back_mild", "lower_back_moderate"], equipment="none"),
    dict(name="Sit-up", muscle_group="core", goal_tags=["strength"],
         difficulty=2, impact_level="medium", contraindicated_for=["neck_moderate", "neck_severe", "lower_back_moderate", "lower_back_severe"],
         rehab_for=[], equipment="none"),
    dict(name="Cat-Cow Stretch", muscle_group="core", goal_tags=["flexibility", "rehab"],
         difficulty=1, impact_level="low", contraindicated_for=[],
         rehab_for=["lower_back_mild", "lower_back_moderate", "neck_mild"], equipment="none"),

    # ---------------- CARDIO ----------------
    dict(name="Brisk Walking", muscle_group="full_body", goal_tags=["cardio", "rehab"],
         difficulty=1, impact_level="low", contraindicated_for=["ankle_severe"],
         rehab_for=["knee_mild", "ankle_mild"], equipment="none"),
    dict(name="Stationary Cycling (light resistance)", muscle_group="legs", goal_tags=["cardio", "rehab"],
         difficulty=1, impact_level="low", contraindicated_for=["knee_severe"],
         rehab_for=["knee_mild", "knee_moderate"], equipment="bike"),
    dict(name="Swimming / Water Walking", muscle_group="full_body", goal_tags=["cardio", "rehab"],
         difficulty=1, impact_level="low", contraindicated_for=[],
         rehab_for=["knee_mild", "knee_moderate", "knee_severe", "ankle_mild", "ankle_moderate", "lower_back_mild", "lower_back_moderate"], equipment="pool"),
    dict(name="Jump Rope", muscle_group="full_body", goal_tags=["cardio"],
         difficulty=2, impact_level="high", contraindicated_for=["knee_mild", "knee_moderate", "knee_severe", "ankle_mild", "ankle_moderate", "ankle_severe"],
         rehab_for=[], equipment="rope"),
    dict(name="Running (moderate pace)", muscle_group="full_body", goal_tags=["cardio"],
         difficulty=2, impact_level="high", contraindicated_for=["knee_moderate", "knee_severe", "ankle_moderate", "ankle_severe", "lower_back_moderate", "lower_back_severe"],
         rehab_for=[], equipment="none"),

    # ---------------- FLEXIBILITY / NECK ----------------
    dict(name="Neck Rotation Stretch", muscle_group="neck", goal_tags=["flexibility", "rehab"],
         difficulty=1, impact_level="low", contraindicated_for=["neck_severe"],
         rehab_for=["neck_mild", "neck_moderate"], equipment="none"),
    dict(name="Chin Tuck", muscle_group="neck", goal_tags=["rehab"],
         difficulty=1, impact_level="low", contraindicated_for=[],
         rehab_for=["neck_mild", "neck_moderate", "neck_severe"], equipment="none"),
    dict(name="Hamstring Stretch", muscle_group="legs", goal_tags=["flexibility", "rehab"],
         difficulty=1, impact_level="low", contraindicated_for=[],
         rehab_for=["lower_back_mild", "knee_mild"], equipment="none"),
    dict(name="Child's Pose", muscle_group="back", goal_tags=["flexibility", "rehab"],
         difficulty=1, impact_level="low", contraindicated_for=["knee_severe"],
         rehab_for=["lower_back_mild", "lower_back_moderate"], equipment="none"),
]

INJURY_ZONES = ["knee", "shoulder", "lower_back", "ankle", "wrist", "neck", "none"]
SEVERITY_LEVELS = ["mild", "moderate", "severe"]
GOALS = ["strength", "cardio", "flexibility", "rehab"]
FITNESS_LEVELS = ["beginner", "intermediate", "advanced"]
