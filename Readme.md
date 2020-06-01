## 关于CV Tool
当前版本最新版本为0.5.1.b4
软件仍处于测试阶段，图像功能基本完成，视频功能尚未完成

## 运行环境
Python 3.7
PyQt5.13.0
Numpy1.18.2
Matplotlib3.2.1

注：PyQt在不同python版本下可能会出现不兼容的情况

## 安装环境
安装python3.7和pip这里不在赘述

安装第三方库
pip3 install pyqt5==5.13.0 numpy==1.18.2 matplotlib==3.2.1

## 界面部分
### 图像处理界面如下所示
![](https://cdn.site.taoidle.com/wp-content/uploads/2020/04/wp_editor_md_d9f01e88ed9c304a10405e488c6082a5.jpg)

左边为工具栏，可以选择工具栏里的功能对图像进行处理

当前版本工具栏一共分为8个部分

图像基本处理：恢复原图，上一步图像，灰度化，反相，二值化 ，自动二值化，亮度对比度

图像位置变换：水平镜像，垂直镜像，顺时针旋转90度，逆时针旋转90度

图像噪声添加：椒盐噪声，高斯噪声

图像滤波处理：均值滤波，中值滤波，方框滤波，高斯滤波，双边滤波

图像边缘检测：Canny算子，Sobel算子，Laplace算子，Scharr滤波器

图像形态学操作 ：膨胀，腐蚀，开运算，闭运算，顶帽，黑帽，形态学梯度

图像信息嵌入：LSB嵌入

图像信息提取：LSB提取

注：该版本为对中文嵌入进行处理，只能嵌入英文

### 视频处理界面如下所示

![](https://cdn.site.taoidle.com/wp-content/uploads/2020/04/wp_editor_md_b9c5ac975cc3a4a205735a8de70f3007.jpg)

注：当前视频功能尚未完成，这部分暂不做说明

### 直方图显示界面如下所示
![](https://cdn.site.taoidle.com/wp-content/uploads/2020/04/wp_editor_md_db768a2d1346824f391a225d1963ec17.jpg)

### 操作实例

开打图像

![](https://cdn.site.taoidle.com/wp-content/uploads/2020/04/wp_editor_md_e511343b09cc081918455191d329be43.jpg)

![](https://cdn.site.taoidle.com/wp-content/uploads/2020/04/wp_editor_md_8a64d3c5f7e42c22f145188efe2dd4d0.jpg)

观察图像直方图

![](https://cdn.site.taoidle.com/wp-content/uploads/2020/04/wp_editor_md_4956b5644d05df7dc42b1162af8868db.jpg)

![](https://cdn.site.taoidle.com/wp-content/uploads/2020/04/wp_editor_md_ebfc8d39d885a5a334f7e9f3ce18cec8.jpg)

图像边缘检测

![](https://cdn.site.taoidle.com/wp-content/uploads/2020/04/wp_editor_md_a6573ae844443aaab4ef86004a375d17.jpg)

![](https://cdn.site.taoidle.com/wp-content/uploads/2020/04/wp_editor_md_8b20c24dd48de19270a5f357ee87b98d.jpg)

![](https://cdn.site.taoidle.com/wp-content/uploads/2020/04/wp_editor_md_dfbd626bdfbcc6335077925eff52d090.jpg)

图像信息嵌入

![](https://cdn.site.taoidle.com/wp-content/uploads/2020/04/wp_editor_md_d8c562da0b6ebde95f1d8743a573e18e.jpg)

图像信息提取

![](https://cdn.site.taoidle.com/wp-content/uploads/2020/04/wp_editor_md_7313b0e3c6a563e4dfc43acee6e44bd2.jpg)

![](https://cdn.site.taoidle.com/wp-content/uploads/2020/04/wp_editor_md_cab210e0c8713d42f348dbc0d16548db.jpg)

![](https://cdn.site.taoidle.com/wp-content/uploads/2020/04/wp_editor_md_9ffff702eea373601860ff1c8884f309.jpg)

![](https://cdn.site.taoidle.com/wp-content/uploads/2020/04/wp_editor_md_84a023c42a22b7523a734d5733710baf.jpg)