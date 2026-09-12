from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo
from pathlib import Path

out_dir = Path('C:/Users/24779/Desktop/AI related/CaseB_Crawler/results')
out_dir.mkdir(parents=True, exist_ok=True)
out_file = out_dir / 'A_result.xlsx'

wb = Workbook()
ws = wb.active
ws.title = '汇总'

blue = '1F4E78'
white = 'FFFFFF'
thin = Side(style='thin', color='D9D9D9')
border = Border(left=thin, right=thin, top=thin, bottom=thin)

def style_sheet(ws, freeze='A2'):
    ws.freeze_panes = freeze
    ws.sheet_view.showGridLines = False
    for row in ws.iter_rows():
        for cell in row:
            cell.alignment = Alignment(vertical='center', wrap_text=True)
            cell.border = border
    for cell in ws[1]:
        cell.font = Font(bold=True, color=white)
        cell.fill = PatternFill('solid', fgColor=blue)
        cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    widths = {}
    for row in ws.iter_rows():
        for cell in row:
            val = '' if cell.value is None else str(cell.value)
            widths[cell.column] = max(widths.get(cell.column, 8), min(max(len(val) + 2, 10), 45))
    for col, width in widths.items():
        ws.column_dimensions[get_column_letter(col)].width = width
    ws.auto_filter.ref = ws.dimensions

def add_table(ws, name):
    if ws.max_row >= 2 and ws.max_column >= 1:
        ref = f'A1:{get_column_letter(ws.max_column)}{ws.max_row}'
        tab = Table(displayName=name, ref=ref)
        style = TableStyleInfo(name='TableStyleMedium2', showFirstColumn=False, showLastColumn=False, showRowStripes=True, showColumnStripes=False)
        tab.tableStyleInfo = style
        ws.add_table(tab)

def add_sheet(title, rows, table_name):
    global ws
    ws = wb.active if title == '汇总' else wb.create_sheet(title)
    if title != '汇总':
        ws.title = title
    for r in rows:
        ws.append(r)
    style_sheet(ws)
    add_table(ws, table_name)

add_sheet('汇总', [
    ['类型','萤石','氢氟酸 / 氟化氢','来源/备注'],
    ['最新价格','2026-09-11：萤石97%酸级精粉 3250-3850 元/吨，持平','2026-09-11：无水氟化氢 15100-15300 元/吨，持平','9月11日氟化工产业链价格表；单位元/吨'],
    ['价格走势','2024-2026图：约3000-3700元/吨；2026年初后回升','2024-2026图：约10000-14000+元/吨；2026年明显上行','走势图为图片，点位为OCR/视觉近似'],
    ['2026年1-5月进口','≤97%：716,719吨；＞97%：33,989吨；正文合计75.10万吨','其他氟化氢/氢氟酸：1,223.4吨','fuwushidian/94356.html'],
    ['2026年1-5月出口','≤97%：81,369吨；＞97%：82,208吨','其他氟化氢/氢氟酸：76,941吨；正文称氟化氢总出口10.15万吨','口径可能不同，需海关编码表核对'],
    ['2025年进口','≤97%：1,824,033吨；＞97%：93,012吨；正文合计191.7万吨','其他氟化氢/氢氟酸：161.6吨','fuwushidian/83495.html'],
    ['2025年出口','≤97%：188,778吨；＞97%：104,858吨','其他氟化氢/氢氟酸：240,932吨；正文称氟化氢总出口24.1万吨','fuwushidian/83495.html'],
    ['产量/产能','公开页显示2026年3月起多地萤石矿山减产、停产范围扩大；未抓到全国具体产量值','未抓到具体产量值','fuwushidian/97054.html'],
    ['消费量','未抓到明确消费量','未抓到明确消费量','公开可访问页面未发现量化消费统计'],
], 'SummaryTable')

add_sheet('价格数据', [
    ['类别','产品','日期/时间范围','价格/区间','单位','涨跌','来源URL','备注'],
    ['最新价格表','萤石（97%酸级精粉）','2026-09-11','3250-3850','元/吨','持平','https://www.fuwuzaixian.cn/quanchanyelianjiagebiao/100698.html','萤石/氟化氢为送到价格'],
    ['最新价格表','无水氟化氢','2026-09-11','15100-15300','元/吨','持平','https://www.fuwuzaixian.cn/quanchanyelianjiagebiao/100698.html','送到价格'],
    ['价格走势','CaF2≥97%萤石粉','2024-01-15至2026-04-15附近','约3000-3700；最新约3500','元/吨','2026年初至4月回升','https://www.fuwuzaixian.cn/jiagezoushi/90371.html','图片OCR/视觉近似，无法精确逐日点位'],
    ['价格走势','无水氟化氢','2024-01-15至2026-04-15附近','约10000-14000+；最新约14000','元/吨','2026年初后明显上行','https://www.fuwuzaixian.cn/jiagezoushi/90372.html','图片OCR/视觉近似；9月价格表已达15100-15300'],
], 'PriceTable')

