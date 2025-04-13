 ##################

  #프로그램명:5명의 학생 성적산출 프로그램

  #작성자: 소프트웨어학과/박찬엽

  #작성일:2025.4.12

  #프로그램 설명:키보드로부터 학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 입력받아 총점, 평균, 학점, 등수를  계산하는 프로그램 class 사용

  ###################
class Student:
    def __init__(self, student_id, name, english, c_lang, python_score):
        self.student_id = student_id
        self.name = name
        self.english = english
        self.c_lang = c_lang
        self.python = python_score
        self.calculate_total_and_avg()
        self.grade = self.calc_grade()
        self.rank = 1

    def calculate_total_and_avg(self):
        self.total = self.english + self.c_lang + self.python
        self.avg = round(self.total / 3)

    def calc_grade(self):
        if self.avg >= 90:
            return "A"
        elif self.avg >= 80:
            return "B"
        elif self.avg >= 70:
            return "C"
        elif self.avg >= 60:
            return "D"
        else:
            return "F"

    def __str__(self):
        return (f"{self.student_id:<15}{self.name:<15}"
                f"{self.english:>8.0f}{self.c_lang:>8.0f}{self.python:>8.0f}"
                f"{self.total:>8.0f}{self.avg:>8}{self.grade:>8}{self.rank:>8}")


class GradeManager:
    def __init__(self):
        self.students = []

    def input_students(self, count=5):
        print(f"{count}명의 학생 정보를 입력하세요.")
        i = 0
        while i < count:
            print(f"\n학생 {i+1} 정보:")
            student_id = input("학번: ")
            name = input("이름: ")
            try:
                english = float(input("영어: "))
                c_lang = float(input("C-언어: "))
                python_score = float(input("파이썬: "))
            except ValueError:
                print("점수는 숫자로 입력해야 합니다. 다시 입력해주세요.")
                continue
            student = Student(student_id, name, english, c_lang, python_score)
            self.students.append(student)
            i += 1
        self.calculate_ranks()

    def calculate_ranks(self):
        for s in self.students:
            s.rank = 1
            for other in self.students:
                if other.total > s.total:
                    s.rank += 1

    def output_students(self):
        print("\n" + " " * 40 + "성적관리 프로그램")
        print("=" * 80)
        header = (f"{'학번':<15}{'이름':<15}{'영어':>8}{'C-언어':>8}"
                  f"{'파이썬':>8}{'총점':>8}{'평균':>8}{'학점':>8}{'등수':>8}")
        print(header)
        print("=" * 80)
        for s in self.students:
            print(s)

    def insert_student(self):
        print("\n[삽입] 새로운 학생 정보를 입력하세요:")
        student_id = input("학번: ")
        name = input("이름: ")
        try:
            english = float(input("영어: "))
            c_lang = float(input("C-언어: "))
            python_score = float(input("파이썬: "))
        except ValueError:
            print("점수는 숫자로 입력해야 합니다. 삽입 실패.")
            return
        new_student = Student(student_id, name, english, c_lang, python_score)
        self.students.append(new_student)
        self.calculate_ranks()
        print("학생 정보가 삽입되었습니다.")

    def delete_student(self, student_id):
        found = False
        for i, s in enumerate(self.students):
            if s.student_id == student_id:
                del self.students[i]
                found = True
                print(f"학번 {student_id} 학생 정보가 삭제되었습니다.")
                break
        if not found:
            print("삭제할 학생 정보를 찾지 못했습니다.")
        self.calculate_ranks()

    def search_by_id(self, student_id):
        results = [s for s in self.students if s.student_id == student_id]
        return results

    def search_by_name(self, name):
        results = [s for s in self.students if s.name == name]
        return results

    def sort_by_total(self):
        self.students.sort(key=lambda s: s.total, reverse=True)
        self.calculate_ranks()

    def count_above_80(self):
        return sum(1 for s in self.students if s.avg >= 80)


def main():
    gm = GradeManager()
    gm.input_students(5)
    gm.output_students()
    gm.insert_student()
    gm.output_students()
    search_id = input("\n[탐색] 검색할 학번을 입력하세요: ")
    results = gm.search_by_id(search_id)
    if results:
        print("\n[학번 탐색 결과]")
        for s in results:
            print(s)
    else:
        print("해당 학번의 학생을 찾지 못했습니다.")
    search_name = input("\n[탐색] 검색할 이름을 입력하세요: ")
    results = gm.search_by_name(search_name)
    if results:
        print("\n[이름 탐색 결과]")
        for s in results:
            print(s)
    else:
        print("해당 이름의 학생을 찾지 못했습니다.")
    del_id = input("\n[삭제] 삭제할 학생의 학번을 입력하세요: ")
    gm.delete_student(del_id)
    gm.output_students()
    gm.sort_by_total()
    print("\n[정렬] 총점 기준 내림차순 정렬 후:")
    gm.output_students()
    count80 = gm.count_above_80()
    print(f"\n평균 80점 이상 학생 수: {count80}")


if __name__ == "__main__":
    main()