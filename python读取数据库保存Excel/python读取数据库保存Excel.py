import pymysql
import xlwt


def execude_sql():
    con = pymysql.connect(host='101.34.178.236', user='matt', password='1230',database= 'matt', charset='utf8')  # 连接数据库
    # 创建游标
    cur = con.cursor()
    # 如果存在student表，则删除
    cur.execute("DROP TABLE IF EXISTS student")
    # 创建student表
    sql = """
            create table student(
            id int not null,
            name char(10),
            age int,
            address char(20),
            create_time datetime)
        """
    cur.execute(sql) # args即要传入SQL的参数  # 执行SQL，sql为你要执行的SQL语句，如果是简单的SQL语句使用''单引号引起来就好，如果SQL较复杂，可以使用“”双引号代替
    result = cur.fetchall()  # 获取全部查询结果，fetchone()获取结果集的第一个数据
    cur.close()  # 关闭游标
    con.close()  # 关闭数据库连接

# 写入Excel ------ xlwt
def wite_to_excel(name):
    filename = name + '.xls'  # 定义Excel名字
    wbk = xlwt.Workbook()  # 实例化一个Excel
    sheet1 = wbk.add_sheet('sheet1', cell_overwrite_ok=True)  # 添加该Excel的第一个sheet，如有需要可依次添加sheet2等
    fileds = [u'ID编号', u'名字']  # 直接定义结果集的各字段名
    execude_sql(1024)  # 调用函数执行SQL，获取结果集
    for filed in range(0, len(fileds)):  # 写入字段信息
        sheet1.write(0, filed, fileds[i])
    for row in range(1, len(result) + 1):# 写入SQL查询数据
        for col in range(0, len(fileds)):
            sheet1.write(row, col, result[row - 1][col])
    wbk.save(filename)  # 保存Excel

# Excel格式调整
def set_style(name,height,bold=False):
    style = xlwt.XFStyle() # 初始化样式
    font = xlwt.Font() # 为样式创建字体
    font.name = name # 'Times New Roman'
    font.bold = bold  #是否加粗，默认不加粗
    font.color_index = 4
    font.height = height  #定义字体大小
    style.font = font
    alignment = xlwt.Alignment() #创建居中
    alignment.horz = xlwt.Alignment.HORZ_CENTER #可取值: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
    alignment.vert = xlwt.Alignment.VERT_CENTER # 可取值: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
    style.alignment = alignment # 文字居中


if __name__ == '__main__':
    execude_sql()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
