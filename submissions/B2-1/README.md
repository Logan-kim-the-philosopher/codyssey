# B2-1 나만의 용돈 기입장

- [서비스 체험](https://allowance-b2-1.vercel.app/)
- [발표자료](https://allowance-b2-1.vercel.app/presentation/index.html)
- [Python 소스코드](artifact/budget_app)

콘솔 실행: artifact 폴더에서 `python3 -m budget_app --help`.
웹 로컬 실행: web-demo 폴더에서 `python3 prepare.py`, `python3 dev.py`.
웹은 원본 Python 서비스와 JSONL 저장소를 요청별 임시 폴더에서 호출하며 데이터를 브라우저에 보관합니다.
웹 검증: web-demo 폴더에서 `python3 -m unittest discover -s tests -v`.
