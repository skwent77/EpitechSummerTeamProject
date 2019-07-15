from DominantColors import DominantColors
#from tester import tester
#from 파일이름 import 클래스이름
class Main:
    ImageOfFruit = 'APPLE.jpg'

    def main():
        #for :


        clusters = 2

        dc = DominantColors(Main.ImageOfFruit, clusters)
        img=ImageOfFruit
        colors = dc.dominantColors()

        print(colors)

    if __name__ == '__main__':
        main()




