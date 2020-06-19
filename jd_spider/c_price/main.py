import csv
import random
import math
file = 'jd.csv'

def main(file):
    with open(file,'r',encoding='utf-8')as f:
        rows = csv.reader(f)
        for row in rows:
            if float(row[16]) < 200:
                continue
            else:
                for date in range(6,16):
                        num = random.randint(10,100)
                        price = int(float(row[16]))
                        c = [price + num,price - num]
                        row[date] = random.choice(c)
                        if row[date] == row[9]:
                            row[date] = abs(c[1])
                        if row[date] <= 0:
                            row[date] = abs(row[date])
                        row[date] = str(row[date])
            with open('jds.csv', 'a+', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows([row])
                print('-------写入成功--------')




# row = [['100009000000 ', '联想(Lenovo)天逸510 Pro英特尔酷睿i5 台式机电脑整机(i5-9400F 16G 256G SSD+1T RX550X 4G 独显)23英寸', 'https://item.jd.com/100009349506.html', '0.98', 'https://img11.360buyimg.com/n1/s450x450_jfs/t1/48327/5/16200/388892/5dd3a695E8cf70cbe/57e7dbc4dfa1ec7c.jpg', '电脑', '7876', '7750', '7776', '7723', '7771', '7822', '7776', '7768', '7789', '7705', '7799']]

if __name__ == '__main__':
    main(file)
