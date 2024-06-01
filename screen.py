screen_helper = """
ScreenManager:
    MenuScreen:
    ExactSolutionScreen:
    ApproximateSolutionScreen:

<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Нахождение точных значений корней системы линейных уравнений'
        pos_hint: {'center_x':0.5, 'center_y':0.55}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'exact'
    MDRectangleFlatButton:
        text: 'Нахождение приближенных значений корней системы линейных уравнений'
        pos_hint: {'center_x':0.5, 'center_y':0.45}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'approximate'

<ExactSolutionScreen>:
    eq_numb: number_of_eq
    
    _4_eq_layout: _4_eq

    _3_eq_layout: _3_eq
    
    _2_eq_layout: _2_eq
    
    _1_input: _1_k

    _2_input: _2_k

    _3_input: _3_k

    _4_input: _4_k

    _5_input: _5_k

    _6_input: _6_k

    _7_input: _7_k

    _8_input: _8_k

    _9_input: _9_k

    _10_input: _10_k

    _11_input: _11_k

    _12_input: _12_k
    
    _101_input: _101_k

    _201_input: _201_k

    _401_input: _401_k

    _501_input: _501_k

    _601_input: _601_k

    _801_input: _801_k
    
    _111_input: _111_k

    _21_input: _21_k

    _31_input: _31_k

    _41_input: _41_k

    _51_input: _51_k
    
    _61_input: _61_k

    _71_input: _71_k

    _81_input: _81_k

    _91_input: _91_k

    _1001_input: _1001_k
    
    _1101_input: _1101_k

    _1201_input: _1201_k

    _1301_input: _1301_k

    _1401_input: _1401_k

    _1501_input: _1501_k
    
    _1601_input: _1601_k

    _1701_input: _1701_k

    _1801_input: _1801_k

    _1901_input: _1901_k

    _2001_input: _2001_k

    output_except: except_text

    output_x: x_number

    output_y: y_number

    output_z: z_number
    
    output_w: w_number

    name: 'exact'

    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5, 'center_y':0.9}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'menu'
    
    MDLabel:
        id: number_of_eq
        text: 'Уравнений: 3'
        halign: 'center'
        pos_hint: {'center_x':0.1, 'center_y':0.43}
    
    MDRectangleFlatButton:
        text: '+'
        pos_hint: {'center_x':0.1, 'center_y':0.33}
        on_release:
            root.plus_change_number_of_equations()
            
    MDRectangleFlatButton:
        text: '-'
        pos_hint: {'center_x':0.2, 'center_y':0.33}
        on_release:
            root.minus_number_of_equations()

    MDRectangleFlatButton:
        text: 'Вычислить корни'
        pos_hint: {'center_x':0.5, 'center_y':0.33}
        on_release: root.change_text()

    MDLabel:
        text: 'Калькулятор'
        halign: 'center'
        pos_hint: {'center_x':0.5, 'center_y':0.8}
        
    MDGridLayout:
        id: _3_eq
        cols: 7
        rows: 3
        size_hint: (0.6, 0.15)
        padding: 10
        spacing: 10
        pos_hint: {'center_x':0.5, 'center_y':0.55}


        TextInput:
            id: _1_k
            multiline: False
        MDLabel:
            text: 'x   +'
            halign: 'center'
            pos_hint: {'center_x':0.34, 'center_y':0.55}
        TextInput:
            id: _2_k
            pos_hint: {'center_x':0.42, 'center_y':0.55}
            multiline: False
        MDLabel:
            text: 'y   +'
            halign: 'center'
            pos_hint: {'center_x':0.47, 'center_y':0.55}
        TextInput:
            id: _3_k
            pos_hint: {'center_x':0.55, 'center_y':0.55}
            multiline: False
        MDLabel:
            text: 'z   ='
            halign: 'center'
            pos_hint: {'center_x':0.6, 'center_y':0.55}
        TextInput:
            id: _4_k
            pos_hint: {'center_x':0.69, 'center_y':0.55}
            multiline: False
        TextInput:
            id: _5_k
            pos_hint: {'center_x':0.29, 'center_y':0.5}
            multiline: False
        MDLabel:
            text: 'x   +'
            halign: 'center'
            pos_hint: {'center_x':0.34, 'center_y':0.5}
        TextInput:
            id: _6_k
            pos_hint: {'center_x':0.42, 'center_y':0.5}
            multiline: False
        MDLabel:
            text: 'y   +'
            halign: 'center'
            pos_hint: {'center_x':0.47, 'center_y':0.5}
        TextInput:
            id: _7_k
            pos_hint: {'center_x':0.55, 'center_y':0.5}
            multiline: False
        MDLabel:
            text: 'z   ='
            halign: 'center'
            pos_hint: {'center_x':0.6, 'center_y':0.5}
        TextInput:
            id: _8_k
            pos_hint: {'center_x':0.69, 'center_y':0.5}
            multiline: False
        TextInput:
            id: _9_k
            pos_hint: {'center_x':0.29, 'center_y':0.45}
            multiline: False
        MDLabel:
            text: 'x   +'
            halign: 'center'
            pos_hint: {'center_x':0.34, 'center_y':0.45}
        TextInput:
            id: _10_k
            pos_hint: {'center_x':0.42, 'center_y':0.45}
            multiline: False
        MDLabel:
            text: 'y   +'
            halign: 'center'
            pos_hint: {'center_x':0.47, 'center_y':0.45}
        TextInput:
            id: _11_k
            pos_hint: {'center_x':0.55, 'center_y':0.45}
            multiline: False
        MDLabel:
            text: 'z   ='
            halign: 'center'
            pos_hint: {'center_x':0.6, 'center_y':0.45}
        TextInput:
            id: _12_k
            pos_hint: {'center_x':0.69, 'center_y':0.45}
            multiline: False
            
    MDGridLayout:
        id: _2_eq
        cols: 5
        rows: 2
        size_hint: (0.48, 0.11)
        padding: 10
        spacing: 10
        pos_hint: {'center_x':0.5, 'center_y':1.55}


        TextInput:
            id: _101_k
            multiline: False
        MDLabel:
            text: 'x   +'
            halign: 'center'
            pos_hint: {'center_x':0.34, 'center_y':0.55}
        TextInput:
            id: _201_k
            pos_hint: {'center_x':0.42, 'center_y':0.55}
            multiline: False
        MDLabel:
            text: 'y   ='
            halign: 'center'
            pos_hint: {'center_x':0.47, 'center_y':0.55}
        TextInput:
            id: _401_k
            pos_hint: {'center_x':0.69, 'center_y':0.55}
            multiline: False
        TextInput:
            id: _501_k
            pos_hint: {'center_x':0.29, 'center_y':0.5}
            multiline: False
        MDLabel:
            text: 'x   +'
            halign: 'center'
            pos_hint: {'center_x':0.34, 'center_y':0.5}
        TextInput:
            id: _601_k
            pos_hint: {'center_x':0.42, 'center_y':0.5}
            multiline: False
        MDLabel:
            text: 'y   ='
            halign: 'center'
            pos_hint: {'center_x':0.47, 'center_y':0.5}
        TextInput:
            id: _801_k
            pos_hint: {'center_x':0.69, 'center_y':0.5}
            multiline: False    
    
    MDGridLayout:
        id: _4_eq
        cols: 9
        rows: 4
        size_hint: (0.7, 0.2)
        padding: 10
        spacing: 10
        pos_hint: {'center_x': 0.5, 'center_y': -0.45}


        TextInput:
            id: _111_k
            multiline: False
        MDLabel:
            text: 'x   +'
            halign: 'center'
            pos_hint: {'center_x':0.34, 'center_y':0.55}
        TextInput:
            id: _21_k
            pos_hint: {'center_x':0.42, 'center_y':0.55}
            multiline: False
        MDLabel:
            text: 'y   +'
            halign: 'center'
            pos_hint: {'center_x':0.47, 'center_y':0.55}
        TextInput:
            id: _31_k
            pos_hint: {'center_x':0.55, 'center_y':0.55}
            multiline: False
        MDLabel:
            text: 'z   +'
            halign: 'center'
            pos_hint: {'center_x':0.6, 'center_y':0.55}
        TextInput:
            id: _41_k
            pos_hint: {'center_x':0.55, 'center_y':0.55}
            multiline: False
        MDLabel:
            text: 'w   ='
            halign: 'center'
            pos_hint: {'center_x':0.6, 'center_y':0.55}
        TextInput:
            id: _51_k
            pos_hint: {'center_x':0.69, 'center_y':0.55}
            multiline: False
        TextInput:
            id: _61_k
            pos_hint: {'center_x':0.29, 'center_y':0.5}
            multiline: False
        MDLabel:
            text: 'x   +'
            halign: 'center'
            pos_hint: {'center_x':0.34, 'center_y':0.5}
        TextInput:
            id: _71_k
            pos_hint: {'center_x':0.42, 'center_y':0.5}
            multiline: False
        MDLabel:
            text: 'y   +'
            halign: 'center'
            pos_hint: {'center_x':0.47, 'center_y':0.5}
        TextInput:
            id: _81_k
            pos_hint: {'center_x':0.55, 'center_y':0.5}
            multiline: False
        MDLabel:
            text: 'z   +'
            halign: 'center'
            pos_hint: {'center_x':0.6, 'center_y':0.5}
        TextInput:
            id: _91_k
            pos_hint: {'center_x':0.55, 'center_y':0.55}
            multiline: False
        MDLabel:
            text: 'w   ='
            halign: 'center'
            pos_hint: {'center_x':0.6, 'center_y':0.55}
        TextInput:
            id: _1001_k
            pos_hint: {'center_x':0.69, 'center_y':0.5}
            multiline: False
        TextInput:
            id: _1101_k
            pos_hint: {'center_x':0.29, 'center_y':0.45}
            multiline: False
        MDLabel:
            text: 'x   +'
            halign: 'center'
            pos_hint: {'center_x':0.34, 'center_y':0.45}
        TextInput:
            id: _1201_k
            pos_hint: {'center_x':0.42, 'center_y':0.45}
            multiline: False
        MDLabel:
            text: 'y   +'
            halign: 'center'
            pos_hint: {'center_x':0.47, 'center_y':0.45}
        TextInput:
            id: _1301_k
            pos_hint: {'center_x':0.55, 'center_y':0.45}
            multiline: False
        MDLabel:
            text: 'z   +'
            halign: 'center'
            pos_hint: {'center_x':0.6, 'center_y':0.45}
        TextInput:
            id: _1401_k
            pos_hint: {'center_x':0.55, 'center_y':0.55}
            multiline: False
        MDLabel:
            text: 'w   ='
            halign: 'center'
            pos_hint: {'center_x':0.6, 'center_y':0.55}
        TextInput:
            id: _1501_k
            pos_hint: {'center_x':0.69, 'center_y':0.45}
            multiline: False
        TextInput:
            id: _1601_k
            pos_hint: {'center_x':0.69, 'center_y':0.5}
            multiline: False   
        MDLabel:
            text: 'x   +'
            halign: 'center'
            pos_hint: {'center_x':0.34, 'center_y':0.45}
        TextInput:
            id: _1701_k
            pos_hint: {'center_x':0.42, 'center_y':0.45}
            multiline: False
        MDLabel:
            text: 'y   +'
            halign: 'center'
            pos_hint: {'center_x':0.47, 'center_y':0.45}
        TextInput:
            id: _1801_k
            pos_hint: {'center_x':0.55, 'center_y':0.45}
            multiline: False
        MDLabel:
            text: 'z   +'
            halign: 'center'
            pos_hint: {'center_x':0.6, 'center_y':0.45}
        TextInput:
            id: _1901_k
            pos_hint: {'center_x':0.55, 'center_y':0.55}
            multiline: False
        MDLabel:
            text: 'w   ='
            halign: 'center'
            pos_hint: {'center_x':0.6, 'center_y':0.55}
        TextInput:
            id: _2001_k
            pos_hint: {'center_x':0.69, 'center_y':0.45}
            multiline: False
    
    MDLabel:
        id: except_text
        text: ''
        halign: 'center'
        pos_hint: {'center_x':0.5, 'center_y':0.25}
    MDLabel:
        id: x_number
        text: 'x = ?'
        halign: 'center'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
    MDLabel:
        id: y_number
        text: 'y = ?'
        halign: 'center'
        pos_hint: {'center_x':0.5, 'center_y':0.15}
    MDLabel:
        id: z_number
        text: 'z = ?'
        halign: 'center'
        pos_hint: {'center_x':0.5, 'center_y':0.1}
    MDLabel:
        id: w_number
        text: 'w = ?'
        halign: 'center'
        pos_hint: {'center_x':1.5, 'center_y':0.05}

<ApproximateSolutionScreen>:
    eq_numb: number_of_eq

    _13_input: _13_k

    _14_input: _14_k

    _15_input: _15_k

    _16_input: _16_k

    _17_input: _17_k

    _18_input: _18_k

    _19_input: _19_k

    _20_input: _20_k

    _211_input: _211_k

    _22_input: _22_k

    _23_input: _23_k

    _24_input: _24_k

    _33_input: _33_k

    _34_input: _34_k

    _35_input: _35_k
    
    _36_input: _36_k

    _44_input: _44_k
    
    _113_input: _113_k

    _114_input: _114_k

    _115_input: _115_k

    _117_input: _117_k

    _118_input: _118_k

    _119_input: _119_k
    
    _1013_input: _1013_k

    _1014_input: _1014_k

    _1015_input: _1015_k

    _1016_input: _1016_k

    _1017_input: _1017_k

    _1018_input: _1018_k

    _1019_input: _1019_k

    _1020_input: _1020_k

    _1021_input: _1021_k

    _1022_input: _1022_k

    _1023_input: _1023_k

    _1024_input: _1024_k

    _1025_input: _1025_k

    _1026_input: _1026_k

    _1027_input: _1027_k
    
    _1028_input: _1028_k

    _1029_input: _1029_k
    
    _1030_input: _1030_k

    _1031_input: _1031_k

    _1032_input: _1032_k
    
    z_label: z1_label
    
    w_label: w1_label

    output_except: except_text

    output_x1: x1_number

    output_y1: y1_number

    output_z1: z1_number
    
    output_w1: w1_number
    
    _4_eq_layout:_4_eq
    
    _3_eq_layout: _3_eq
    
    _2_eq_layout: _2_eq

    name: 'approximate'

    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5, 'center_y':0.9}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'menu'

    MDRectangleFlatButton:
        text: 'Вычислить корни'
        pos_hint: {'center_x':0.5, 'center_y':0.33}
        on_release: root.change_text()
        
    MDLabel:
        id: number_of_eq
        text: 'Уравнений: 3'
        halign: 'center'
        pos_hint: {'center_x':0.1, 'center_y':0.43}
    
    MDRectangleFlatButton:
        text: '+'
        pos_hint: {'center_x':0.1, 'center_y':0.33}
        on_release:
            root.plus_change_number_of_equations()
            
    MDRectangleFlatButton:
        text: '-'
        pos_hint: {'center_x':0.2, 'center_y':0.33}
        on_release:
            root.minus_number_of_equations()

    MDLabel:
        text: 'Калькулятор'
        halign: 'center'
        pos_hint: {'center_x':0.5, 'center_y':0.83}
    MDLabel:
        text: 'Первые приближения'
        halign: 'center'
        pos_hint: {'center_x':0.5, 'center_y':0.77}

    MDLabel:
        text: 'x'
        halign: 'center'
        pos_hint: {'center_x':0.34, 'center_y':0.69}
    TextInput:
        id: _33_k
        pos_hint: {'center_x':0.29, 'center_y':0.69}
        size_hint: (0.06, 0.04)
        multiline: False
    TextInput:
        id: _34_k
        pos_hint: {'center_x':0.42, 'center_y':0.69}
        size_hint: (0.06, 0.04)
        multiline: False
    MDLabel:
        text: 'y'
        halign: 'center'
        pos_hint: {'center_x':0.47, 'center_y':0.69}
    TextInput:
        id: _35_k
        pos_hint: {'center_x':0.55, 'center_y':0.69}
        size_hint: (0.06, 0.04)
        multiline: False
    MDLabel:
        id: z1_label
        text: 'z'
        halign: 'center'
        pos_hint: {'center_x':0.6, 'center_y':0.69}    
    MDLabel:
        id: w1_label
        text: 'w'
        halign: 'center'
        pos_hint: {'center_x':0.73, 'center_y':1.69}
    TextInput:
        id: _36_k
        pos_hint: {'center_x':0.68, 'center_y':1.69}
        size_hint: (0.06, 0.04)
        multiline: False

    MDGridLayout:
        id: _2_eq
        cols: 5
        rows: 2
        size_hint: (0.48, 0.11)
        padding: 10
        spacing: 10
        pos_hint: {'center_x':0.5, 'center_y':1.55}

        TextInput:
            id: _113_k
            pos_hint: {'center_x':0.29, 'center_y':0.55}
            multiline: False
            
        MDLabel:
            text: 'x   +'
            halign: 'center'
            pos_hint: {'center_x':0.34, 'center_y':0.55}
            
        TextInput:
            id: _114_k
            pos_hint: {'center_x':0.42, 'center_y':0.55}
            multiline: False
            
        MDLabel:
            text: 'y   ='
            halign: 'center'
            pos_hint: {'center_x':0.47, 'center_y':0.55}
            
        TextInput:
            id: _115_k
            pos_hint: {'center_x':0.55, 'center_y':0.55}
            multiline: False
    
        TextInput:
            id: _117_k
            pos_hint: {'center_x':0.29, 'center_y':0.5}
            multiline: False
            
        MDLabel:
            text: 'x   +'
            halign: 'center'
            pos_hint: {'center_x':0.34, 'center_y':0.5}
            
        TextInput:
            id: _118_k
            pos_hint: {'center_x':0.42, 'center_y':0.5}
            multiline: False
            
        MDLabel:
            text: 'y   ='
            halign: 'center'
            pos_hint: {'center_x':0.47, 'center_y':0.5}
            
        TextInput:
            id: _119_k
            pos_hint: {'center_x':0.55, 'center_y':0.5}
            multiline: False

    MDGridLayout:
        id: _3_eq
        cols: 7
        rows: 3
        size_hint: (0.6, 0.15)
        padding: 10
        spacing: 10
        pos_hint: {'center_x':0.5, 'center_y':0.55}

        TextInput:
            id: _13_k
            pos_hint: {'center_x':0.29, 'center_y':0.55}
            multiline: False
            
        MDLabel:
            text: 'x   +'
            halign: 'center'
            pos_hint: {'center_x':0.34, 'center_y':0.55}
            
        TextInput:
            id: _14_k
            pos_hint: {'center_x':0.42, 'center_y':0.55}
            multiline: False
            
        MDLabel:
            text: 'y   +'
            halign: 'center'
            pos_hint: {'center_x':0.47, 'center_y':0.55}
            
        TextInput:
            id: _15_k
            pos_hint: {'center_x':0.55, 'center_y':0.55}
            multiline: False
        MDLabel:
            text: 'z   ='
            halign: 'center'
            pos_hint: {'center_x':0.6, 'center_y':0.55}
            
        TextInput:
            id: _16_k
            pos_hint: {'center_x':0.69, 'center_y':0.55}
            multiline: False
    
        TextInput:
            id: _17_k
            pos_hint: {'center_x':0.29, 'center_y':0.5}
            multiline: False
            
        MDLabel:
            text: 'x   +'
            halign: 'center'
            pos_hint: {'center_x':0.34, 'center_y':0.5}
            
        TextInput:
            id: _18_k
            pos_hint: {'center_x':0.42, 'center_y':0.5}
            multiline: False
            
        MDLabel:
            text: 'y   +'
            halign: 'center'
            pos_hint: {'center_x':0.47, 'center_y':0.5}
            
        TextInput:
            id: _19_k
            pos_hint: {'center_x':0.55, 'center_y':0.5}
            multiline: False
            
        MDLabel:
            text: 'z   ='
            halign: 'center'
            pos_hint: {'center_x':0.6, 'center_y':0.5}
            
        TextInput:
            id: _20_k
            pos_hint: {'center_x':0.69, 'center_y':0.5}
            multiline: False
    
        TextInput:
            id: _211_k
            pos_hint: {'center_x':0.29, 'center_y':0.45}
            multiline: False
        MDLabel:
            text: 'x   +'
            halign: 'center'
            pos_hint: {'center_x':0.34, 'center_y':0.45}
        TextInput:
            id: _22_k
            pos_hint: {'center_x':0.42, 'center_y':0.45}
            multiline: False
        MDLabel:
            text: 'y   +'
            halign: 'center'
            pos_hint: {'center_x':0.47, 'center_y':0.45}
        TextInput:
            id: _23_k
            pos_hint: {'center_x':0.55, 'center_y':0.45}
            multiline: False
        MDLabel:
            text: 'z   ='
            halign: 'center'
            pos_hint: {'center_x':0.6, 'center_y':0.45}
        TextInput:
            id: _24_k
            pos_hint: {'center_x':0.69, 'center_y':0.45}
            multiline: False
            
    MDGridLayout:
        id: _4_eq
        cols: 9
        rows: 4
        size_hint: (0.7, 0.2)
        padding: 10
        spacing: 10
        pos_hint: {'center_x':0.5, 'center_y': -0.45}

        TextInput:
            id: _1013_k
            pos_hint: {'center_x':0.29, 'center_y':0.55}
            multiline: False
            
        MDLabel:
            text: 'x   +'
            halign: 'center'
            pos_hint: {'center_x':0.34, 'center_y':0.55}
            
        TextInput:
            id: _1014_k
            pos_hint: {'center_x':0.42, 'center_y':0.55}
            multiline: False
            
        MDLabel:
            text: 'y   +'
            halign: 'center'
            pos_hint: {'center_x':0.47, 'center_y':0.55}
            
        TextInput:
            id: _1015_k
            pos_hint: {'center_x':0.55, 'center_y':0.55}
            multiline: False
            
        MDLabel:
            text: 'z   +'
            halign: 'center'
            pos_hint: {'center_x':0.6, 'center_y':0.55}
            
        TextInput:
            id: _1016_k
            pos_hint: {'center_x':0.69, 'center_y':0.55}
            multiline: False
            
        MDLabel:
            text: 'w   ='
            halign: 'center'
            pos_hint: {'center_x':0.6, 'center_y':0.55}
            
        TextInput:
            id: _1017_k
            pos_hint: {'center_x':0.69, 'center_y':0.55}
            multiline: False
    
        TextInput:
            id: _1018_k
            pos_hint: {'center_x':0.29, 'center_y':0.5}
            multiline: False
            
        MDLabel:
            text: 'x   +'
            halign: 'center'
            pos_hint: {'center_x':0.34, 'center_y':0.5}
            
        TextInput:
            id: _1019_k
            pos_hint: {'center_x':0.42, 'center_y':0.5}
            multiline: False
            
        MDLabel:
            text: 'y   +'
            halign: 'center'
            pos_hint: {'center_x':0.47, 'center_y':0.5}
            
        TextInput:
            id: _1020_k
            pos_hint: {'center_x':0.55, 'center_y':0.5}
            multiline: False
            
        MDLabel:
            text: 'z   +'
            halign: 'center'
            pos_hint: {'center_x':0.6, 'center_y':0.5}
            
        TextInput:
            id: _1021_k
            pos_hint: {'center_x':0.69, 'center_y':0.5}
            multiline: False
            
        MDLabel:
            text: 'w   ='
            halign: 'center'
            pos_hint: {'center_x':0.6, 'center_y':0.5}
            
        TextInput:
            id: _1022_k
            pos_hint: {'center_x':0.69, 'center_y':0.5}
            multiline: False
    
        TextInput:
            id: _1023_k
            pos_hint: {'center_x':0.29, 'center_y':0.45}
            multiline: False
        MDLabel:
            text: 'x   +'
            halign: 'center'
            pos_hint: {'center_x':0.34, 'center_y':0.45}
        TextInput:
            id: _1024_k
            pos_hint: {'center_x':0.42, 'center_y':0.45}
            multiline: False
        MDLabel:
            text: 'y   +'
            halign: 'center'
            pos_hint: {'center_x':0.47, 'center_y':0.45}
        TextInput:
            id: _1025_k
            pos_hint: {'center_x':0.55, 'center_y':0.45}
            multiline: False
        MDLabel:
            text: 'z   +'
            halign: 'center'
            pos_hint: {'center_x':0.6, 'center_y':0.45}
        TextInput:
            id: _1026_k
            pos_hint: {'center_x':0.69, 'center_y':0.45}
            multiline: False        
        MDLabel:
            text: 'w   ='
            halign: 'center'
            pos_hint: {'center_x':0.6, 'center_y':0.45}
        TextInput:
            id: _1027_k
            pos_hint: {'center_x':0.69, 'center_y':0.45}
            multiline: False     
        TextInput:
            id: _1028_k
            pos_hint: {'center_x':0.29, 'center_y':0.45}
            multiline: False
        MDLabel:
            text: 'x   +'
            halign: 'center'
            pos_hint: {'center_x':0.34, 'center_y':0.45}
        TextInput:
            id: _1029_k
            pos_hint: {'center_x':0.42, 'center_y':0.45}
            multiline: False
        MDLabel:
            text: 'y   +'
            halign: 'center'
            pos_hint: {'center_x':0.47, 'center_y':0.45}
        TextInput:
            id: _1030_k
            pos_hint: {'center_x':0.55, 'center_y':0.45}
            multiline: False
        MDLabel:
            text: 'z   +'
            halign: 'center'
            pos_hint: {'center_x':0.6, 'center_y':0.45}
        TextInput:
            id: _1031_k
            pos_hint: {'center_x':0.69, 'center_y':0.45}
            multiline: False        
        MDLabel:
            text: 'w   ='
            halign: 'center'
            pos_hint: {'center_x':0.6, 'center_y':0.45}
        TextInput:
            id: _1032_k
            pos_hint: {'center_x':0.69, 'center_y':0.45}
            multiline: False  
            
    MDLabel:
        text: 'Точность'
        halign: 'center'
        pos_hint: {'center_x':0.53, 'center_y':0.4}
    TextInput:
        id: _44_k
        pos_hint: {'center_x':0.69, 'center_y':0.4}
        size_hint: (0.06, 0.04)
        multiline: False
    MDLabel:
        id: except_text
        text: ''
        halign: 'center'
        pos_hint: {'center_x':0.5, 'center_y':0.25}
    MDLabel:
        id: x1_number
        text: 'x = ?'
        halign: 'center'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
    MDLabel:
        id: y1_number
        text: 'y = ?'
        halign: 'center'
        pos_hint: {'center_x':0.5, 'center_y':0.15}
    MDLabel:
        id: z1_number
        text: 'z = ?'
        halign: 'center'
        pos_hint: {'center_x':0.5, 'center_y':0.1}
    MDLabel:
        id: w1_number
        text: 'w = ?'
        halign: 'center'
        pos_hint: {'center_x':0.5, 'center_y':1.05}
"""