import os
from src.packages.worksheets.worksheets import WorkSheets


if __name__ == '__main__':
    b_title = 'Ведомость_работ.xlsx'
    ws_first_title = 'Страница_1 V05110______'
    ws_second_title = 'Страница_2 V05110______'
    ws_third_title = 'Страница_2 V05110______'
    if os.path.exists(b_title):
        os.remove(b_title)
    work_sheet = WorkSheets(title=b_title)
    work_sheet.set_content_of_active_ws()
    work_sheet.change_active_ws_title(ws_first_title)
    work_sheet.create_new_sheet(ws_second_title)
    work_sheet.create_new_sheet(ws_third_title)
    work_sheet.save_work_sheet()
