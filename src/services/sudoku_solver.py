from repositories.sudoku_repository import SudokuRepository
import time


class SudokuSolver:
    def __init__(self, sudoku=None):
        self.start_time = None
        self.sudoku = sudoku
        if sudoku:
            self.state = self.parse_str_to_sudoku_state(sudoku.initial_setup)
        else:
            self.state = None
        self.current_row = 4
        self.current_col = 4

    def get_sudokus_by_difficulty(self, difficulty):
        sudoku_repo = SudokuRepository()
        return sudoku_repo.find_by_difficulty(difficulty)

    def set_sudoku_solver(self, sudoku):
        self.start_time = time.time()
        self.sudoku = sudoku
        self.state = self.parse_str_to_sudoku_state(sudoku.initial_setup)

    def get_solving_time(self):
        solving_time = round(time.time() - self.start_time)
        if solving_time <= 60:
            return str(solving_time)
        seconds = solving_time % 60
        minutes = solving_time // 60
        return f'{minutes}:{seconds:0=2d}'

    def get_value_at(self, row, col):
        return self.state[row][col]

    def get_current_value(self):
        return self.state[self.current_row][self.current_col]

    def change_value_at(self, row, col, value):
        if not self.is_given(row, col):
            self.state[row][col] = value

    def change_current_value(self, value):
        if not self.is_given(self.current_row, self.current_col):
            self.state[self.current_row][self.current_col] = value

    def remove_value_at(self, row, col):
        if not self.is_given(row, col):
            self.state[row][col] = '0'

    def remove_current_value(self):
        if not self.is_given(self.current_row, self.current_col):
            self.state[self.current_row][self.current_col] = '0'

    def is_given(self, row, col):
        return self.sudoku.initial_setup[9*row + col] != '0'

    def is_selected(self, row, col):
        return row == self.current_row and col == self.current_col

    def check_answer(self):
        for row in range(9):
            for col in range(9):
                if self.state[row][col] != self.sudoku.answer[9*row + col]:
                    return False
        return True

    def get_answer(self):
        for row in range(9):
            for col in range(9):
                self.state[row][col] = self.sudoku.answer[9*row + col]

    def parse_str_to_sudoku_state(self, string):
        sudoku = []
        for i in range(9):
            sudoku.append(list(string[9*i:9*i+9]))
        return sudoku
