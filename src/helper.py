helper_string = '''
BoxLayout:
    orientation:'vertical'
    MDToolbar:
        id: label
        md_bg_color: [0.5294117647,0.50588235294,0.74117647058,1]
    FloatLayout:
        id : floatlayout
        orientation:'vertical'
        MDCard:
            size_hint: None, None
            size: "400dp", "400dp"
            halign:"center"
            radius: 20
            pos_hint: {"center_x": .5, "center_y": .5}
            FitImage:
                id:img
                size_hint: [.9, .9]
                pos_hint: {"center_x": .5, "center_y": .5}
                          
'''
