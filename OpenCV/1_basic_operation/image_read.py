# OpenCV 라이브러리 로드
import cv2

def main():
    original = cv2.imread('kei.png', cv2.IMREAD_COLOR)
    gray = cv2.imread('kei.png', cv2.IMREAD_GRAYSCALE)
    unchanged = cv2.imread('kei.png', cv2.IMREAD_UNCHANGED)
    
    print(type(original))
    print('original image shape:', original.shape)
    print('gray image shape:', gray.shape)
    print('4channel image shape:', unchanged.shape)

    cv2.imshow('original image', original)
    cv2.imshow('gray image', gray)
    cv2.imshow('with transparent channel', unchanged)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite('kei_gray.jpg', gray)

if __name__ == '__main__':
    main()