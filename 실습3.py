vocabulary.txt 파일을 읽어 "단어:의미" 사전을 구성하고, 
# 사용자가 단어를 입력하면 의미를 출력한다.

def load_dictionary(filename):
    """파일에서 단어와 의미를 읽어 딕셔너리도 반환한다."""
    word_dict = {}
    with open(filename, 'r', encoding='utf-8') as f: # 파일을 읽기 모드로 열다
        for line in f:
            line = line.strip() # 줄 양쭉 공백.개행 제거 
            if not line: # 빈 줄이면 건너뛴다
                continue
            parts = line.split(maxsplit=1) # 첫 번째 공백을 기준으로 분리(번호와 나머지)
            if len(parts) <2: # 분리 결과가 2개 미만이면 유효하지 않은 행이므로 건너뛴다
                continue
            rest = parts[1]

            tokens = rest.split(maxsplit=1) # 영단어와 의미를 공백 기준으로 분리
            if len(tokens) < 2: # 의미가 없으면 건너뛴다
                continue
            word = tokens[0].strip() #영단어 양쭝 공백 제거
            meaning = tokens[1].strip().strip('"') # 의미 양쭝 공백 및 따옴표 제거
            word_dict[word] = meaning
    return word_dict


def main():
    dictionary = load_dictionary('vocabulary.txt') # 파일을 읽어 사전 딕셔너리를 생성

    print("=== 영어 단어 사전 ===")
    print(f"총 {len(dictionary)} 개의 단어가 등록되어 있습니다.")
    print("종료하려면 'quit'를 입력하세요.\n")

    while True:
        word = input("단어를 입력하세요: ").strip() # 사용자 입력을 받고 양쪽 공백 제거
        if word.lower() == 'quit': # 소문자로 변환하여 'quit' 입력 여부 확인
            print("프로그램을 종료합니다.")
            break
        if word in dictionary: # 입력 단어가 사전에 존재하는지 확인
            print(f"{word}: {dictionary[word]}\n")
        else: # 사전에 없는 단어인 경우
            print(f"'{word}'은(는) 사전에 없는 단어입니다.\n")


if __name__ == "__main__": # 이 파일이 직접 실행될 때만 main()을 호출
    main() # 메인 함수 실행#
