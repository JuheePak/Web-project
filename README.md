# project1. 장애인&보호자를 위한 웹사이트 

- 장애인과 보호자를 위한 통합된 웹사이트 구축을 목표로 하였음.

- 지역 범위는 서울시로 한정함

- 내가 맡은 파트 중심으로 정리하고 전체적으로 정리 예정
  > 서울시 전동휠체어 충전소 위치 정보 표시 (Map)

  > 서울시에 위치한 관광지/음식점/공공기관의 장애인 화장실 위치 표시 (Map)

---

- 서울시 열린데이터광장 https://data.seoul.go.kr/ 에서 끌어온 open API(json)를 필요한 정보(location, address, tel 등)만 남기는 전처리 작업 진행하여 csv 파일로 정리
- 정리된 **Seoul_all.csv & Seoul_wheelchair.csv** 파일을 지도에 띄우는 작업 진행
- Seoul_wheelchair.csv 파일을 DB에 저장하고(SQLite) 하나 지도에 띄움.
- 참고) 위도가 y, 경도가 x인 참사가 발생함