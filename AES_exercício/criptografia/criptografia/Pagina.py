import flet as ft
from .Encriptador import encripta_arquivo
from .Decriptador import decriptador
from .gerar_metadata import gerar_metadata
from .verificar_integridade import verificar_integridade
import os

def criarPagina(iv):
    def main(page: ft.Page):
        page.title = "Encriptador"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        selected_files_text = ft.Text("Nenhum arquivo selecionado", size=16)

        campo_chave = ft.TextField(label="Digite a chave de 16 bytes", hint_text="Ex: Olá mundo!", password=True)


        dialog_sucess = ft.AlertDialog(
            title=ft.Text("Sucesso!"),
            content=ft.Text("Ação realizada com sucesso."),
            actions=[ft.TextButton("OK", on_click=lambda e: page.close(dialog_sucess))],
        )

        dialog_insucesso = ft.AlertDialog(
            title=ft.Text("Erro!"),
            content=ft.Text("Algo deu errado. Verifique a chave e tente novamente."),
            actions=[ft.TextButton("OK", on_click=lambda e: page.close(dialog_insucesso))],
        )

        dialog_verificacao = ft.AlertDialog(
            title=ft.Text("Resultado da Verificação"),
            content=ft.Text(),  # Será preenchido dinamicamente
            actions=[ft.TextButton("OK", on_click=lambda e: page.close(dialog_verificacao))],
        )

        # Resultado da seleção de arquivos
        selected_path = {"path": None}

        def on_dialog_result(e: ft.FilePickerResultEvent):
            if e.files:
                file_names = ", ".join([f.name for f in e.files])
                selected_files_text.value = f"Arquivos selecionados: {file_names}"
                selected_path["path"] = e.files
            else:
                selected_files_text.value = "Nenhum arquivo selecionado"
                selected_path["path"] = None
            selected_files_text.update()

        file_picker = ft.FilePicker(on_result=on_dialog_result)
        page.overlay.append(file_picker)

        # Botões
        def botao_encripta(e):
            
            print("Lozao")
            print(selected_path, "selecte")
            
            print(os.path.abspath(selected_path["path"][0].name), "nome")

            try:
                caminho_arquivo = selected_path["path"][0].path
            except:
                caminho_arquivo = ""

            try:
                if not caminho_arquivo:
                    raise ValueError("Nenhum arquivo selecionado.")
                chave = campo_chave.value.encode("utf-8")
                enc_file = encripta_arquivo(caminho_arquivo, chave, iv)
                dialog_sucess.content = ft.Text(f"Ação realizada com sucesso. Arquivo criado em: ${os.path.abspath(enc_file)}")

                page.open(dialog_sucess)

            except Exception as ex:
                print("Erro:", ex)
                page.open(dialog_insucesso)

        def botao_decripta(e):

            try:
                caminho_arquivo = selected_path["path"][0].path
            except:
                caminho_arquivo = ""

            try:
                chave = campo_chave.value.encode("utf-8")
                
                decrip_file = decriptador(chave, caminho_arquivo)
            
                dialog_sucess.content = ft.Text(f"Ação realizada com sucesso. Arquivo criado em: ${os.path.abspath(decrip_file)}")
                

                page.open(dialog_sucess)

            except Exception as ex:
                print("Erro:", ex)

                page.open(dialog_insucesso)

        def botao_criar_token(e):

            try:
                caminho_arquivo = selected_path["path"][0].path
            except:
                caminho_arquivo = ""

            try:
                if not selected_path["path"]:
                    raise ValueError("Nenhum arquivo selecionado.")

                chave = campo_chave.value.encode("utf-8")
                meta_file = gerar_metadata(caminho_arquivo, chave)


                dialog_sucess.content = ft.Text(f"Ação realizada com sucesso. Arquivo criado em: ${os.path.abspath(meta_file)}")

                page.open(dialog_sucess)

            except Exception as ex:
                print("Erro:", ex)
                page.open(dialog_insucesso)

        def botao_verificar_veracidade(e):

            try:
                caminho_arquivo = selected_path["path"][0].path
                caminho_meta = selected_path["path"][1].path
            except:
                caminho_arquivo = ""
                caminho_meta = ""


            try:
                if not caminho_arquivo or not caminho_meta:
                    raise ValueError("Nenhum arquivo selecionado.")

                chave = campo_chave.value.encode("utf-8")

                resultado = verificar_integridade(caminho_arquivo, caminho_meta, chave)

                if resultado:
                    dialog_verificacao.content = ft.Text("O arquivo está íntegro e não foi modificado.")
                else:
                    dialog_verificacao.content = ft.Text("ATENÇÃO: O arquivo foi modificado ou está corrompido!")

                page.open(dialog_verificacao)

            except Exception as ex:
                print("Erro:", ex)
                dialog_insucesso.content = ft.Text(f"Erro na verificação: {str(ex)}")
                page.open(dialog_insucesso)
        page.add(
            campo_chave,
            ft.ElevatedButton("Escolher para decriptar, encriptar, gerar meta, ou verificar", on_click=lambda _: file_picker.pick_files(allow_multiple=True)),
            selected_files_text,
            ft.ElevatedButton("Encriptar", on_click=botao_encripta),
            ft.ElevatedButton("Decriptar", on_click=botao_decripta),
            ft.ElevatedButton("Criar Token", on_click=botao_criar_token),
            ft.ElevatedButton("Verificar Veracidade", on_click=botao_verificar_veracidade),
        )

    print("Rodando ft.app com Flet em: http://0.0.0.0:8550")
    ft.app(target=main, view=ft.WEB_BROWSER, port=8550, host="0.0.0.0")

