helper_string = '''

BoxLayout:
    orientation:'vertical'
    MDToolbar:
        id: label
    FloatLayout:
        id : floatlayout
        orientation:'vertical'
        MDCard:
            size_hint: None, None
            size: "400dp", "400dp"
            halign:"center"
            pos_hint: {"center_x": .5, "center_y": .5}
            FitImage:
                id: img
        
                      
'''