add_sheet('进出口_2026_1-5', [
    ['产品','2026年1-5月进口量(吨)','2025年1-5月进口量(吨)','进口同比','2026年1-5月出口量(吨)','2025年1-5月出口量(吨)','出口同比','来源URL','备注'],
    ['萤石（≤97%含量）',716719,679408,'+5%',81369,77875,'+4%','https://www.fuwuzaixian.cn/fuwushidian/94356.html','图片表OCR'],
    ['萤石（＞97%含量）',33989,27080,'+26%',82208,34515,'+138%','https://www.fuwuzaixian.cn/fuwushidian/94356.html','图片表OCR'],
    ['其他氟化氢（氢氟酸）',1223.4,143.5,'+752%',76941,104187,'-26%','https://www.fuwuzaixian.cn/fuwushidian/94356.html','与正文“氟化氢总出口10.15万吨”口径可能不同'],
], 'Trade2026Table')

add_sheet('2026正文补充', [
    ['项目','数据','单位/口径','来源URL','备注'],
    ['2026年1-5月萤石合计进口量','75.10','万吨','https://www.fuwuzaixian.cn/fuwushidian/94356.html','正文'],
    ['萤石进口同比','+6.26%','同比','https://www.fuwuzaixian.cn/fuwushidian/94356.html','正文'],
    ['2026年1-5月萤石（≤97%）总出口量','8.14','万吨','https://www.fuwuzaixian.cn/fuwushidian/94356.html','正文'],
    ['萤石（≤97%）出口同比','+4.5%','同比','https://www.fuwuzaixian.cn/fuwushidian/94356.html','正文'],
    ['2026年1-5月萤石（＞97%）总出口量','8.22','万吨','https://www.fuwuzaixian.cn/fuwushidian/94356.html','正文'],
    ['萤石（＞97%）出口同比','+138%','同比','https://www.fuwuzaixian.cn/fuwushidian/94356.html','正文'],
    ['2026年1-5月氟化氢总出口','10.15','万吨','https://www.fuwuzaixian.cn/fuwushidian/94356.html','正文；可能不同于表中“其他氟化氢（氢氟酸）”'],
    ['氟化氢出口同比','-2.3%','同比','https://www.fuwuzaixian.cn/fuwushidian/94356.html','正文'],
    ['5月萤石（≤97%）自蒙古进口量','12.31','万吨','https://www.fuwuzaixian.cn/fuwushidian/94356.html','正文'],
    ['5月自蒙古进口环比','-5.30%','环比','https://www.fuwuzaixian.cn/fuwushidian/94356.html','正文'],
], 'Trade2026TextTable')

add_sheet('进出口_2025全年', [
    ['产品','2025年进口量(吨)','2024年进口量(吨)','进口同比','2025年出口量(吨)','2024年出口量(吨)','出口同比','来源URL','备注'],
    ['萤石（≤97%含量）',1824033,1314891,'+39%',188778,190229,'-1%','https://www.fuwuzaixian.cn/fuwushidian/83495.html','图片表OCR'],
    ['萤石（＞97%含量）',93012,32572,'+186%',104858,54561,'+92%','https://www.fuwuzaixian.cn/fuwushidian/83495.html','图片表OCR'],
    ['其他氟化氢（氢氟酸）',161.6,209.3,'-23%',240932,227595,'+6%','https://www.fuwuzaixian.cn/fuwushidian/83495.html','图片表OCR'],
], 'Trade2025Table')

add_sheet('2025正文补充', [
    ['项目','数据','单位/口径','来源URL','备注'],
    ['2025年萤石合计进口量','191.7','万吨','https://www.fuwuzaixian.cn/fuwushidian/83495.html','正文'],
    ['萤石进口同比','+42.3%','同比','https://www.fuwuzaixian.cn/fuwushidian/83495.html','正文'],
    ['2025年萤石（≤97%）总出口量','18.87','万吨','https://www.fuwuzaixian.cn/fuwushidian/83495.html','正文'],
    ['萤石（≤97%）出口同比','-0.76%','同比','https://www.fuwuzaixian.cn/fuwushidian/83495.html','正文'],
    ['2025年萤石（＞97%）总出口量','10.48','万吨','https://www.fuwuzaixian.cn/fuwushidian/83495.html','正文'],
    ['萤石（＞97%）出口同比','+92%','同比','https://www.fuwuzaixian.cn/fuwushidian/83495.html','正文'],
    ['2025年氟化氢总出口','24.1','万吨','https://www.fuwuzaixian.cn/fuwushidian/83495.html','正文'],
    ['氟化氢出口同比','+6%','同比','https://www.fuwuzaixian.cn/fuwushidian/83495.html','正文'],
    ['2025年萤石（＞97%）主要进口来源','蒙古、赞比亚','','https://www.fuwuzaixian.cn/fuwushidian/83495.html','正文'],
    ['2025年自蒙古进口萤石量','169.3','万吨','https://www.fuwuzaixian.cn/fuwushidian/83495.html','正文'],
    ['蒙古占萤石进口总量比例','88.3%','占比','https://www.fuwuzaixian.cn/fuwushidian/83495.html','正文'],
], 'Trade2025TextTable')

