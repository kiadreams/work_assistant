from openpyxl.styles import Border, Side


class WorkSheetStyles:

    def __init__(self) -> None:
        self.width_of_columns = {17: ("B", "C"), 5: ("A",)}
        self.height_of_rows = {70: (4, 7), 35: (5, 14), 25: (*range(16, 24), *range(28, 36), 26)}
        self.merge_columns_of_row = {
            "C:D": "4",
            "E:H": "4",
            "C:H": "5:6:7:8:9:10:11:12",
            "E:K": "14",
            "A:C": "24:25:26:27",
            "B:H": "2",
            "B:D": "37",
            "G:H": "37",
        }
        self.merge_rows_of_column = {"14:15": "A:B:C:D"}
        self.merge_rows_and_columns: list[str] = []
        self.border_cells = {
            self.__create_border(
                side_style="thin",
            ): ("E16:K23",),
            self.__create_border(side_style="medium"): ("B4:I12", "A14:D35", "E14:K15", "E24:K27"),
            self.__create_border(side_style="medium", border_type="left"): ("L16:L23",),
        }

    @property
    def cells_to_merge(self) -> tuple[str, ...]:
        return tuple(
            self.__get_range_cells_from_rows()
            + self.__get_range_cells_from_columns()
            + self.merge_rows_and_columns
        )

    def __get_range_cells_from_columns(self) -> list[str]:
        range_of_cells = []
        for columns, rows in self.merge_columns_of_row.items():
            column_start, column_end = columns.split(":")
            for row in rows.split(":"):
                range_of_cells.append(":".join((column_start + row, column_end + row)))
        return range_of_cells

    def __get_range_cells_from_rows(self) -> list[str]:
        range_of_cells = []
        for rows, columns in self.merge_rows_of_column.items():
            row_start, row_end = rows.split(":")
            for column in columns.split(":"):
                range_of_cells.append(":".join((column + row_start, column + row_end)))
        return range_of_cells

    @staticmethod
    def __create_border(side_style: str, border_type: str = "full") -> Border:
        type_side = Side(style=side_style)
        match border_type.lower():
            case "top":
                return Border(top=type_side)
            case "left":
                return Border(left=type_side)
            case _:
                return Border(top=type_side, right=type_side, bottom=type_side, left=type_side)
