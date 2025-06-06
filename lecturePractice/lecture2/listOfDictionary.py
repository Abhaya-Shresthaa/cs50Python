students = [
    {"name": "Abhaya", "caste": "Shrestha", "shortCut": "AS"},
    {"name": "Chandan", "caste": "Shah", "shortCut": "CS"},
    {"name": "Kushal", "caste": "Regmi", "shortCut": "KR"},
    {"name": "Asmit", "caste": "Khanal", "shortCut": "AK"},
    {"name": "Darpan", "caste": "Giri", "shortCut": "DG"}
]

for student in students:
    print(student["name"], student["caste"], student["shortCut"], sep = ", " )