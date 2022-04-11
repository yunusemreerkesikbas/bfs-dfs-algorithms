from app import Graph
import time
graph = Graph()

print("********** 2021-2022 ÇİZGE KURAMI **********")
print("""
              Algoritma Uygulamasına Hoşgeldiniz 
              Uygulamamızda güncel olarak 2 adet algoritma vardır:
              BFS(Bread First Search) - DFS(Depth First Search)
              Grafımız açılan pencerede modellenmiştir(Sadece Görsel Amaçlıdır)
              Lütfen yapmak istediğiniz işlemi seçiniz( 1 or 2 ):
              1- BFS uygulamasını çalıştırmak
              2- DFS uygulamasını çalıştırmak
              Çıkmak için 'q' tuşuna basınız
      """)


def ui():
    graph.openImg('graph.png')
    while True:

        choose = input("Seciminiz: ")
        if choose == "1":
            print('İşleminiz yerine getiriliyor. Lütfen bekleyiniz')
            print('başlangıç düğümünden(1) başlayarak tüm düğümleri tarayan BFS algoritması:')
            time.sleep(1)
            graph.bfsAlgorithms('1')
            print('\n')
        elif choose == '2':
            print('İşleminiz yerine getiriliyor. Lütfen bekleyiniz')
            print(' Başlangıç düğümünden(1) başlayarak tüm düğümleri tarayan DFS algoritması:')
            time.sleep(1)
            graph.dfsAlgorithms('1')
        elif choose == 'q':
            print("Çıkış yapılıyor... Yine bekleriz...")
            time.sleep(2)
            break
        else:
            print("OOPPS ! Bir şeyler yanlış gitti tekrar deneyiniz...")
            time.sleep(1)


ui()
