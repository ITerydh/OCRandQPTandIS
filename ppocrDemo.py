from paddleocr import PaddleOCR
import os
import csv
import time

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


# dirpath 为存图片的文件夹的路径，如这里的test,这里是为了取图片的路径
def manyImages(dirpath):
    dirpath = dirpath
    all_list = []
    all_list_path = []
    i = 0  # 标记总文件数量
    for root, dirs, files in os.walk(dirpath):  # 分别代表根目录、文件夹、文件
        for file in files:
            i = i + 1
            imgpath = os.path.join(root, file)
            all_list.append(imgpath + "\n")
            all_list_path.append(imgpath)

    allstr = ''.join(all_list)
    f = open('all_list.txt', 'w', encoding='utf-8-sig')
    f.write(allstr)
    return all_list_path, i


def ocr(dirpath, savepath):
    all_img, length = manyImages(dirpath)
    print("all_img:", all_img)
    print("一共需要处理%d张图片" % length)
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")
    print("开始识别并写入csv文件：")

    # 获取当前时间戳
    time_stamp = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))

    # 创建文件夹如果不存在的话
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    final_csv_path = savepath + "result_" + time_stamp + ".csv"

    with open(final_csv_path, 'w', encoding='utf-8-sig') as f:
        row = ['姓名', '扫码地点', '进入登记时间', '最新上报时间', '结果', '码状态', '疫苗接种信息']
        write = csv.writer(f)
        write.writerow(row)
        f.close()
    for img in all_img:
        results = ocr.ocr(img, cls=True)

        with open(final_csv_path, 'a', encoding='UTF-8', newline='') as f:
            write = csv.writer(f)
            r = ['未知', '未知', '未知', '未知', '未知', '未知', '未知']
            for i in range(len(results)):
                data = results[i]
                if "*" in data[1][0]:
                    if data[1][1] > 0.8:
                        r[0] = data[1][0]
                        r[1] = results[i+1][1][0]
                    else:
                        r[0] = "未知"
                if "登记时间" in data[1][0]:
                    if data[1][1] > 0.8:
                        r[2] = data[1][0].split("：")[1].split("-")[0] + "-" + \
                               data[1][0].split("：")[1].split("-")[1] + "-" + \
                               data[1][0].split("：")[1].split("-")[2][:2] + " " + \
                               data[1][0].split("：")[1].split("-")[2][2:]
                    else:
                        r[2] = "未知"
                if "上报时间" in data[1][0]:
                    if data[1][1] > 0.8:
                        r[3] = data[1][0].split("：")[1]
                    else:
                        r[3] = "未知"
                if "阴性" in data[1][0] or "阳性" in data[1][0]:
                    if data[1][1] > 0.8:
                        r[4] = data[1][0][-2:]
                    else:
                        r[4] = "未知"
                if "码" in data[1][0]:
                    if data[1][1] > 0.8:
                        r[5] = data[1][0]
                    else:
                        r[5] = "未知"
                if "完成" in data[1][0]:
                    if data[1][1] > 0.8:
                        r[6] = data[1][0].split("您")[1]
                    else:
                        r[6] = "未知"

            write.writerow(r)
            f.close()
    print("写入csv文件完成")


if __name__ == '__main__':
    ocr('images', 'csv/')
