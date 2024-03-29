import flet as ft

def main(page: ft.Page):
    alerta = ft.AlertDialog(
        title= ft.Text(value='Aviso'),
        content= ft.Text(value= 'Quer deletar os dados da Sessão?'),
        content_padding= ft.padding.all(30),
        inset_padding= ft.padding.all(10),
        modal=False,
        shape= ft.RoundedRectangleBorder(radius=5),
        on_dismiss= lambda _: print('Fechou'),

        actions=[
            ft.TextButton(text='Cancelar', style=ft.ButtonStyle(color=ft.colors.RED)),
            ft.ElevatedButton(text='Salvar', style=ft.ButtonStyle(bgcolor=ft.colors.GREEN, color=ft.colors.WHITE))
        ],
      actions_alignment=ft.MainAxisAlignment.END,
    )

    def abrir_dialogo(e):
        page.dialog = alerta
        alerta.open = True
        page.update()

    btn1 = ft.ElevatedButton(text='Abrir', on_click=abrir_dialogo)

    page.add(btn1)

    page.dialog = alerta
    alerta.open = True
    page.update()

if __name__ == '__main__':
    ft.app(target=main)