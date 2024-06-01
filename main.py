from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import screen
from determinant import det

screen_helper = screen.screen_helper


def permute(arr, memo=None):
    if memo is None:
        memo = []
    results = []
    for i in range(len(arr)):
        cur = arr.pop(i)
        if len(arr) == 0:
            results.append(memo + [cur])
        results += permute(arr[:], memo + [cur])
        arr.insert(i, cur)
    return results


A = [[1, 0, 1], [0, 1, 0], [0, 0, 1]]
b = [1, 2, 3]


def equation(A, b, c, eps):
    A = permute(A)
    max_diagonal_prod = [0, 0]
    for i in range(len(A)):
        diagonal_prod = 1
        for j in range(len(A[i])):
            diagonal_prod *= abs(A[i][j][j])
        if max_diagonal_prod[0] < abs(diagonal_prod):
            max_diagonal_prod = [abs(diagonal_prod), i]

    A = A[max_diagonal_prod[1]]

    if det(A) == 0:
        return "Нет корней", "Нет корней", "Нет корней"
    condition = True
    print(c)
    variables0 = [0 for i in c]

    while condition:
        for i in range(len(b)):
            variables0[i] = c[i]
        for i in range(len(c)):
            form = 0
            for j in range(len(c)):
                if j != i:
                    form -= A[i][j] * c[j]
            c[i] = (b[i] + form) / A[i][i]

        print(variables0)
        if max(abs(c[i] - variables0[i]) for i in range(len(c))) <= eps or str(c[0]) == 'nan':
            condition = False
        # break
    if str(c[0]) == 'nan':
        return 'Привышено максимальное значение', 'Привышено максимальное значение', 'Привышено максимальное значение'
    return [str(c[i]) + ' ± ' + str(eps) for i in range(len(c))]


