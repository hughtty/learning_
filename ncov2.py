import requests
import json
from pyecharts.charts import Map, Geo
from pyecharts import options as opts
from pyecharts.globals import GeoType,RenderType
import time

import json
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
data = json.loads(requests.get(url=url).json()['data'])
china = data['areaTree'][0]['children']





china_total = "确诊:%d "% data['chinaTotal']['confirm'] + \
              " 疑似:%d " % data['chinaTotal']['suspect'] + \
              " 死亡:%d " %  data['chinaTotal']['dead'] +  \
              " 治愈:%d " %  data['chinaTotal']['heal'] +\
              "  更新时间："+ time.strftime('%Y-%m-%d %H:%M',time.localtime())

max0=data['chinaTotal']['confirm']
data = []
for i in range(len(china)):
    data.append([china[i]['name'],china[i]['total']['confirm']])

geo = Geo(init_opts = opts.InitOpts(width="1300px",height="700px",bg_color="#404a59",page_title="全国疫情实时报告",renderer=RenderType.SVG,theme="white"))

geo.add_schema(maptype="china",itemstyle_opts=opts.ItemStyleOpts(color="rgb(225,238,210)",border_color="rgb(0,0,0)"))#中国地图，地图区域颜色，区域边界颜色    
geo.add(series_name="geo",data_pair=data,type_=GeoType.EFFECT_SCATTER)#设置地图数据，动画方式为涟漪特效effect scatter    
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False),effect_opts = opts.EffectOpts(scale = 6))#设置涟漪特效缩放比例    
geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(min_=0,max_=max0/len(data)), title_opts=opts.TitleOpts(title="全国疫情地图", subtitle=china_total,pos_left="center",pos_top="10px",title_textstyle_opts=opts.TextStyleOpts(color="#fff")),legend_opts = opts.LegendOpts(is_show=False))

geo.render(path="ChinaMap.html")#输出html
