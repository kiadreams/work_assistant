import string

from openpyxl.drawing.image import Image
from openpyxl.styles import Alignment, Font
from openpyxl.utils import coordinate_to_tuple, get_column_letter


class WorkSheetContent:
    base_font = Font(size=10, name='Arial Cyr')
    base_alignment = Alignment(wrap_text=True)

    text_of_cells = {
        'Ведомость фактического учета трудоемкости работ': (
            'B2',
            Font(bold=True, size=12, name='Arial Cyr'),
            Alignment(horizontal='center', vertical='center')
        ),
        '№ заказа из АСУ ТОиР': ('B4', base_font, base_alignment),
        '№ объекта (его признак из АСУ ТОиР)': ('B5', base_font, base_alignment),
        'Код работы': ('B6', base_font, base_alignment),
        'Наименование работ': ('B7', base_font, base_alignment),
        'Дата начала работ': ('B8', base_font, base_alignment),
        'Дата окончания работ': ('B9', base_font, base_alignment),
        'Наименование МЭС': ('B10', base_font, base_alignment),
        'Наименование ПМЭС': ('B11', base_font, base_alignment),
        'Наименование ПС (ВЛ)': ('B12', base_font, base_alignment),
        'МЭС Юга': ('C10', base_font, base_alignment),
        'Кубанское ПМЭС': ('C11', base_font, base_alignment),
        'ПС 330 кВ Армавир': ('C12', base_font, base_alignment),
        'Доставка персонала (перебазировка)': ('A24', base_font, base_alignment),
        'Итого по бригаде': ('A25', base_font, base_alignment),
        'Итого по бригаде с учетом перебазировки': ('A26', base_font, Alignment(wrap_text=True, vertical='center')),
        'в том числе по категориям рабочих': ('A27', base_font, base_alignment),
        'Вед.инженер-рук. СВ УРЗА СРЗА и АСУТП': ('B37', base_font, base_alignment),
        'Лебедев А.В.': ('G37', base_font, base_alignment),
        '=IF(SUM(E16:E24)=0,IF(SUM(F16:F24)=0,IF(SUM(G16:G24)=0,IF(SUM(H16:H24)=0,IF(SUM(I16:I24)=0,IF(SUM(J16:J24)=0,'
        'K15,J15),I15),H15),G15),F15),E15)': (
            'C8',
            base_font,
            Alignment(wrap_text=True, horizontal='left', vertical='center')
        ),
        '=IF(SUM(K16:K24)=0,IF(SUM(J16:J24)=0,IF(SUM(I16:I24)=0,IF(SUM(H16:H24)=0,IF(SUM(G16:G24)=0,IF(SUM(F16:F24)=0,'
        'E15,F15),G15),H15),I15),J15),K15)': (
            'C9',
            base_font,
            Alignment(wrap_text=True, horizontal='left', vertical='center')
        ),
        '№ п/п': (
            'A14',
            Font(bold=True, size=10, name='Arial Cyr'),
            Alignment(wrap_text=True, horizontal='center', vertical='center'),
        ),
        'ФИО': (
            'B14',
            Font(bold=True, size=10, name='Arial Cyr'),
            Alignment(wrap_text=True, horizontal='center', vertical='center'),
        ),
        'Разряд': (
            'C14',
            Font(bold=True, size=10, name='Arial Cyr'),
            Alignment(wrap_text=True, horizontal='center', vertical='center'),
        ),
        'Итого, чел/час': (
            'D14',
            Font(bold=True, size=10, name='Arial Cyr'),
            Alignment(wrap_text=True, horizontal='center', vertical='center'),
        ),
    }

    text_cascade_of_cells = {
        string.Template('=IF(SUM($r_1:$r_2)=0,"",SUM($r_1:$r_2))'): (
            {'r': 'D16', 'r_1': 'E16', 'r_2': 'K16'},
            (1, 1, 1),
            8,
            Font(bold=True, size=10, name='Arial Cyr'),
            Alignment(horizontal='center', vertical='center')
        ),
        string.Template('=IF(SUM($c_1:$c_2)=0,"",SUM($c_1:$c_2))'): (
            {'c': 'D25', 'c_1': 'D16', 'c_2': 'D24'},
            (1, 1, 1),
            8,
            Font(bold=True, size=10, name='Arial Cyr'),
            Alignment(horizontal='center', vertical='center')
        ),
        string.Template('=$r_1'): (
            {'r': 'D28', 'r_1': 'D16'},
            (1, 1),
            8,
            Font(bold=True, size=10, name='Arial Cyr'),
            Alignment(horizontal='center', vertical='center')
        ),
    }

    image_of_cells = {'E36': 'src/images/img.png'}

    @staticmethod
    def change_cells(cells: dict[str, str], steps: tuple[int, ...]) -> dict[str, str]:
        names, values = zip(*cells.items())
        coordinate_of_cells = map(coordinate_to_tuple, values)
        new_coordinate = []
        for i, cell in enumerate(coordinate_of_cells):
            row, column = cell
            row, column = ((row + steps[i], column) if names[i].startswith('r') else (row, column + steps[i]))
            new_coordinate.append(f'{get_column_letter(column)}{row}')
        return dict(zip(names, new_coordinate))

    @staticmethod
    def get_text_from_template(template: string.Template, values: dict[str, str]) -> str:
        return template.substitute(values)
