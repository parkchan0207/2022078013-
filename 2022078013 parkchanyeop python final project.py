# 2022078013 Parkchanyeop Final Project
# Student Grade Management System using SQLite

import sqlite3

DB_NAME = "grades.db"


def initialize_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS students (
                id TEXT PRIMARY KEY,
                name TEXT,
                english INTEGER,
                clang INTEGER,
                python INTEGER,
                total INTEGER,
                average REAL,
                grade TEXT
        )"""
    )
    conn.commit()
    conn.close()


def calculate_total_average(english: int, clang: int, python: int):
    total = english + clang + python
    average = total / 3
    return total, average


def calculate_grade(avg: float) -> str:
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def insert_student():
    student_id = input("학번: ")
    name = input("이름: ")
    english = int(input("영어 점수: "))
    clang = int(input("C-언어 점수: "))
    python_score = int(input("파이썬 점수: "))
    total, average = calculate_total_average(english, clang, python_score)
    grade = calculate_grade(average)

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (student_id, name, english, clang, python_score, total, average, grade),
        )
        conn.commit()
        print("학생 정보가 저장되었습니다.")
    except sqlite3.IntegrityError:
        print("이미 존재하는 학번입니다.")
    finally:
        conn.close()


def delete_student():
    student_id = input("삭제할 학번: ")
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=?", (student_id,))
    if cur.rowcount:
        print("삭제되었습니다.")
    else:
        print("해당 학번이 존재하지 않습니다.")
    conn.commit()
    conn.close()


def search_student():
    option = input("1. 학번 검색 2. 이름 검색 선택: ")
    keyword = input("검색어: ")
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    if option == "1":
        cur.execute("SELECT * FROM students WHERE id=?", (keyword,))
    else:
        cur.execute("SELECT * FROM students WHERE name LIKE ?", (f"%{keyword}%",))
    rows = cur.fetchall()
    if rows:
        print_students(rows)
    else:
        print("검색 결과가 없습니다.")
    conn.close()


def fetch_all_sorted() -> list:
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM students ORDER BY total DESC")
    rows = cur.fetchall()
    conn.close()
    return rows


def count_above_80() -> int:
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM students WHERE average >= 80")
    (count,) = cur.fetchone()
    conn.close()
    return count


def print_students(rows):
    print("학번 | 이름 | 영어 | C | 파이썬 | 총점 | 평균 | 학점 | 등수")
    sorted_rows = sorted(rows, key=lambda r: r[5], reverse=True)
    for rank, row in enumerate(sorted_rows, start=1):
        sid, name, eng, clang, py, total, avg, grade = row
        print(
            f"{sid} | {name} | {eng} | {clang} | {py} | {total} | {avg:.2f} | {grade} | {rank}"
        )


def display_all():
    rows = fetch_all_sorted()
    if not rows:
        print("등록된 학생이 없습니다.")
        return
    print_students(rows)


def menu():
    initialize_db()
    while True:
        print("\n==== 성적 관리 프로그램 ====")
        print("1. 학생 정보 입력")
        print("2. 학생 정보 삭제")
        print("3. 학생 정보 검색")
        print("4. 전체 학생 출력(총점순)")
        print("5. 평균 80점 이상 학생 수")
        print("0. 종료")
        choice = input("메뉴 선택: ")
        if choice == "1":
            insert_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_all()
        elif choice == "5":
            count = count_above_80()
            print(f"평균 80점 이상 학생 수: {count}")
        elif choice == "0":
            break
        else:
            print("다시 선택하세요.")


if __name__ == "__main__":
    menu()
