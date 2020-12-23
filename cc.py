from pyecharts import options as opts
from pyecharts.charts import Pie
from random import randint
from pyecharts.charts import Bar
def pie_base() -> Pie:
    c = (
        Pie()
        .add("", [list(z) for z in zip(['男','女'],[3137,46] )])
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"),toolbox_opts=opts.ToolboxOpts(is_show=True))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c

pie_base().render('gener.html')

bar = Bar()
bar.add_xaxis(['金牛座', '射手座', '双子座', '天秤座', '狮子座', '处女座', '巨蟹座', '双鱼座', '天蝎座', '水瓶座', '白羊座', '魔羯座'])
bar.add_yaxis("12星座", [334, 219, 308, 462, 292, 338, 212, 241, 281, 138, 174, 184])
bar.set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"),toolbox_opts=opts.ToolboxOpts(is_show=True))
bar.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render('xing.html') #在notebook上直接展示可用这个