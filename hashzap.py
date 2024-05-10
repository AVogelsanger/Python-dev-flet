# Título: Hashzap
# Botão de iniciar Chat
    # popup (Janela na frente da tela)
    # Título: Bem vindo ao Hashzap
    # campo de texto -> Escreva seu nome no input do chat
    # Botão: entrar no chat
        # remover com o título
        # remover o Btn iniciar
        # Fechar a janela (popup)
        # Carregar o chat
            # As mensagens que já foram enviadas
            # Campo digite a msg
            # Botão enviar

# Instale o flet - (pip install flet)
import flet as ft


# criar a função principal do app
def main(pagina):
    # criar todas as funcionalidades  

    # criar o elemento
    titulo = ft.Text('Hashzap')

    titulo_popup = ft.Text('Bem vindo ao Hashzap')
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat:")


    chat = ft.Column()

    def enviar_msg_tunel(mensagem):
        texto_chat = ft.Text(mensagem)
        chat.controls.append(texto_chat)
        pagina.update()

    pagina.pubsub.subscribe(enviar_msg_tunel)    

    def enviar_msg(evento):
        texto_msg = campo_msg.value
        nome_usuario = campo_nome_usuario.value
        mensagem = f"{nome_usuario} : {texto_msg}"
        pagina.pubsub.send_all(mensagem)
        campo_msg.value = ''
        pagina.update()
        

    campo_msg = ft.TextField(label='Digite sua mensagem')
    btn_envivar_msg = ft.ElevatedButton('Enviar', on_click=enviar_msg)

    
   
    linha_msg = ft.Row([campo_msg, btn_envivar_msg])
    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(btn_iniciar)
        popup.open = False
        pagina.add(chat)
        pagina.add(linha_msg)
        mensagem = f'{campo_nome_usuario.value} entrou no chat'
        pagina.pubsub.send_all(mensagem)
        pagina.update()

    btn_pop_entrar_chat = ft.ElevatedButton('Entrar no chat', on_click=entrar_chat)
    
    popup = ft.AlertDialog(
                        title=titulo_popup, 
                        content=campo_nome_usuario,
                        actions=[btn_pop_entrar_chat])

    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    btn_iniciar = ft.ElevatedButton('iniciar chat', on_click=iniciar_chat)

    

    # adicionar o elemento na página
    pagina.add(titulo)
    pagina.add(btn_iniciar)
    pagina.add(popup)

# rodar a aplicação
ft.app(main, view=ft.WEB_BROWSER)