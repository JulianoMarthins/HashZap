# FrontEnd -> Tudo que o usuário vê e interage
# BackEnd -> Código de programação com toda a lógica necessária para fazer o sistema funcionar


# Título da HashZap

# Botão de iniciar o chat
    # Popup
        # Bem vindo ao HashZap
        # Escreva seu nome
        # Entrar no chat
# Chat
    # Usuário entrou no site
    # Mensagens do usuário
# Campo para enviar mensagem
# Botão de enviar

import flet

def main(pagina):
    texto = flet.Text("HashZap")

    nome_usuario = flet.TextField(label="Escreva seu nome")

    popup = flet.AlertDialog(
        open=False,
        modal=True,
        title=flet.Text("Bem Vindo ao HashZap"),
        content=nome_usuario
        )

    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()


    botao_iniciar = flet.ElevatedButton("Iniciar Chat", on_click=iniciar_chat)
    
    pagina.add(texto)
    pagina.add(botao_iniciar)

flet.app(main)


# Htm*Comunidade I - Aula pausada em 56 minutos