import flet as ft
from Encriptador import encripta_arquivo
from Decriptador import decriptador

def criarPagina(iv):
    def main(page: ft.Page):
        page.title = "Flet File Picker com Texto Dinâmico"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        selected_files_text = ft.Text("Nenhum arquivo selecionado", size=16)

        campo_chave = ft.TextField(label="Digite a chave de 16 bytes", hint_text="Ex: Olá mundo!", password=True)

        # Diálogo de sucesso
        def fechar_dialogo_sucesso(e):
            dialog_sucess.open = False
            page.update()

        dialog_sucess = ft.AlertDialog(
            title=ft.Text("Sucesso!"),
            content=ft.Text("Ação realizada com sucesso."),
            actions=[ft.TextButton("OK", on_click=fechar_dialogo_sucesso)],
        )

        # Diálogo de erro
        def fechar_dialogo_insucesso(e):
            dialog_insucesso.open = False
            page.update()

        dialog_insucesso = ft.AlertDialog(
            title=ft.Text("Erro!"),
            content=ft.Text("Algo deu errado. Verifique a chave e tente novamente."),
            actions=[ft.TextButton("OK", on_click=fechar_dialogo_insucesso)],
        )

        # Resultado da seleção de arquivos
        selected_path = {"path": None}

        def on_dialog_result(e: ft.FilePickerResultEvent):
            if e.files:
                file_names = ", ".join([f.name for f in e.files])
                selected_files_text.value = f"Arquivos selecionados: {file_names}"
                selected_path["path"] = e.files[0].path
            else:
                selected_files_text.value = "Nenhum arquivo selecionado"
                selected_path["path"] = None
            selected_files_text.update()

        file_picker = ft.FilePicker(on_result=on_dialog_result)
        page.overlay.append(file_picker)

        # Botões
        def botao_encripta(e):
            try:
                if not selected_path["path"]:
                    raise ValueError("Nenhum arquivo selecionado.")
                chave = campo_chave.value.encode("utf-8")
                encripta_arquivo(selected_path["path"], chave, iv)
                dialog_sucess.open = True
                page.dialog = dialog_sucess
                page.update()
            except Exception as ex:
                print("Erro:", ex)
                dialog_insucesso.open = True
                page.dialog = dialog_insucesso
                page.update()

        def botao_decripta(e):
            try:
                chave = campo_chave.value.encode("utf-8")
                decriptador(chave, selected_path["path"])
                dialog_sucess.open = True
                page.dialog = dialog_sucess
                page.update()
            except Exception as ex:
                print("Erro:", ex)
                dialog_insucesso.open = True
                page.dialog = dialog_insucesso
                page.update()

        def botao_criar_token(e):
            print("Criar Token")

        def botao_verificar_veracidade(e):
            print("Verificar Veracidade")

        page.add(
            campo_chave,
            ft.ElevatedButton("Escolher arquivos...", on_click=lambda _: file_picker.pick_files(allow_multiple=False)),
            selected_files_text,
            ft.ElevatedButton("Encriptar", on_click=botao_encripta),
            ft.ElevatedButton("Decriptar", on_click=botao_decripta),
            ft.ElevatedButton("Criar Token", on_click=botao_criar_token),
            ft.ElevatedButton("Verificar Veracidade", on_click=botao_verificar_veracidade),
        )

    ft.app(target=main)
