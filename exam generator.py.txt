import random
from pathlib import Path

def load_questions(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        questions = [line.strip() for line in file if line.strip()]
    return questions

def create_exam(questions, num_questions=10):
    return random.sample(questions, num_questions)

def save_exam(exam_questions, version_number, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    with open(output_dir / f"exam_version_{version_number}.txt", "w", encoding="utf-8") as file:
        for idx, question in enumerate(exam_questions, 1):
            file.write(f"{idx}. {question}\n")

def main():
    subject = input("Enter subject (example: math_class10): ")
    questions_file = Path(f"questions/{subject}_questions.txt")
    
    if not questions_file.exists():
        print(f"Question file not found for {subject}. Please check the file name.")
        return

    questions = load_questions(questions_file)
    output_dir = Path("generated_exams") / subject

    for version in range(1, 13):  # 12 versions
        exam = create_exam(questions, num_questions=10)  # 10 questions per exam
        save_exam(exam, version, output_dir)

    print(f"✅ Successfully generated 12 exams for {subject}!")

if __name__ == "__main__":
    main()
