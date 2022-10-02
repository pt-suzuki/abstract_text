from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import time

start_index = 0
end_index = 1000

def get_content(id):
    time.sleep(10)

    url = 'https://news.livedoor.com/article/detail/'+id+'/'

    print(url)
    try:
        with urlopen(url) as res:
            output1 = ''
            html = res.read().decode('euc_jp', 'ignore')
            soup = BeautifulSoup(html, 'html.parser')
            line_list = soup.select('.articleBody p')
            for line in line_list:
                if len(line.contents) > 0 and type(line.contents[0]) == NavigableString:
                    output1 += line.contents[0].strip()
            if output1 == '':
                print('なし1')
                return
            output1 += '\n'

            output0 = ''
            summary_list = soup.select('.summaryList li')
            for summary in summary_list:
                output0 += summary.contents[0].strip()+'\t'
            if output0 == '':
                print('なし0')
                return

            print(output0+output1)
            with open('output.tsv', mode ='a') as f:
                f.writelines(output0+output1)
    except Exception:
        print('Exception')

id_list = []
with open('ThreeLineSummaryDataset/data/train.csv', mode='r') as f:
    lines = f.readlines()
    for line in lines:
        id = line.strip().split(',')[3].split('.')[0]
        id_list.append(id)

for i in range(start_index, end_index):
    print('index:', i)
    get_content(id_list[i])
