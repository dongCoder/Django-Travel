# 基于Django的定点景点及酒店推荐预订系统
本系统使用Python 3.7+Django 2.1.8+MySQL 8.0
- 前置准备条件
  - matplotlib安装
    - pip install matplotlib
  - PIL安装
    - pip install Pillow
  - re安装
    - pip install re
- 建立数据库
  - 数据库名：travel
  - setting中可自行修改数据库名称，用户名及密码
- 运行
  - Python manage.py runserver
    - 打开网页，键入：127.0.0.1:8000
  - python manage.py runserver 0.0.0.0
    - 允许在同一内网的所有主机访问该网站
- 目录结构
  - Travels
    - 为Django的主目录，内含setting,urls等配置文件
  - templates
    - 存放前端页面
  - static
    - 存放静态文件
  - media
    - 存放上传文件
  - pay
    - 订单支付文件
  - new
    - 普通用户后台
    - 景区，酒店管理人员后台
  - index
    - 前端静态页面渲染
- 数据库
  - attractions_datail
    - 景点详情信息存储
  - attractions_img
    - 景点图片存储
  - attractions_order
    - 景点订单
  - attractions_price
    - 景点票价信息存储
  - auth_group
    - 用户组
  - auth_user
    - 用户信息存储
  - django_session
    - 存储用户登录session
  - flow
    - 景区流量分析信息以及自动生成的图集存储
  - home_datail
    - 酒店房型信息存储
  - hotel_datail
    - 酒店信息存储
  - hotel_img
    - 酒店图片存储
  - hotel_order
    - 酒店订单存储
  - news
    - 新闻存储
  - publicity_photo
    - 宣传照存储
  - user_information
    - 用户详情信息存储
  - user_order
    - 用户订单存储
  
