""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util


DATAFILE = r"D:\Programming\Python\5th_Weekpair\secure-erp-python-csabaszl\model\crm\crm.csv"
HEADERS = ["Id", "Name", "Email", "Subscribed"]
