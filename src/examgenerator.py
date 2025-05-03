import random
from pathlib import Path

def read_questions(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [q.strip() for q in f if q.strip()]
    return lines

def generate_exam(questions_list, count=10):
    return random.sample(questions_list, count)

def write_exam_to_file(exam_list, version, folder):
    folder.mkdir(parents=True, exist_ok=True)
    file_path = folder / f"exam_v{version}.txt"
    with open(file_path, "w", encoding="utf-8") as out:
        for i, q in enumerate(exam_list, start=1):
            out.write(f"{i}) {q}\n")

def main():
    subject_name = input("📚 Enter the subject name (e.g., math_class10): ")
    input_file = Path(f"exam_bank/{subject_name}_bank.txt")

    if not input_file.exists():
        print(f"🚫 Error: No file found for {subject_name}.")
        return

    all_questions = read_questions(input_file)
    exam_folder = Path("exam_versions") / subject_name

    total_versions = 10  # Modified: 10 exam sets instead of 12
    for ver in range(1, total_versions + 1):
        one_exam = generate_exam(all_questions, count=10)
        write_exam_to_file(one_exam, ver, exam_folder)

    print(f"🎉 All {total_versions} versions of the {subject_name} exam created successfully!")

if __name__ == "__main__":
    main()
