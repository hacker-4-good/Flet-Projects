import flet
from flet import (
    Column,
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    UserControl,
    border_radius,
    colors,
)


class CalculatorApp(UserControl):
    def build(self):
        self.number1 = 0
        self.number2 = 0
        self.expression = ""
        self.result = Text(value="0", color=colors.WHITE, size=20)

        # application's root control (i.e. "view") containing all other controls
        return Container(
            width=300,
            bgcolor=colors.BLACK,
            border_radius=border_radius.all(20),
            padding=20,
            content=Column(
                controls=[
                    Row(controls=[self.result], alignment="end"),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="AC",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.InputAC,
                            ),
                            ElevatedButton(
                                text="+/-",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="%",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.Inputpercent,
                            ),
                            ElevatedButton(
                                text="/",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.Inputdivide,
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="7",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.Input7,
                            ),
                            ElevatedButton(
                                text="8",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.Input8,
                            ),
                            ElevatedButton(
                                text="9",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.Input9,
                            ),
                            ElevatedButton(
                                text="*",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.Inputmultiply,
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="4",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.Input4,
                            ),
                            ElevatedButton(
                                text="5",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.Input5,
                            ),
                            ElevatedButton(
                                text="6",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.Input6,
                            ),
                            ElevatedButton(
                                text="-",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.Inputminus,
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="1",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.Input1,
                            ),
                            ElevatedButton(
                                text="2",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.Input2,
                            ),
                            ElevatedButton(
                                text="3",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.Input3,
                            ),
                            ElevatedButton(
                                text="+",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.Inputadd,
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="0",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=2,
                                on_click=self.Input0,
                            ),
                            ElevatedButton(
                                text=".",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="=",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.Output,
                            ),
                        ]
                    ),
                ]
            ),
        )
    
    def InputAC(self,e):
        self.expression = ""
        self.result.value = self.expression
        self.number1 = 0
        self.number2 = 0
        self.update()
    def Inputpercent(self,e):
        self.expression += " % "
        self.result.value = self.expression
        self.update()
    def Inputdivide(self,e):
        self.expression += " / "
        self.result.value = self.expression
        self.update()

    def Input7(self,e):
        self.expression += "7"
        self.result.value = self.expression
        self.update()
    def Input8(self,e):
        self.expression += "8"
        self.result.value = self.expression
        self.update()
    def Input9(self,e):
        self.expression += "9"
        self.result.value = self.expression
        self.update()
    def Inputmultiply(self,e):
        self.expression += " * "
        self.result.value = self.expression
        self.update()

    def Input4(self,e):
        self.expression += "4"
        self.result.value = self.expression
        self.update()
    def Input5(self,e):
        self.expression += "5"
        self.result.value = self.expression
        self.update()
    def Input6(self,e):
        self.expression += "6"
        self.result.value = self.expression
        self.update()
    def Inputminus(self,e):
        self.expression += " - "
        self.result.value = self.expression
        self.update()

    def Input1(self,e):
        self.expression += "1"
        self.result.value = self.expression
        self.update()
    def Input2(self,e):
        self.expression += "2"
        self.result.value = self.expression
        self.update()
    def Input3(self,e):
        self.expression += "3"
        self.result.value = self.expression
        self.update()
    def Inputadd(self,e):
        self.expression += " + "
        self.result.value = self.expression
        self.update()
    
    def Input0(self,e):
        self.expression += "0"
        self.result.value = self.expression
        self.update()
    def Output(self,e):
        try:
            self.result.value = eval(self.expression)
            self.expression = str(self.result.value)
            self.update()
        except SyntaxError:
            self.result.value = "Error"
            self.update()
    

        

def main(page: Page):
    page.title = "Calc App"
    calc = CalculatorApp()
    page.add(calc)


flet.app(target=main)