from DominantColors import DominantColors
from tester import three_d_model

image = 'colors.jpg'
def main():

   three_d_model.chart(image)
   clusters = 2

   dc = DominantColors(image, clusters)

   colors = dc.dominantColors()

   print(colors)

if __name__ == '__main__':
    main()