def calculating_exact(matrix1, array, q):
    matrix = []
    for i in matrix1:
        matrix.append(i.copy())
    t = det(matrix)
    print(t)
    for i in range(len(array)):
        matrix[i][q] = array[i]
    if t == 0:
        return "Нет корней"
    elif det(matrix) / t == det(matrix) // t:
        return str(int(det(matrix) // t))
    return str(det(matrix) / t)


class MenuScreen(Screen):
    pass


class ExactSolutionScreen(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.n = 3

    def change_text(self):
        # self._3_eq_layout.pos_hint = {'center_x':1.5, 'center_y':1.55}
        print(self._9_input.text, self._10_input.text, self._11_input.text)
        if self.n == 3:
            try:
                matrix = [[float(self._1_input.text), float(self._2_input.text), float(self._3_input.text)],
                          [float(self._5_input.text), float(self._6_input.text), float(self._7_input.text)],
                          [float(self._9_input.text), float(self._10_input.text), float(self._11_input.text)]]
                array = [float(self._4_input.text), float(self._8_input.text), float(self._12_input.text)]
                self.output_x.text = 'x = ' + calculating_exact(matrix, array, 0)
                print(matrix)
                self.output_y.text = 'y = ' + calculating_exact(matrix, array, 1)
                self.output_z.text = 'z = ' + calculating_exact(matrix, array, 2)
                print(self.output_y.text)
                self.output_except.text = ""
            except ValueError:
                self.output_except.text = "Введите все значения корректно"
        if self.n == 2:
            try:
                matrix = [[float(self._101_input.text), float(self._201_input.text)],
                          [float(self._501_input.text), float(self._601_input.text)]]
                array = [float(self._401_input.text), float(self._801_input.text)]
                self.output_x.text = 'x = ' + calculating_exact(matrix, array, 0)
                print(matrix)
                self.output_y.text = 'y = ' + calculating_exact(matrix, array, 1)
                # self.output_z.text = calculating_exact(matrix, array, 2)
                self.output_except.text = ""
            except ValueError:
                self.output_except.text = "Введите все значения корректно"
        if self.n == 4:
            try:
                matrix = [[float(self._111_input.text), float(self._21_input.text),
                           float(self._31_input.text), float(self._41_input.text)],
                          [float(self._61_input.text), float(self._71_input.text),
                           float(self._81_input.text), float(self._91_input.text)],
                          [float(self._1101_input.text), float(self._1201_input.text),
                           float(self._1301_input.text), float(self._1401_input.text)],
                          [float(self._1601_input.text), float(self._1701_input.text),
                           float(self._1801_input.text), float(self._1901_input.text)], ]
                array = [float(self._51_input.text), float(self._1001_input.text), float(self._1501_input.text),
                         float(self._2001_input.text)]
                self.output_x.text = 'x = ' + calculating_exact(matrix, array, 0)
                print(matrix)
                self.output_y.text = 'y = ' + calculating_exact(matrix, array, 1)
                self.output_z.text = 'z = ' + calculating_exact(matrix, array, 2)
                self.output_w.text = 'w = ' + calculating_exact(matrix, array, 3)
                print(self.output_y.text)
                self.output_except.text = ""
            except ValueError:
                self.output_except.text = "Введите все значения корректно"

    def plus_change_number_of_equations(self):
        if self.n > 3:
            pass
        else:
            array = [self._1_input, self._2_input, self._3_input,
                     self._4_input, self._5_input, self._6_input,
                     self._7_input, self._8_input, self._9_input,
                     self._10_input, self._11_input, self._12_input,
                     self._101_input, self._201_input, self._401_input,
                     self._501_input, self._601_input, self._801_input, self._111_input, self._21_input, self._31_input,
                     self._41_input, self._51_input, self._61_input,
                     self._71_input, self._81_input, self._91_input,
                     self._1001_input, self._1101_input, self._1201_input,
                     self._1301_input, self._1401_input, self._1501_input,
                     self._1601_input, self._1701_input, self._1801_input, self._1901_input, self._2001_input]
            for i in array:
                i.text = ''
            self.output_except.text = ""
            self.output_x.text = 'x = ?'
            self.output_y.text = 'y = ?'
            self.output_z.text = 'z = ?'
            self.output_w.text = 'w = ?'
            self.n += 1
            self._4_eq_layout.pos_hint = {'center_x': self._4_eq_layout.pos_hint['center_x'],
                                          'center_y': self._4_eq_layout.pos_hint['center_y'] + 1}
            self._3_eq_layout.pos_hint = {'center_x': self._3_eq_layout.pos_hint['center_x'],
                                          'center_y': self._3_eq_layout.pos_hint['center_y'] + 1}
            self._2_eq_layout.pos_hint = {'center_x': self._2_eq_layout.pos_hint['center_x'],
                                          'center_y': self._2_eq_layout.pos_hint['center_y'] + 1}
            self.eq_numb.text = f'Уравнений: {self.n}'
        print(self.n)
        if self.n == 2:
            self.output_w.pos_hint = {'center_x': 1.5, 'center_y': 0.05}
            self.output_z.pos_hint = {'center_x': 1.5, 'center_y': 0.1}
        if self.n == 3:
            self.output_w.pos_hint = {'center_x': 1.5, 'center_y': 0.05}
            self.output_z.pos_hint = {'center_x': 0.5, 'center_y': 0.1}
        if self.n == 4:
            self.output_w.pos_hint = {'center_x': 0.5, 'center_y': 0.05}
            self.output_z.pos_hint = {'center_x': 0.5, 'center_y': 0.1}

    def minus_number_of_equations(self):
        if self.n < 3:
            pass
        else:
            array = [self._1_input, self._2_input, self._3_input,
                     self._4_input, self._5_input, self._6_input,
                     self._7_input, self._8_input, self._9_input,
                     self._10_input, self._11_input, self._12_input]
            for i in array:
                i.text = ''
            self.output_except.text = ""
            self.output_x.text = 'x = ?'
            self.output_y.text = 'y = ?'
            self.output_z.text = 'z = ?'
            self.output_w.text = 'w = ?'
            self.n -= 1
            self._4_eq_layout.pos_hint = {'center_x': self._4_eq_layout.pos_hint['center_x'],
                                          'center_y': self._4_eq_layout.pos_hint['center_y'] - 1}
            self._3_eq_layout.pos_hint = {'center_x': self._3_eq_layout.pos_hint['center_x'],
                                          'center_y': self._3_eq_layout.pos_hint['center_y'] - 1}
            self._2_eq_layout.pos_hint = {'center_x': self._2_eq_layout.pos_hint['center_x'],
                                          'center_y': self._2_eq_layout.pos_hint['center_y'] - 1}
            self.eq_numb.text = f'Уравнений: {self.n}'
        if self.n == 2:
            self.output_w.pos_hint = {'center_x': 1.5, 'center_y': 0.05}
            self.output_z.pos_hint = {'center_x': 1.5, 'center_y': 0.1}
        if self.n == 3:
            self.output_w.pos_hint = {'center_x': 1.5, 'center_y': 0.05}
            self.output_z.pos_hint = {'center_x': 0.5, 'center_y': 0.1}
        if self.n == 4:
            self.output_w.pos_hint = {'center_x': 0.5, 'center_y': 0.05}
            self.output_z.pos_hint = {'center_x': 0.5, 'center_y': 0.1}


class ApproximateSolutionScreen(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.n = 3

    def change_text(self):
        if self.n == 3:
            try:
                matrix = [[float(self._13_input.text), float(self._14_input.text), float(self._15_input.text)],
                          [float(self._17_input.text), float(self._18_input.text), float(self._19_input.text)],
                          [float(self._211_input.text), float(self._22_input.text), float(self._23_input.text)]]
                array = [float(self._16_input.text), float(self._20_input.text), float(self._24_input.text)]
                x0 = float(self._33_input.text)
                y0 = float(self._34_input.text)
                z0 = float(self._35_input.text)
                eps = float(self._44_input.text)
                if eps <= 0 or eps >= 1:
                    self.output_except.text = "Точность должна быть положительным дробным числом меньше 1"
                else:
                    answer = equation(matrix, array, [x0, y0, z0], eps)
                    print(answer)
                    if '±' not in answer[0]:
                        self.output_x1.text = 'x = ' + str(answer[0])
                        self.output_y1.text = 'y = ' + str(answer[1])
                        self.output_z1.text = 'z = ' + str(answer[2])
                        self.output_except.text = ""
                    else:
                        self.output_x1.text = str(answer[0])
                        self.output_y1.text = str(answer[1])
                        self.output_z1.text = str(answer[2])
                        self.output_except.text = ""
            except ValueError:
                self.output_except.text = "Введите все значения корректно"
        if self.n == 2:
            try:
                matrix = [[float(self._113_input.text), float(self._114_input.text)],
                          [float(self._117_input.text), float(self._118_input.text)]]
                array = [float(self._115_input.text), float(self._119_input.text)]
                x0 = float(self._33_input.text)
                y0 = float(self._34_input.text)
                eps = float(self._44_input.text)
                if eps <= 0 or eps >= 1:
                    self.output_except.text = "Точность должна быть положительным дробным числом меньше 1"
                else:
                    answer = equation(matrix, array, [x0, y0], eps)
                    print(answer)
                    if '±' not in answer[0]:
                        self.output_x1.text = 'x = ' + str(answer[0])
                        self.output_y1.text = 'y = ' + str(answer[1])
                        self.output_except.text = ""
                    else:
                        self.output_x1.text = str(answer[0])
                        self.output_y1.text = str(answer[1])
                        self.output_except.text = ""
            except ValueError:
                self.output_except.text = "Введите все значения корректно"
        if self.n == 4:
            try:
                matrix = [[float(self._1013_input.text), float(self._1014_input.text), float(self._1015_input.text),
                           float(self._1016_input.text)],
                          [float(self._1018_input.text), float(self._1019_input.text), float(self._1020_input.text),
                           float(self._1021_input.text)],
                          [float(self._1023_input.text), float(self._1024_input.text), float(self._1025_input.text),
                           float(self._1026_input.text)],
                          [float(self._1028_input.text), float(self._1029_input.text), float(self._1030_input.text),
                           float(self._1031_input.text)]]
                array = [float(self._1017_input.text), float(self._1022_input.text), float(self._1027_input.text),
                         float(self._1032_input.text)]
                x0 = float(self._33_input.text)
                y0 = float(self._34_input.text)
                z0 = float(self._35_input.text)
                w0 = float(self._36_input.text)
                eps = float(self._44_input.text)
                if eps <= 0 or eps >= 1:
                    self.output_except.text = "Точность должна быть положительным дробным числом меньше 1"
                else:
                    answer = equation(matrix, array, [x0, y0, z0, w0], eps)
                    print(answer)
                    if '±' not in answer[0]:
                        self.output_x1.text = 'x = ' + str(answer[0])
                        self.output_y1.text = 'y = ' + str(answer[1])
                        self.output_z1.text = 'z = ' + str(answer[2])
                        self.output_w1.text = 'w = ' + str(answer[3])
                        self.output_except.text = ""
                    else:
                        self.output_x1.text = str(answer[0])
                        self.output_y1.text = str(answer[1])
                        self.output_z1.text = str(answer[2])
                        self.output_w1.text = str(answer[3])
                        self.output_except.text = ""
            except ValueError:
                self.output_except.text = "Введите все значения корректно"

    def plus_change_number_of_equations(self):
        if self.n > 3:
            pass
        else:
            array = [self._13_input, self._14_input, self._15_input,
                     self._16_input, self._17_input, self._18_input,
                     self._19_input, self._20_input, self._211_input,
                     self._22_input, self._23_input, self._24_input,
                     self._33_input, self._34_input, self._35_input, self._36_input,
                     self._44_input, self._1013_input, self._1014_input, self._1015_input,
                     self._1016_input, self._1017_input, self._1018_input, self._1019_input, self._1020_input,
                     self._1021_input, self._1022_input, self._1023_input,self._1024_input, self._1025_input,
                     self._1026_input, self._1027_input,self._1028_input, self._1029_input, self._1030_input,
                     self._1031_input, self._1032_input, self._113_input, self._114_input, self._115_input,
                     self._117_input, self._118_input, self._119_input]

            # , self._601_input, self._801_input, self._111_input, self._21_input, self._31_input,
            # self._41_input, self._51_input, self._61_input,
            # self._71_input, self._81_input, self._91_input,
            # self._1001_input, self._1101_input, self._1201_input,
            # self._1301_input, self._1401_input, self._1501_input,
            # self._1601_input, self._1701_input, self._1801_input, self._1901_input, self._2001_input
            for i in array:
                i.text = ''
            self.output_except.text = ""
            self.output_x1.text = 'x = ?'
            self.output_y1.text = 'y = ?'
            self.output_z1.text = 'z = ?'
            self.output_w1.text = 'w = ?'
            self.n += 1
            self._4_eq_layout.pos_hint = {'center_x': self._4_eq_layout.pos_hint['center_x'],
                                          'center_y': self._4_eq_layout.pos_hint['center_y'] + 1}
            self._3_eq_layout.pos_hint = {'center_x': self._3_eq_layout.pos_hint['center_x'],
                                          'center_y': self._3_eq_layout.pos_hint['center_y'] + 1}
            self._2_eq_layout.pos_hint = {'center_x': self._2_eq_layout.pos_hint['center_x'],
                                          'center_y': self._2_eq_layout.pos_hint['center_y'] + 1}
            self.eq_numb.text = f'Уравнений: {self.n}'
        print(self.n)
        if self.n == 3:
            self.output_w1.pos_hint = {'center_x': 1.5, 'center_y': 1.05}
            self.output_z1.pos_hint = {'center_x': 0.5, 'center_y': 0.1}
            self.w_label.pos_hint = {'center_x': 0.73, 'center_y': 1.69}
            self.z_label.pos_hint = {'center_x': 0.6, 'center_y': 0.69}
            self._36_input.pos_hint = {'center_x': 0.68, 'center_y': 1.69}
            self._35_input.pos_hint = {'center_x': 0.55, 'center_y': 0.69}
        if self.n == 4:
            self.output_w1.pos_hint = {'center_x': 0.5, 'center_y': 0.05}
            self.output_z1.pos_hint = {'center_x': 0.5, 'center_y': 0.1}
            self.w_label.pos_hint = {'center_x': 0.73, 'center_y': 0.69}
            self.z_label.pos_hint = {'center_x': 0.6, 'center_y': 0.69}
            self._36_input.pos_hint = {'center_x': 0.68, 'center_y': 0.69}
            self._35_input.pos_hint = {'center_x': 0.55, 'center_y': 0.69}

    def minus_number_of_equations(self):
        self._33_input.text, self._34_input.text, self._35_input.text = '', '', ''
        if self.n < 3:
            pass
        else:
            self.output_except.text = ""
            self.output_x1.text = 'x = ?'
            self.output_y1.text = 'y = ?'
            self.output_z1.text = 'z = ?'
            self.output_w1.text = 'w = ?'
            self.n -= 1
            self._4_eq_layout.pos_hint = {'center_x': self._4_eq_layout.pos_hint['center_x'],
                                          'center_y': self._4_eq_layout.pos_hint['center_y'] - 1}
            self._3_eq_layout.pos_hint = {'center_x': self._3_eq_layout.pos_hint['center_x'],
                                          'center_y': self._3_eq_layout.pos_hint['center_y'] - 1}
            self._2_eq_layout.pos_hint = {'center_x': self._2_eq_layout.pos_hint['center_x'],
                                          'center_y': self._2_eq_layout.pos_hint['center_y'] - 1}
            self.eq_numb.text = f'Уравнений: {self.n}'
        if self.n == 2:
            self.output_w1.pos_hint = {'center_x': 1.5, 'center_y': 0.05}
            self.output_z1.pos_hint = {'center_x': 1.5, 'center_y': 0.1}
            self.w_label.pos_hint = {'center_x': 0.73, 'center_y': 1.69}
            self.z_label.pos_hint = {'center_x': 0.6, 'center_y': 1.69}
            self._36_input.pos_hint = {'center_x': 0.68, 'center_y': 1.69}
            self._35_input.pos_hint = {'center_x': 0.68, 'center_y': 1.69}
        if self.n == 3:
            self.output_w1.pos_hint = {'center_x': 1.5, 'center_y': 0.05}
            self.output_z1.pos_hint = {'center_x': 0.5, 'center_y': 0.1}
            self.w_label.pos_hint = {'center_x': 0.73, 'center_y': 1.69}
            self.z_label.pos_hint = {'center_x': 0.6, 'center_y': 0.69}
            self._36_input.pos_hint = {'center_x': 0.68, 'center_y': 1.69}
            self._35_input.pos_hint = {'center_x': 0.55, 'center_y': 0.69}


class DemoApp(MDApp):
    def __init__(self):
        super().__init__()
        self.sm = ScreenManager()
        self.sm.add_widget(MenuScreen(name='menu'))

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


DemoApp().run()
