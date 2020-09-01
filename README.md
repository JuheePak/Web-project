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

---

- leaflet 대신 Googlemap 사용
- 다중 마커 표시, 마커를 클릭하면 Zoom 기능 & 말풍선에 상세 정보가 뜬다.
- 주소를 입력하면 해당 동네로 Zoom 되는 기능까지 구현해보려고 함. 제발...pls...