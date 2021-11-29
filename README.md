# Diary_Sentiment_Analysis

### 인공지능(AI), 자연어처리(NLP), 감성분석(Sentiment-Analysis)
---
# 1. 프로젝트 개요
- 프로젝트 명 : 끄적이는 일기속에서 너의 노래가 느껴진거야 ♬

- 프로젝트 참여 인원 : 5명

- 프로젝트 기간 : 21.09.07 ~ 21.12.14 (약 4개월)
- 프로젝트 개요 : 간략한 텍스트 형식의 일기 작성 후, 감정을 자동 분류 및 기록 한다. 나아가 분류 된 감정에 적합한 노래를 추천한다.
- 프로젝트 효과 : 객관적인 감정 분석으로 자신의 감정을 더 정확하게 확인 하며 감정에 따른 노래 추천으로 감정을 치유할 수 있다.  
정신과 심리 치료 참고 자료로 활용 가능하며 스스로의 심리 상태를 확인하고 개선하는 자가 치료 목적으로도 활용 가능하다.
- 프로젝트 시연 결과 :     

# 2. 프로젝트 환경 구성
- 추가 학습 데이터셋 : [AIhub](https://aihub.or.kr/opendata/keti-data/recognition-laguage/KETI-02-009) 한국어 단발성 대화 데이터셋, 한국어 연속성 대화 데이터셋
- 학습 모델 : [SKT/Kobert](https://github.com/SKTBrain/KoBERT)
- 프로젝트 설치 환경
```
!pip install mxnet
!pip install gluonnlp pandas tqdm
!pip install sentencepiece==0.1.91
!pip install transformers==4.8.2
!pip install torch
```

# 3. 프로젝트 폴더 설명
<실행 방법> main.py가 저장되어있는 폴더로 이동한다.
```
cd 폴더위치 streamlit run main.py
```
> |_ data/ (데이터)
>> |_ kobert_tokenizer.py : (kobert 모델에 적합한 tokenizer)  
>> |_ 노래 라벨링 감정 7개 수정.xlsx : (노래 추천 시스템 구현을 위한 감정 라벨링)

> |_ kobert/ ([skt/kobert 모델](https://huggingface.co/skt/kobert-base-v1))  

> |_pages/ (streamlit 웹 페이지 구현에 사용)
>> |_다이어리.py (감정 분석 다이어리 구현)

> |_webpage/
>> |_web_diary_test.py (감정 분석 최종 결과)  
>> |_web_module.py  (감정분석 학습에 사용되는 모듈)  
>> |_web_music_data.py (음악 추천 분류 데이터 정제)  
>> |_web_predict.py (감성분석 평가)

>|_login.py (웹 페이지 로그인창)  

>|_main.py (최종 웹페이지 구현 파일)

# 4. 프로젝트 결과
1. 프로젝트에 사용한 Kobert 모델로 사전 학습한 param7.pt 모델 저장 값은 용량 문제로 올리지 않았음
- 한국어 데이터셋에 최적화된 KoBERT 모델의 성능이 가장 높게 나타났다.  

|학습 모델|데이터셋|정확도|
|:---:|:---:|:---:|
|KoBERT|한국어 단발성 대화 |56%|
|BERT|한국어 단발성 대화 |48%|
|CNN Fast Text|한국어 단발성 대화 |42%| 

2. 한국어 단발성 대화 데이터셋의 기존 감정 분류 7개(공포,놀람,분노,슬픔,중립,행복,혐오)를 수정하고, 한국어 연속성 데이터셋과 추가 학습 시키며 성능 향상에 노력하였다.

|학습 모델|데이터셋(감정 분류 갯수)|정확도|
|:---:|:---:|:---:|
|KoBERT|단발성(7개) |56%|
|KoBERT|단발성(5개) |69%|
|KoBERT|단발성+연속성(7개) |72%|
- 단발성+연속성 데이터셋 감정 분류를 [공포,놀람,분노,슬픔,중립,행복,혐오]로 7개의 감정으로 합치며 학습한 결과 72%의 정확도가 나타났다.

# 5. 프로젝트 참고 자료
