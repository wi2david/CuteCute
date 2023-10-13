import cv2

def main() :
  image = cv2.imread("page1.png")

  scale_percent = 150
  width = int(image.shape[1] * scale_percent / 100)
  height = int(image.shape[0] * scale_percent / 100)
  dim = (width, height)
  imageResized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

  imageGray = cv2.cvtColor(imageResized, cv2.COLOR_BGR2GRAY)
  
  imageCanny = cv2.Canny(imageGray, 500, 1000)

  _, th = cv2.threshold(imageGray, 100, 255, cv2.THRESH_BINARY)
  img, contourns = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  imgContorned = cv2.drawContours(imageResized, contourns, -1, (0, 255, 0), 3)
  #cv2.imshow("Imagem Original: ", imageResized)
  #cv2.imshow("Imagem em tons de cinza: ", imageGray)
  cv2.imshow("Image com Canny: ", imageCanny)
  cv2.imshow("Imagem Contornada: ", imgContorned)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

if __name__ == "__main__" :
  main()