# Projeto Chat

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

    def enviar_mensagem_tunel(info):
        chat.controls.append(flet.Text(info))
        pagina.update()
    
    # Cria tunel na rede entre dois ou mais usuários que estejam conectadas ao mesmo tempo no sistema.
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    pagina.add(texto)
    
    def enviar_mensagem(evento):
        texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value}"
        

        pagina.pubsub.send_all(texto_campo_mensagem)
        campo_mensagem.value = ""

        pagina.update()


    chat = flet.Column()
    campo_mensagem = flet.TextField(label="Escreva sua mensagem aqui") 
    botao_enviar = flet.ElevatedButton("Enviar", on_click=enviar_mensagem)


    def entrar_chat(evento):
        popup.open=False
        
        linha_mensagem = flet.Row(
            [campo_mensagem, botao_enviar]
        )
        
        pagina.remove(botao_iniciar)
        pagina.add(chat)
        pagina.add(linha_mensagem)
        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)
        
        pagina.update()
        
        
        # Criar campo eviar mensage
        # criar botão enviar mensagem
    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()


    popup = flet.AlertDialog(
        open=False,
        modal=True,
        title=flet.Text("Bem Vindo ao HashZap"),
        content=nome_usuario,
        actions=[flet.ElevatedButton("Entrar", on_click=entrar_chat)]
        )


    botao_iniciar = flet.ElevatedButton("Iniciar Chat", on_click=iniciar_chat)
    pagina.add(botao_iniciar)

flet.app(main, view=flet.WEB_BROWSER)
