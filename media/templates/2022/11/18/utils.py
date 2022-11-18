import requests
import config
from docxtpl import DocxTemplate

class Utils:
    def __init__(self) -> None:
        self.session = requests.Session()

    def get_doc_name(self,date:str):
        response = self.session.get(f'{config.API}?date={date}')
        data_json = response.json()
        if len(data_json)==0:
            return
        doc_name = str(DocumentMaker(data_json, date))
        return doc_name


class DocumentMaker:
    def __init__(self, json_data, date) -> None:
        self.data = json_data
        self.date = date
        self.doc_name = self.make_document()

    def make_document(self):
        text_list = [self.make_one_task_text(key.get('fields'),index+1) for index,key in enumerate(self.data)]
        document_text = "\n".join(text_list)
        template = DocxTemplate('template.docx')       
        template.render({"data":document_text})
        doc_name = f"Задачи на {self.date}.docx"
        template.save(doc_name)
        return doc_name
        

    def make_one_task_text(self, task_fields, index):
        text = list()
        text.append(f"{index}. {task_fields.get('title')} : {task_fields.get('appoint_to')}")
        text.append(f"{task_fields.get('typing')}")
        text.append(f"{task_fields.get('content')}")
        text.append("\n")
        return "\n".join(text)

    def __str__(self) -> str:
        return self.doc_name
