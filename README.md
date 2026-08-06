# E1-2 파이썬 이해하기

## 프로젝트 개요

터미널에서 실행하는 Python 퀴즈 게임입니다.  
메뉴를 통해 퀴즈 풀기, 퀴즈 추가, 퀴즈 목록 확인, 퀴즈 삭제, 최고 점수 확인, 플레이 기록 확인을 수행할 수 있습니다.

## 퀴즈 주제 선정 이유

Python 기초 문법을 배우는 과제이기 때문에, 퀴즈 주제도 Python 기본 개념으로 맞췄습니다.  
문자열, 불리언, 리스트, 반복문, 반환값처럼 과제에서 직접 설명해야 하는 개념을 퀴즈 문제로 다시 확인할 수 있게 구성했습니다.

## 실행 방법

과제 작업 루트에서 아래 명령으로 실행합니다.

```bash
cd /Users/hskim/Projects/codyssey/artifacts/e1-2/work
python3 main.py
```

## 기능 목록

- 메뉴 출력과 종료
- 빈 입력, 문자 입력, 범위 밖 숫자 입력 예외 처리
- `Quiz` 클래스 기반 개별 퀴즈 표현
- `QuizGame` 클래스 기반 전체 게임 관리
- 퀴즈 풀기
- 퀴즈 추가
- 퀴즈 목록 보기
- 퀴즈 삭제
- 최고 점수 확인
- 플레이 기록 저장과 조회
- `state.json` 저장/복구
- 랜덤 출제
- 문제 수 선택
- 힌트 사용과 점수 차감

## 파일 구조

```text
artifacts/e1-2/
├── README.md
├── state.json
├── logs/
│   └── practice.jsonl
├── render/
│   └── latest/
│       ├── README.md
│       └── presentation.html
└── work/
    ├── main.py
    └── state.json
```

## 데이터 파일 설명

이 과제의 실행 데이터는 기본적으로 `artifacts/e1-2/work/state.json`에 UTF-8로 저장됩니다.

주요 필드는 다음과 같습니다.

- `quizzes`: 문제, 선택지, 정답, 힌트 목록
- `best_score`: 현재 최고 점수
- `score_history`: 날짜/시간, 푼 문제 수, 점수 기록 배열

예시 구조:

```json
{
  "quizzes": [
    {
      "question": "Python에서 문자열을 저장하는 자료형은?",
      "choices": ["int", "str", "bool", "list"],
      "answer": 2,
      "hint": "문자열은 따옴표로 감싸 자주 표현합니다."
    }
  ],
  "best_score": 1,
  "score_history": [
    {
      "played_at": "2026-08-06T19:55:55",
      "total_questions": 1,
      "score": 1
    }
  ]
}
```
