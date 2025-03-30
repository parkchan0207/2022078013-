# 2022078013 박찬엽 개인과제 2

def input_data():
    """학생 정보를 입력받는 함수"""
    students = []
    
    # 5명의 학생 정보 입력
    for i in range(5):
        print(f"\n{i+1}번째 학생 정보 입력:")
        student_id = input("학번: ")
        name = input("이름: ")
        english = int(input("영어 점수: "))
        c_lang = int(input("C-언어 점수: "))
        python = int(input("파이썬 점수: "))
        
        student = {
            "학번": student_id,
            "이름": name,
            "영어": english,
            "C언어": c_lang,
            "파이썬": python,
            "총점": 0,
            "평균": 0.0,
            "학점": "",
            "등수": 0
        }
        
        students.append(student)
    
    return students

def calculate_total_avg(students):
    """총점과 평균을 계산하는 함수"""
    for student in students:
        student["총점"] = student["영어"] + student["C언어"] + student["파이썬"]
        student["평균"] = student["총점"] / 3
    
    return students

def calculate_grade(students):
    """학점을 계산하는 함수"""
    for student in students:
        avg = student["평균"]
        
        if avg >= 90:
            student["학점"] = "A"
        elif avg >= 80:
            student["학점"] = "B"
        elif avg >= 70:
            student["학점"] = "C"
        elif avg >= 60:
            student["학점"] = "D"
        else:
            student["학점"] = "F"
    
    return students

def calculate_rank(students):
    """등수를 계산하는 함수"""
    for i in range(len(students)):
        rank = 1
        for j in range(len(students)):
            if students[j]["총점"] > students[i]["총점"]:
                rank += 1
        students[i]["등수"] = rank
    
    return students

def print_data(students):
    """학생 정보를 출력하는 함수"""
    if not students:
        print("등록된 학생이 없습니다.")
        return
        
    print("\n" + "=" * 80)
    print("{:<10} {:<10} {:<8} {:<8} {:<8} {:<8} {:<8} {:<6} {:<6}".format(
        "학번", "이름", "영어", "C언어", "파이썬", "총점", "평균", "학점", "등수"))
    print("-" * 80)
    
    for student in students:
        print("{:<10} {:<10} {:<8} {:<8} {:<8} {:<8} {:<8.2f} {:<6} {:<6}".format(
            student["학번"],
            student["이름"],
            student["영어"],
            student["C언어"],
            student["파이썬"],
            student["총점"],
            student["평균"],
            student["학점"],
            student["등수"]
        ))
    
    print("=" * 80)

def insert_student(students):
    """학생 정보를 추가하는 함수"""
    print("\n새로운 학생 정보 입력:")
    student_id = input("학번: ")
    name = input("이름: ")
    english = int(input("영어 점수: "))
    c_lang = int(input("C-언어 점수: "))
    python = int(input("파이썬 점수: "))
    
    student = {
        "학번": student_id,
        "이름": name,
        "영어": english,
        "C언어": c_lang,
        "파이썬": python,
        "총점": 0,
        "평균": 0.0,
        "학점": "",
        "등수": 0
    }
    
    # 총점과 평균 계산
    student["총점"] = student["영어"] + student["C언어"] + student["파이썬"]
    student["평균"] = student["총점"] / 3
    
    # 학점 계산
    avg = student["평균"]
    if avg >= 90:
        student["학점"] = "A"
    elif avg >= 80:
        student["학점"] = "B"
    elif avg >= 70:
        student["학점"] = "C"
    elif avg >= 60:
        student["학점"] = "D"
    else:
        student["학점"] = "F"
    
    # 학생 추가
    students.append(student)
    
    # 등수 재계산
    calculate_rank(students)
    
    print(f"학생 '{name}'이(가) 추가되었습니다.")
    return students

def delete_student(students):
    """학생 정보를 삭제하는 함수"""
    if not students:
        print("등록된 학생이 없습니다.")
        return students
        
    student_id = input("삭제할 학생의 학번을 입력하세요: ")
    
    # 학번으로 학생 찾기
    for i, student in enumerate(students):
        if student["학번"] == student_id:
            del students[i]
            print(f"학번 '{student_id}'인 학생을 삭제했습니다.")
            
            # 등수 재계산
            if students:
                calculate_rank(students)
            return students
    
    print(f"학번 '{student_id}'인 학생을 찾을 수 없습니다.")
    return students

