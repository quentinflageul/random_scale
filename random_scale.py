import random

print()
print()

array1 = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]
array2 = ["Major (1, 2, 3, 4, 5, 6, 7)",
          "Minor Harmonic (1, 2, b3, 4, 5, b6, 7)",
          "Minor Melodic (1, 2, b3, 4, 5, 6, 7)",
          "Dorian (1, 2, b3, 4, 5, 6, b7)",
          "Phrygian (1, b2, b3, 4, 5, b6, b7)",
          "Lydian (1, 2, 3, #4, 5, 6, 7)",
          "Mixolydian (1, 2, 3, 4, 5, 6, b7)",
          "Aeolian (1, 2, b3, 4, 5, b6, b7)",
          "Locrian (1, b2, b3, 4, b5, b6, b7)",
          "Dorian b2 - II (1, b2, b3, 4, 5, 6, b7)",
          "Lydian augmented - III (1, 2, 3, #4, #5, 6, 7)",
          "Lydian dominant - IV (1, 2, 3, #4, 5, 6, b7)",
          "Mixolydian b6 - V (1, 2, 3, 4, 5, b6, b7)",
          "Aeolian b5 - VI (1, 2, b3, 4, b5, b6, b7)",
          "Altered scale - VII (1, b2, b3, b4, b5, b6, b7)"]

random_value1 = random.choice(array1)
random_value2 = random.choice(array2)

result = f"     {random_value1} {random_value2}"

print(result)
print()
