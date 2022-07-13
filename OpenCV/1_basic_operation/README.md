# 이미지 읽고 쓰기

파일명을 이용해서 이미지를 읽는다. 이 때, 이미지를 읽는 방식을 flag로 지정할 수 있다.
```python
import cv2
img = cv2.imread('path/to/imagefile', flag)
```
flag의 종류는 다음과 같다.
- cv2.IMREAD_COLOR : 컬러 이미지 상태로 읽는다. default값이므로 flag가 생략되면 3채널 컬러이미지로 읽게 된다.
- cv2.IMREAD_GRAYSCALE : 1채널 Grayscale 값으로 이미지를 읽는다.
- cv2.IMREAD_UNCHANGED : 원본 그대로 읽게된다. 투명도 값을 저장한 알파채널이 있는 png 이미지의 경우 4채널로 읽게 된다.

이외에도 채널, 크기, 정밀도 등을 다르게 이미지를 읽는 flag들이 많지만, 주로 사용하는 값들은 위와 같다.

`cv2.imread()`로 읽은 반환값은 넘파이 배열(`numpy.ndarray`)이며, 다른 이미지 프로세싱 라이브러리와 달리 BGR 채널 순서로 값을 가지게 된다.

이미지를 화면에 띄우기 위해서는 `cv2.imshow()`를 사용한다.
```python
cv2.imshow('title of window', img)
```

보통 `cv2.imshow()`는 아래 함수와 함께 쓰인다.

- `cv2.waitkey()` : 파라미터로 대기할 시간을 ms단위로 넣을 수 있다. 0은 무한 대기를 의미한다.
- `cv2.destroyAllWindows()` : 열려있는 모든 창을 닫는다.

마지막으로 읽어들인 이미지를 저장할 수 있다.
```python
cv2.imwrite('path/to/saveFilename', img)
```