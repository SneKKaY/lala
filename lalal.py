def lolo():
    def zaza():
        print('Я в области видимости функции lolo')
        zaza()
# zaza()  - не удалось выполнить так как функция локальная