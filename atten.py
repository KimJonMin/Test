# attend.py

import datetime  # 날짜를 다루는 기본 라이브러리 (따로 설치 불필요)

FILENAME = "attendance.txt"  # 출석 기록을 저장할 파일

def add_attendance(name):
    """출석을 기록하는 함수"""
    today = datetime.date.today()  # 오늘 날짜 자동으로 가져오기
    record = f"{today} | {name}\n"  # 예: 2025-01-15 | 홍길동

    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write(record)  # 파일에 한 줄 추가 (a = append, 덮어쓰지 않음)

    print(f"✅ 출석 완료: {today} - {name}")

def show_attendance():
    """출석 목록을 보여주는 함수"""
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            lines = f.readlines()

        if not lines:
            print("📋 출석 기록이 없습니다.")
        else:
            print("\n📋 출석 목록:")
            print("-" * 30)
            for line in lines:
                print(line.strip())  # strip() = 줄 끝 빈칸/줄바꿈 제거
            print("-" * 30)

    except FileNotFoundError:
        # 파일이 아직 없을 때 (처음 실행 시)
        print("📋 출석 기록이 없습니다.")

def main():
    """프로그램 시작점"""
    print("=== 스터디 출석부 ===")
    print("1. 출석 등록")
    print("2. 목록 보기")
    print("3. 종료")

    while True:  # 종료 전까지 계속 반복
        choice = input("\n선택 (1/2/3): ").strip()

        if choice == "1":
            name = input("이름을 입력하세요: ").strip()
            if name:  # 이름이 비어있지 않으면
                add_attendance(name)
            else:
                print("⚠️ 이름을 입력해주세요.")

        elif choice == "2":
            show_attendance()

        elif choice == "3":
            print("👋 프로그램을 종료합니다.")
            break  # while 루프 탈출

        else:
            print("⚠️ 1, 2, 3 중에서 선택해주세요.")

# 이 파일을 직접 실행할 때만 main() 호출
if __name__ == "__main__":
    main()
    