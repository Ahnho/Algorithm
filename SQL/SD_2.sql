##############
# 이름에 el이 들어가는 동물 찾기
##############

SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
WHERE NAME LIKE "%EL%" AND ANIMAL_TYPE = "DOG"
ORDER BY NAME