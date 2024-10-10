from flet import (
    flet, 
    UserControl, 
    Page, 
    Column, 
    Row, 
    Container, 
    Text, 
    padding, 
    alignment,
    LinearGradient,
    IconButton,
    icons,
    GridView,
    transform,
    animation,
    )

class Expense(UserControl):

    def hover_animation(self, e):
        if e.data=='true':
            e.control.content.controls[2].offset = transform.Offset(0,0)
            e.control.content.controls[2].opacity = 1
            e.control.update()
        else:
            e.control.content.controls[2].offset = transform.Offset(0,1)
            e.control.content.controls[2].opacity = 0
            e.control.update()


    def change_icon(self, e):
        if e.control.selected != True:
            e.control.selected = True
            e.control.icon_color = 'white'
            e.control.update()
        else:
            e.control.selected = False
            e.control.icon_color = 'white54'
            e.control.update()


    def icon(self, name, color, selected):
        return IconButton(
            icon=name,
            icon_color=color,
            icon_size=18,
            selected=selected,
            on_click=lambda e: self.change_icon(e),
        )
    

    def MainContainer(self):
        self.main = Container(
            width=290, 
            height=600, 
            bgcolor='black', 
            border_radius=35, 
            padding=8,
        )

        self.main_col = Column()

        self.green_container = Container(
            width=self.main.width,
            height=self.main.height * 0.45,
            gradient=LinearGradient(
                begin=alignment.top_left,
                end=alignment.bottom_right,
                colors=[
                    "#0f766e",
                    "#064e3b",
                ],
            ),
            border_radius=30,
        )


        self.notification = self.icon(icons.NOTIFICATIONS, 'white54', True)
        self.hide = self.icon(icons.HIDE_SOURCE, 'white54', False)
        self.chat = self.icon(icons.CHAT_ROUNDED, 'white54', False)


        self.icon_column = Column(
            alignment="center",
            spacing=5,
            controls=[
                self.notification,
                self.hide,
                self.chat,
            ],
        )


        self.inner_green_container = Container(
            width=self.green_container.width,
            height=self.green_container.height,
            content=Row(
                spacing=0,
                controls=[
                    Column(
                        expand=4,
                        controls=[
                            Container(
                                padding=20,
                                expand=True,
                                content=Row(
                                    controls=[
                                        Column(
                                            controls=[
                                                Text(
                                                    "WELCOME BACK",
                                                    size=10,
                                                    color='white70',
                                                ),
                                                Text(
                                                    "Mayank",
                                                    size=18,
                                                    weight="bold",
                                                ),
                                                Container(
                                                    padding = padding.only(
                                                        top=35,
                                                        bottom=35,
                                                    ),
                                                ),
                                                Text(
                                                    "TOTAL CURRENT BALANCE",
                                                    size=10,
                                                    color='white70',
                                                ),
                                                Text(
                                                    "₹ 11,764.28",
                                                    size=18,
                                                    weight="bold",
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    Column(
                        expand=1,
                        controls=[
                            Container(
                                padding=padding.only(right=10),
                                expand=True,
                                content=Row(
                                    alignment="center",
                                    controls=[
                                        Column(
                                            alignment="center",
                                            horizontal_alignment="center",
                                            controls=[
                                                Column(
                                                    alignment="center",
                                                    horizontal_alignment="center",
                                                    controls=[
                                                        Container(
                                                            width=40,
                                                            height=150,
                                                            bgcolor='white10',
                                                            border_radius=14,
                                                            content=self.icon_column,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )


        self.grid_transfer = GridView(
            expand=True,
            max_extent=150,
            runs_count=0,
            spacing=12,
            run_spacing=5,
            horizontal=True,
        )


        self.grid_payments = GridView(
            expand=True,
            max_extent=150,
            runs_count=0,
            spacing=12,
            run_spacing=5,
        )


        self.main_content_area = Container(
            width=self.main.width,
            height=self.main.height * 0.50,
            # bgcolor='blue',
            padding = padding.only(top=10, left=10, right=10),
            content=Column(
                spacing=20,
                controls=[
                    Row(
                        controls=[
                            Container(
                                content=Text(
                                    "Recent Transfer",
                                    size=14,
                                    weight='bold',
                                ),
                            ),
                            Container(
                                content=Text(
                                    "view all",
                                    size=14,
                                    weight='w400',
                                    color='white54',
                                ),
                            ),
                        ],
                        alignment='spaceBetween',
                        vertical_alignment='end',
                    ),
                    Container(
                        height=50,
                        content=self.grid_transfer,
                    ),
                    Row(
                        controls=[
                            Container(
                                content=Text(
                                    "Pending Payments",
                                    size=14,
                                    weight='bold',
                                ),
                            ),
                            Container(
                                content=Text(
                                    "view all",
                                    size=14,
                                    weight='w400',
                                    color='white54',
                                ),
                            ),
                        ],
                        alignment='spaceBetween',
                        vertical_alignment='end',
                    ),
                    self.grid_payments,
                ],
            ),
        )



        info_list = ['PH', 'SD', 'WQ', 'KG', 'TY', 'SB', 'LP', 'LK']
        for i in info_list:
            __ = Container(
                width=100,
                height=100, 
                bgcolor='white10',
                border_radius=15,
                alignment=alignment.center,
                content=Text(f'{i}', weight='bold'),
            )
            self.grid_transfer.controls.append(__)


        payment_list = [
            ['Utilities', '₹ 523.23'],
            ['Phone Bills', '₹ 102.32'],
            ['Insurance', '₹ 128.51'],
            ['Gas', '₹ 45.65'],
            ['Groceries', '₹ 289.42'],
            ['Utilities', '₹ 77.82'],
        ]
        for i in payment_list:
            __ = Container(
                width=100,
                height=100, 
                bgcolor='white10',
                border_radius=15,
                alignment=alignment.center,
                content=Text(f'{i}', weight='bold'),
                on_hover= lambda e: self.hover_animation(e),
            )
            self.grid_payments.controls.append(__)
            for x in i:
                __.content = Column(
                    alignment='center',
                    horizontal_alignment='center',
                    controls=[
                        Text(
                            f'{i[0]}',
                            size=11,
                            color='white54',
                        ),
                        Text(
                            f'{i[1]}',
                            size=16,
                            weight='bold',
                        ),
                        Text(
                            'Pay Now?',
                            color='white60',
                            size=12,
                            text_align='start',
                            weight='w600',
                            offset=transform.Offset(0,1),
                            animate_offset=animation.Animation(
                                duration=900,
                                curve='decelerate',
                            ),
                            animate_opacity=300,
                            opacity=0,
                        ),
                    ],
                )


        self.green_container.content = self.inner_green_container

        #
        self.main_col.controls.append(self.green_container)
        self.main_col.controls.append(self.main_content_area)

        #
        self.main.content = self.main_col

        for icon in self.icon_column.controls[:]:
            if icon.selected == True:
                icon.icon_color = 'white'

        return self.main
    
    def build(self):
        return Column(
            controls=[
                self.MainContainer(),
            ],
        )

def start(page: Page):
    page.title="Flet Expense Concept"
    page.horizontal_alignment="center"
    page.vertical_alignment="center"

    app = Expense()
    page.add(app)
    page.update()


if __name__=="__main__":
    flet.app(target=start)
