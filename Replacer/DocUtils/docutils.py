import os
from docxtpl import DocxTemplate
from datetime import datetime
from Replacer.models import Template, ReplaceField

class DocUtils:
    def __init__(self, template, field_list, insert_fields_list, doc_name, customer, company) -> None:
        self.template = template
        self.field_list = field_list
        self.insert_fields_list = insert_fields_list
        self.customer = customer
        self.company = company
        self.context = self.make_context_dict(self.field_list, self.insert_fields_list, self.customer, self.company)
        self.doxc_template_path = f'media/{self.template.file}'
        self.doc_name = doc_name
        
    def make_company_dict(self, company):
        context = {}
        context['company_abb'] = company.company_abb
        context['company_title'] = company.company_title
        context['manager_name'] = company.manager_name
        context['company_address'] = company.company_address
        context['manager_full_name'] = company.manager_full_name
        return context

    def make_customer_dict(self, customer):
        context = {}
        context['customer'] = customer.customer
        context['customer_abb'] = customer.customer_abb
        return context

    def make_context_dict(self, field_list, insert_fields_list, customer, company):
        context = {}
        for index, field in enumerate(field_list):
            context[field.tag] = insert_fields_list[index]

        context = {**self.make_customer_dict(customer), **self.make_company_dict(company), **context}
        return context

    def get_path_to_save(self):
        path_to_save = datetime.today().strftime('media/uploads/%Y/%m/%d/')
        if not os.path.exists(path_to_save):
            os.makedirs(path_to_save)
        return path_to_save
    
    def make_document(self):
        template = DocxTemplate(self.doxc_template_path)
        template.render(context=self.context)
        doc_path = f"{self.get_path_to_save()}{self.doc_name}.docx"
        template.save(doc_path)
        return f"/{doc_path}"
