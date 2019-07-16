# stopwords = {}
# splist = ["salary", "scale", "公司规模", "degree","学历要求：", "nature","公司性质：", "company",
#              "jobname", "exprience", "工作经验：", "location", "askandduty"]
# for i in splist:
#     print(i)
import json
data = {}
with open('json_test.txt',encoding='utf-8') as szh:
    data = json.load(szh)
print(data)