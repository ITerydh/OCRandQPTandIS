# [疫情信息统计进阶篇]PPOCR和QPT的落地实战 
**--------------------------------------------OCRandQPTandIS-------------------------------------------**

Covid-19 outbreak information statistics



 
> [疫情信息统计进阶篇]PPOCR和QPT的落地实战    
> 项目地址：[https://aistudio.baidu.com/aistudio/projectdetail/3877807](https://aistudio.baidu.com/aistudio/projectdetail/3877807)   

> [PaddleOCR]核酸检测证明复查统计？50行代码轻松搞定    
> 项目地址：[https://aistudio.baidu.com/aistudio/projectdetail/3779297](https://aistudio.baidu.com/aistudio/projectdetail/3779297)  

继上篇说起，完成了ocr的核酸检测信息统计

这次主要来搞搞，如何落地实践。

项目已经放置数据集中，开箱即可使用，因为设计界面制作，请您在本地环境使用。

## 0 先看效果 ~

截图展示：
![截图展示](https://github.com/ITerydh/OCRandQPTandIS/blob/main/1.jpg)


B站视频地址：
[https://www.bilibili.com/video/BV1Hr4y1J7cR](https://www.bilibili.com/video/BV1Hr4y1J7cR)


## 1 解压文件


```python
!unzip -oq /home/aistudio/data/data141663/OcrYq.zip -d work/
```

## 2 文件介绍
![文件内容介绍](https://ai-studio-static-online.cdn.bcebos.com/9a396fb18a714f5ab313df719fa334372a9b3fb5528e4446940ea945a2e74463)


## 3 如何使用

1. 将整个项目下载到本地之后，安装

> work/requirement.txt 中的所以依赖，可能不全，自己看情况导入

2. 运行 run.py 本地项目预览
> 正常这已经可以了

3. 运行pkg.py 打包工具
> 运行之后既可在文件夹中发现out目录，根据QPT的描述进行使用即可。


## 4 实现讲解以及后续提升

**实现：**

1. 首先，肯定是ocr检测的实现，这个直接使用PPOCR的接口即可，但没有采用GPU，方便打包用户使用。
2. 对于检测得到的文本，有针对性的根据数据的特点去保存，但无法做到普适所有的疫情信息图片，这点是缺点。
3. 界面的编写，这里采用PyQt5进行实现，QT designer的界面化使得开发简单了许多，只需要合理使用信号与槽即可完成代码编写。
4. 对于界面的未响应，使用多线程来解决线程的阻塞，进而增加一点用户体验。

**提升：**

1. 由于仅仅花费了几天的时间自学PyQT，界面还需要优化，提升用户体验。
2. OCR没有进行训练，只是采用的接口快速实现，会存在识别不准的情况，但目前来看相对还好。
3. 界面中应该有进度提示，或者是文本流动，增加用户感观体验。
4. 没有采用GPU，很慢，识别起来很慢，200张图片需要15分钟。 


## 5 个人总结

全网同名：

> iterhui

我在AI Studio上获得至尊等级，点亮10个徽章，来互关呀~

> [https://aistudio.baidu.com/aistudio/personalcenter/thirdview/643467](https://aistudio.baidu.com/aistudio/personalcenter/thirdview/643467)
