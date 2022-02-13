import os
import pandas as pd
for filename in os.listdir(r'./001'):
    print(filename)
    sa =pd.read_excel(r'./001/%s'% filename)
    sd = sa.iloc[5:]
    sd.columns=['统计日期',	'商品ID',	'商品名称',	'货号',	'商品状态'	,'商品标签',	'商品访客数',	'商品浏览量',
                '平均停留时长','详情页跳出率','商品收藏人数','商品加购件数','商品加购人数','下单买家数','下单件数','下单金额',
                '下单转化率','支付买家数','支付件数','支付金额','支付转化率','支付新买家数',
                '支付老买家数',	'老买家支付金额',	'聚划算支付金额',	'访客平均价值',
                '售中售后成功退款金额','竞争力评分','年累计支付金额','月累计支付金额','月累计支付件数',
                '搜索引导支付转化率',	'搜索引导访客数',	'搜索引导支付买家数']
    sq = filename.split('.')[0]
    # sd.to_excel(r'C:\Users\lenovo\Desktop\新建文件asfd夹\%s.xlsx'%sq,index =False,encoding='utf-8')
    print(sq)