def search_by_id(students):
    """학번으로 학생을 검색하는 함수"""
    if not students:
        print("등록된 학생이 없습니다.")
        return
        
    student_id = input("검색할 학생의 학번을 입력하세요: ")
    
    # 학번으로 학생 찾기
    for student in students:
        if student["학번"] == student_id:
            print("\n검색 결과:")
            print("=" * 80)
            print("{:<10} {:<10} {:<8} {:<8} {:<8} {:<8} {:<8} {:<6} {:<6}".format(
                "학번", "이름", "영어", "C언어", "파이썬", "총점", "평균", "학점", "등수"))
            print("-" * 80)
            
            print("{:<10} {:<10} {:<8} {:<8} {:<8} {:<8} {:<8.2f} {:<6} {:<6}".format(
                student["학번"],
                student["이름"],
                student["영어"],
                student["C언어"],
                student["파이썬"],
                student["총점"],
                student["평균"],
                student["학점"],
                student["등수"]
            ))
            
            print("=" * 80)
            return
    
    print(f"학번 '{student_id}'인 학생을 찾을 수 없습니다.")

def search_by_name(students):
    """이름으로 학생을 검색하는 함수"""
    if not students:
        print("등록된 학생이 없습니다.")
        return
        
    name = input("검색할 학생의 이름을 입력하세요: ")
    
    # 이름으로 학생 찾기
    found_students = []
    for student in students:
        if student["이름"] == name:
            found_students.append(student)
    
    if found_students:
        print("\n검색 결과:")
        print("=" * 80)
        print("{:<10} {:<10} {:<8} {:<8} {:<8} {:<8} {:<8} {:<6} {:<6}".format(
            "학번", "이름", "영어", "C언어", "파이썬", "총점", "평균", "학점", "등수"))
        print("-" * 80)
        
        for student in found_students:
            print("{:<10} {:<10} {:<8} {:<8} {:<8} {:<8} {:<8.2f} {:<6} {:<6}".format(
                student["학번"],
                student["이름"],
                student["영어"],
                student["C언어"],
                student["파이썬"],
                student["총점"],
                student["평균"],
                student["학점"],
                student["등수"]
            ))
        
        print("=" * 80)
    else:
        print(f"이름이 '{name}'인 학생을 찾을 수 없습니다.")

def sort_by_total(students):
    """총점을 기준으로 학생을 정렬하는 함수 (내림차순)"""
    if not students:
        print("등록된 학생이 없습니다.")
        return students
    
    # 총점을 기준으로 내림차순 정렬
    students.sort(key=lambda student: student["총점"], reverse=True)
    
    # 등수 재계산
    calculate_rank(students)
    
    print("총점 기준으로 학생 목록을 정렬했습니다.")
    return students

def count_above_80(students):
    """평균 80점 이상인 학생 수를 계산하는 함수"""
    if not students:
        print("등록된 학생이 없습니다.")
        return
    
    count = 0
    for student in students:
        if student["평균"] >= 80:
            count += 1
    
    print(f"평균 80점 이상인 학생 수: {count}명")

def display_menu():
    """메뉴를 출력하는 함수"""
    print("\n===== 학생 성적 관리 프로그램 =====")
    print("1. 학생 정보 입력 (5명)")
    print("2. 학생 정보 출력")
    print("3. 학생 정보 추가")
    print("4. 학생 정보 삭제")
    print("5. 학번으로 학생 검색")
    print("6. 이름으로 학생 검색")
    print("7. 총점 기준 정렬")
    print("8. 80점 이상 학생 수 카운트")
    print("0. 종료")
    print("=================================")

def main():
    students = []
    
    while True:
        display_menu()
        choice = input("메뉴 선택: ")
        
        if choice == "1":
            students = input_data()
            students = calculate_total_avg(students)
            students = calculate_grade(students)
            students = calculate_rank(students)
            
        elif choice == "2":
            print_data(students)
            
        elif choice == "3":
            students = insert_student(students)
            
        elif choice == "4":
            students = delete_student(students)
            
        elif choice == "5":
            search_by_id(students)
            
        elif choice == "6":
            search_by_name(students)
            
        elif choice == "7":
            students = sort_by_total(students)
            
        elif choice == "8":
            count_above_80(students)
            
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
            
        else:
            print("잘못된 메뉴를 선택했습니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main(