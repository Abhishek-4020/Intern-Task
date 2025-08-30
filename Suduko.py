import tkinter as tk
from tkinter import messagebox

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        for row in range(9):
            for col in range(9):
                entry = tk.Entry(self.root, width=3, font=('Arial', 18), justify='center')
                entry.grid(row=row, column=col, padx=2, pady=2, ipady=5)
                self.entries[row][col] = entry

    def create_buttons(self):
        solve_button = tk.Button(self.root, text="Solve", command=self.solve_sudoku, bg="lightgreen", font=("Arial", 12))
        solve_button.grid(row=9, column=0, columnspan=3, sticky='nsew')

        clear_button = tk.Button(self.root, text="Clear", command=self.clear_grid, bg="lightblue", font=("Arial", 12))
        clear_button.grid(row=9, column=3, columnspan=3, sticky='nsew')

        exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, bg="lightcoral", font=("Arial", 12))
        exit_button.grid(row=9, column=6, columnspan=3, sticky='nsew')

    def get_grid(self):
        grid = []
        for row in self.entries:
            current_row = []
            for entry in row:
                val = entry.get()
                current_row.append(int(val) if val.isdigit() else 0)
            grid.append(current_row)
        return grid

    def update_grid(self, grid):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                if grid[i][j] != 0:
                    self.entries[i][j].insert(0, str(grid[i][j]))

    def is_valid(self, grid, row, col, num):
        if num in grid[row]: return False
        if num in [grid[i][col] for i in range(9)]: return False
        box_row, box_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[box_row + i][box_col + j] == num:
                    return False
        return True

    def solve(self, grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(grid, row, col, num):
                            grid[row][col] = num
                            if self.solve(grid):
                                return True
                            grid[row][col] = 0
                    return False
        return True

    def solve_sudoku(self):
        grid = self.get_grid()
        if self.solve(grid):
            self.update_grid(grid)
        else:
            messagebox.showerror("No Solution", "This Sudoku puzzle has no valid solution.")

    def clear_grid(self):
        for row in self.entries:
            for entry in row:
                entry.delete(0, tk.END)

# Start the app
if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