add_sheet('产量产能政策', [
    ['项目','信息','来源URL','备注'],
    ['影响时间','自2026年3月起','https://www.fuwuzaixian.cn/fuwushidian/97054.html','公开文章'],
    ['影响区域','浙江、江西、福建、内蒙古等核心萤石产区','https://www.fuwuzaixian.cn/fuwushidian/97054.html','公开文章'],
    ['影响方向','萤石矿山停产范围持续扩大，核心产区减产现象普遍','https://www.fuwuzaixian.cn/fuwushidian/97054.html','公开文章'],
    ['原因','国家及地方安全、生态环保专项监管约束','https://www.fuwuzaixian.cn/fuwushidian/97054.html','公开文章'],
    ['地下生产矿山整改节点','2027年5月1日前完成自建队伍或整体托管','https://www.fuwuzaixian.cn/fuwushidian/97054.html','公开文章'],
    ['露天生产矿山整改节点','2028年5月1日前完成自建队伍或整体托管','https://www.fuwuzaixian.cn/fuwushidian/97054.html','公开文章'],
    ['浙江政策目标','到2026年底，正常生产建设地下矿山采掘作业100%实现机械化、无人化','https://www.fuwuzaixian.cn/fuwushidian/97054.html','公开文章'],
    ['浙江小型地下矿山要求','到2026年底，生产规模3万吨以下地下矿山全部关停','https://www.fuwuzaixian.cn/fuwushidian/97054.html','公开文章'],
    ['浙江中长期目标','到2027年底淘汰20座小型地下矿山；到2028年底大中型地下矿山占比提高到70%以上；到2029年底生产规模5万吨以下地下矿山全部关停','https://www.fuwuzaixian.cn/fuwushidian/97054.html','公开文章'],
    ['具体全国萤石产量','未抓到公开量化数值','https://www.fuwuzaixian.cn/fuwushidian/85191.html','相关页面有登录/验证码限制，未绕过'],
], 'PolicyTable')

add_sheet('消费与限制', [
    ['类别','结果','来源/说明'],
    ['萤石消费量','未抓到明确消费量','公开可访问页面未发现量化消费统计'],
    ['氢氟酸/氟化氢消费量','未抓到明确消费量','公开可访问页面未发现量化消费统计'],
    ['受限页面','2026年1-7月进出口数据、2026年中国萤石产量增长展望等页面出现会员登录/验证码','未尝试绕过验证码或登录'],
    ['抓取方式','web_extract、Google Chrome/Playwright渲染、Scrapling fetch/stealthy-fetch','请求间隔约3秒；仅个人研究用途'],
    ['数据置信度','价格表与进出口表较高；图片走势图为近似；受限页面缺失降低完整性','建议用海关编码原表交叉验证'],
], 'LimitsTable')

add_sheet('来源清单', [
    ['来源URL','页面标题','抓取/提取结果'],
    ['https://www.fuwuzaixian.cn/','氟务在线-专注于氟化工产业链一站式服务','主页发现目标分类、价格表、进出口和价格走势链接'],
    ['https://www.fuwuzaixian.cn/quanchanyelianjiagebiao/100698.html','9月11日氟化工产业链价格表！','提取萤石、无水氟化氢价格'],
    ['https://www.fuwuzaixian.cn/jiagezoushi/90371.html','2024年-2026年国内CaF2≥97%萤石粉价格走势图','提取萤石粉价格趋势，图片近似'],
    ['https://www.fuwuzaixian.cn/jiagezoushi/90372.html','2024年-2026年国内无水氟化氢价格走势图','提取无水氟化氢价格趋势，图片近似'],
    ['https://www.fuwuzaixian.cn/fuwushidian/94356.html','2026年1-5月|最新氟化工进出口数据变化！','提取2026年1-5月进出口数据'],
    ['https://www.fuwuzaixian.cn/fuwushidian/83495.html','年度汇总！2025年氟化工产品进出口数据最新出炉','提取2025年全年进出口数据'],
    ['https://www.fuwuzaixian.cn/fuwushidian/97054.html','最新政策梳理！监管历史最严，萤石矿山减产扩容','提取产能/减产政策信息'],
    ['https://www.fuwuzaixian.cn/fuwushidian/85191.html','氟务解读！2026年中国萤石产量增长展望','页面需登录/验证码；未提取具体产量预测数据'],
], 'SourcesTable')

for ws in wb.worksheets:
    for row in ws.iter_rows():
        for cell in row:
            if isinstance(cell.value, (int, float)):
                cell.number_format = '#,##0.0' if isinstance(cell.value, float) and not float(cell.value).is_integer() else '#,##0'

wb.save(out_file)

# Verification
wb2 = load_workbook(out_file, read_only=True, data_only=False)
print(out_file)
print('verified exists:', out_file.exists(), 'size:', out_file.stat().st_size)
for s in wb2.worksheets:
    print(s.title, s.max_row, s.max_column)
