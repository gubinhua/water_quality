

def judge(dic,value):
    if dic['name'].upper() == 'PH' or dic['name'].upper() == 'PH值':
        if 6.5<=value<=8.5:
            return 'Ⅰ~Ⅲ'
        elif 5.5<=value<6.5 or 8.5<value<=9.0:
            return 'Ⅳ'
        else:
            return 'Ⅴ'
    if dic['one']>=value:
        return 'Ⅰ'
    elif dic['two']>=value:
        return 'Ⅱ'
    elif dic['three']>=value:
        return 'Ⅲ'
    elif dic['four']>=value:
        return 'Ⅳ'
    else:
        return 'Ⅴ'


#1、读取标准数据库
import pandas as pd
def readDB(filepath):
    excel_data = pd.read_excel(filepath)
    df = pd.DataFrame(excel_data,index = None)
    print(df)
filepath = r"C:\Users\GBH\Desktop\gw.xlsx"
readDB(filepath)



#2、读取待处理数据:指标名称：第几列，监测值：第几列： 点位个数： 


#3、数据标准化：
    #1）将括号、逗号、横杠全部替换为英文输入法下的字符；同时将科学表示法（'*10-N或×10-N'）全部转化为小数
    #2）提取在数据库中的指标，形成一个列表;同时提示输入不重复指标总数以及识别指标总数，判定是否提示用户检查指标名称。
    #3）单位标准化为数据库单位

#4 核心工作:水质类别判定（注意特殊指标的处理）
    #1）地下水质量标准：PH、总α放射性、总β放射性
    #2)地表水质量标准：溶解氧、ph

#5 结果输出：格式：[name,unit,value1,type1,value2,type2,...]

