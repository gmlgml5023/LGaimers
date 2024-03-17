# LGaimers
<br>

## MQL data 기반 b2b 영업 기회 창출 예측 모델 개발

이번 해커톤을 통해 풀 문제는 고객지수 중 하나인 영업기회전환지수이며, 이는 B2B Marketing에서 활용되는 고객지수이다.

여기서 B2B Marketing은 기업 고객을 대상으로 영업 기회를 발굴해서 지속적으로 매출을 발생시키는 것을 목표로 한다. 자사 제품에 대해 관심을 보이고 구매 가능성이 있는 잠재 고객을 Lead라고 하는데, 이러한 Lead 고객 중에서도 BANT Quatation에 대한 답변을 한 고객을 Marketing Qualified Lead 의 약자로 MQL 고객 이라고 정의를 한다. 이러한 MQL 고객을 대상으로 영업 사원을 할당하게 되고, 최종적으로 구매까지 이어지게 하기 위해 개인화 Marketing 활동을 진행하게 된다.

하지만 할당할 수 있는 영업사원의 수는 한정적이기에 MQL 고객 정보를 이용해서 영업 전환 성공 여부를 예측하는 AI Model 만든다면 각 고객의 영업 전환 성공 가능성을 지수로 표현할 수 있고 이 지수를 활용해 효율적으로 영업사원의 배치가 가능하다. 이렇게 개발된 지수를 영업기회전환지수라고 한다.

본 해커톤에서는 약 30개의 Feature를 가진 학습용 Dataset인 train.csv 파일과, 제출용 Test Dataset인 submission 파일, 그리고 Base 코드가 제공된다.

이 대회에서 예측해야 하는 값은 is_converted로 각 데이터를 True or False로 분류함을 통해 영업 성공 여부를 예측한다. Feature, 다시 말해서 다른 Column들은 동일하지만 Submission파일에는 고객의 고유한 번호로 고객의 순서가 섞인 경우에도 올바른 채점이 진행되기 위한 값인 id칼럼이 추가적으로 있으며, is_converted은 모두 비어있다.

<br>

## 📜 Dataset
<br>

- bant_submit : MQL 구성 요소들 중 [1]Budget(예산), [2]Title(고객의 직책/직급), [3]Needs(요구사항), [4]Timeline(희망 납기일) 4가지 항목에 대해서 작성된 값의 비율
- customer_country : 고객의 국적
- business_unit : MQL 요청 상품에 대응되는 사업부
- com_reg_ver_win_rate : Vertical Level 1, business unit, region을 기준으로 oppty 비율을 계산
- customer_idx : 고객의 회사명
- customer_type : 고객 유형
- enterprise : Global 기업인지, Small/Medium 규모의 기업인지
- historical_existing_cnt : 이전에 Converted(영업 전환) 되었던 횟수
- id_strategic_ver : (도메인 지식) 특정 사업부(Business Unit이 ID일 때), 특정 사업 영역(Vertical Level1)에 대해 가중치를 부여
- it_strategic_ver : (도메인 지식) 특정 사업부(Business Unit이 IT일 때), 특정 사업 영역(Vertical Level1)에 대해 가중치를 부여
- idit_strategic_ver : id_strategic_ver이나 it_strategic_ver 값 중 하나라도 1의 값을 가지면 1 값으로 표현
- customer_job : 고객의 직업군
- lead_desc_length : 고객이 작성한 Lead Descriptoin 텍스트 총 길이
- inquiry_type : 고객의 문의 유형
- product_category : 요청 제품 카테고리
- product_subcategory : 요청 제품 하위 카테고리
- product_modelname : 요청 제품 모델명
- customer_country.1 : 담당 자사 법인명 기반의 지역 정보(대륙)
- customer_position : 고객의 회사 직책
- response_corporate : 담당 자사 법인명
- expected_timeline : 고객의 요청한 처리 일정
- ver_cus : 특정 Vertical Level 1(사업영역) 이면서 Customer_type(고객 유형)이 소비자(End-user)인 경우에 대한 가중치
- ver_pro : 특정 Vertical Level 1(사업영역) 이면서 특정 Product Category(제품 유형)인 경우에 대한 가중치
- ver_win_rate_x : 전체 Lead 중에서 Vertical을 기준으로 Vertical 수 비율과 Vertical 별 Lead 수 대비 영업 전환 성공 비율 값을 곱한 값
- ver_win_ratio_per_bu : 특정 Vertical Level1의 Business Unit 별 샘플 수 대비 영업 전환된 샘플 수의 비율을 계산
- business_area : 고객의 사업 영역
- business_subarea : 고객의 세부 사업 영역
- lead_owner : 영업 담당자 이름
- is_converted : 영업 성공 여부. True일 시 성공

<br>

## 🎖️ 결과
<img width="545" alt="image" src="https://github.com/gmlgml5023/LGaimers/assets/135304794/cd14fa4b-1849-454b-bfbf-f097adcee539">

<br>

## 팀 노션

[Notion](https://magnetic-heron-6b4.notion.site/MQL-b2b-8f213398be00478f85351312363543cc)
