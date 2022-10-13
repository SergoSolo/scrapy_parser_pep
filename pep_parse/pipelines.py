import csv
import datetime
from collections import Counter

from pep_parse.settings import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:
    statuses = []

    def open_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        now = datetime.datetime.now()
        now_formated = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formated}.csv'
        self.file_path = results_dir / file_name

    def process_item(self, item, spider):
        self.statuses.append(item['status'])
        self.status_counter = Counter(self.statuses)
        self.total = len(self.statuses)
        return item

    def close_spider(self, spider):
        with open(self.file_path, 'w', encoding='utf-8', newline='') as file:
            field_name = ['Статус', 'Количество']
            writer = csv.DictWriter(file, fieldnames=field_name)
            writer.writeheader()
            for status, amount in self.status_counter.items():
                writer.writerow(
                    {'Статус': f'{status}', 'Количество': f'{amount}'}
                )
            writer.writerow({'Статус': 'Total', 'Количество': f'{self.total}'})
