import pandas as pd
import json
import os

# 📂 XLSX & JSON 파일 경로
xlsx_file_path = 'school_list.xlsx'  # ✅ XLSX 파일 경로
json_file_path = 'D:/summer_school/summer_school/public/data.json'

# ✅ 모든 분야 리스트 (필요한 경우 확장 가능)
ALL_CATEGORIES = ["공학", "사회과학", "경영경제", "자연과학", "인문예술", "언어·지역학"]

# 기존 JSON 파일 읽기 (파일이 존재하면 로드)
if os.path.exists(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as f:
        try:
            existing_data = json.load(f)  # 기존 JSON 로드
        except json.JSONDecodeError:
            existing_data = []  # JSON이 비어 있거나 손상된 경우 빈 리스트
else:
    existing_data = []

# 📥 XLSX 파일 읽기
df = pd.read_excel(xlsx_file_path, engine='openpyxl')

# ✅ NaN 값(빈 값)을 빈 문자열("")로 채우기
df = df.fillna("")

# ✅ 새로운 데이터 리스트
new_data = []
for _, row in df.iterrows():
    d = row.to_dict()  # ✅ 각 행을 딕셔너리로 변환

    # ✅ category 필드 처리 (전체 → 모든 카테고리로 변환)
    if "category" in d and isinstance(d["category"], str):
        categories = [cat.strip() for cat in d["category"].split(",") if cat.strip()]
        d["category"] = ALL_CATEGORIES if "전체" in categories else categories

    # ✅ program_date_tidily → program_month 변환
    program_date_tidily = d.get("program_date_tidily", "").replace(" ", "")  # 공백 제거
    month_entries = program_date_tidily.split(",")  # 쉼표로 나누기
    month_data = []

    for entry in month_entries:
        months = []
        is_range = False

        if "6월" in entry and "7월" in entry:
            months = [6, 7]
            is_range = True  # ✅ 6-7월 같은 경우 범위
        elif "7월" in entry and "8월" in entry:
            months = [7, 8]
            is_range = True  # ✅ 7-8월 같은 경우 범위
        elif "6월" in entry:
            months = [6]
        elif "7월" in entry:
            months = [7]
        elif "8월" in entry:
            months = [8]

        month_data.append({"program_month": months, "is_range": is_range})  # ✅ 개별 저장

    d["program_months"] = month_data  # ✅ 변환된 월 정보 저장 (리스트)

    new_data.append(d)

# ✅ 기존 데이터 덮어쓰기 (중복 방지)
with open(json_file_path, 'w', encoding='utf-8') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=2)

print("✅ JSON 파일이 성공적으로 업데이트되었습니다!")
