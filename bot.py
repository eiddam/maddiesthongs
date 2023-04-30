import discord
import asyncio
import datetime

intents = discord.Intents.default()
intents.members = True
intents.messages = True

client = discord.Client(intents=intents)
token = 'MTA3OTQ5NTY4MzQzNTkzNzg0Mg.Gwy_sH.CNb_T9Fb9krv7aLqF8CUKWM8DRUhgBzx9faYw0'
role_id = 1042430786277744772
channel_id = 1070661587540639814

async def send_scheduled_message(channel, message, date_time):
    await asyncio.sleep((date_time - datetime.datetime.now()).total_seconds())
    await channel.send(message)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    channel = client.get_channel(channel_id)
    
    # Schedule messages with mentions of a specific role
    role = channel.guild.get_role(role_id)
    
    # Mensagem 1 
    date_time = datetime.datetime(2023, 5, 1, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia Internacional dos Trabalhadores*, por isso a {role.mention} é: **Qual era o teu emprego de sonho quando eras mais novo? E agora?**'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 2 
    date_time = datetime.datetime(2023, 5, 2, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia Mundial do Atum*, por isso a {role.mention} é: **Qual é o teu animal aquático favorito? Já o comeste?**'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 3 
    date_time = datetime.datetime(2023, 5, 3, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia Internacional do Sol *, por isso a {role.mention} é: **Se te oferecessem agora umas férias gostavas de ir para onde?**'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 4 
    date_time = datetime.datetime(2023, 5, 4, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia Internacional do Bombeiro*, por isso a {role.mention} é: **Já fingiste estar doente para não fazeres alguma coisa? Ou para faltares à escola ou ao trabalho?**'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 5 
    date_time = datetime.datetime(2023, 5, 5, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia Mundial da Língua Portuguesa*, por isso a {role.mention} é: **Se tivesses de inventar uma nova palavra qual seria e que significado teria? E qual foi o maior pontapé na gramática que deste ou viste alguém dar?**'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 6 
    date_time = datetime.datetime(2023, 5, 6, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia da Coragem*, por isso a {role.mention} é: **Gostas de aceitar desafios? Se sim conta-nos um segredo ou alguma coisa que ainda não tenhas contado a nínguem! Se não, conta-nos um segredo ou rumor que ouviste e que te deixou chocado!**'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 7 
    date_time = datetime.datetime(2023, 5, 7, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia do Silêncio*, por isso a {role.mention} é: **O que é que gostas de fazer sozinho? E, depois de um dia barulhento o que é que fazes para desanuviar?**'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 8 
    date_time = datetime.datetime(2023, 5, 8, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia da Vitória*, por isso a {role.mention} é: **Qual é o teu jogo favorito? E qual é o jogo em que achas que és mesmo bom jogador e conseguias derrotar todo o pessoal aqui no soshi?**'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 9 
    date_time = datetime.datetime(2023, 5, 9, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia da Europa*, por isso a {role.mention} é: **Se te oferecessem uma viagem grátis já no próximo fim-de-semana para qualquer país europeu, ias para qual? E quem do soshi levavas contigo?**'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 10 
    date_time = datetime.datetime(2023, 5, 10, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia de Limpar o Teu Quarto*, por isso a {role.mention} é: **Costumas ter o quarto arrumado ou nem por isso? E também tens aquela cadeira especial onde vai parar toda a roupa que não queres arrumar? Confessa!**'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 11 
    date_time = datetime.datetime(2023, 5, 11, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia do Reggae*, por isso a {role.mention} é: **Qual é o teu género musical favorito? E que música recomendas a toda a gente aqui no soshi?**'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 12 
    date_time = datetime.datetime(2023, 5, 12, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia Internacional do Enfermeiro*, por isso a {role.mention} é: **Quais pensas que são os maiores desafios que os profissionais de saúde enfrentam e o que poderia ser feito para facilitar o seu trabalho?**'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 13 
    date_time = datetime.datetime(2023, 5, 13, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia Mundial do Cocktail*, por isso a {role.mention} é: **Qual é a tua bebida alcoólica favorita? E és bom a prepará-la?**'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 14 
    date_time = datetime.datetime(2023, 5, 14, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia da Bicicleta*, por isso a {role.mention} é: **Sabes andar de bicicleta? Se sim, preferes andar no campo ou pela cidade? E se não, ainda pensas em aprender?**'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 15 
    date_time = datetime.datetime(2023, 5, 15, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia Internacional da Família*, por isso a {role.mention} é: **Qual é a tua atividade favorita de fazer em família? E consideras animais de estimação família? Se sim, fala nos dos teus!**'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 16
    date_time = datetime.datetime(2023, 5, 16, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia Internacional da Luz*, por isso a {role.mention} é: **Gostas mais da noite ou do dia? És das pessoas que gosta de acordar cedo ou preferes ficar na cama mais tempo?**'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 17 
    date_time = datetime.datetime(2023, 5, 17, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia Mundial da Internet*, por isso a {role.mention} é: **Onde passas mais tempo enquanto navegas a internet e como é reages quando estás com o bom lag? **'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 18 
    date_time = datetime.datetime(2023, 5, 18, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia Internacional dos Museus*, por isso a {role.mention} é: **Em Portugal são muitos os museus que são gratuitos aos fins de semana, então para que fique registrado, quais são os teus museus favoritos dos que já visitastes e quais gostarias de conhecer? **'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 19 
    date_time = datetime.datetime(2023, 5, 19, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia Mundial da Doação de Leite Humano*, por isso a {role.mention} é: **O leite humano é essencial para o crescimento e imunização das crianças, mas infelizmente nem todas têm acesso. Qual é a tua relação com o leite e que outros elementos achas essenciais para o bom desenvolvimento das crianças?**'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 20 
    date_time = datetime.datetime(2023, 5, 20, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia Europeu do Mar*, por isso a {role.mention} é: **Tens algum desporto aquático que praticas ou gostavas de experimentar? E qual é a tua praia favorita?**'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 21 
    date_time = datetime.datetime(2023, 5, 21, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia Internacional do Chá*, por isso a {role.mention} é: **Boas amantes de chá, sejam eles calmantes ou estimulantes, nada bate um bom cházinho, de quais  gostas mais e conheces os efeitos curativos que possam ter? **'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 22 
    date_time = datetime.datetime(2023, 5, 22, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia Internacional da Diversidade Biológica*, por isso a {role.mention} é: **Foram feitas novas pesquisas relativas aos testes em animais e criou-se uma célula em chip capaz de produzir resultados com margens de erro infeiriores aos destes testes controversos. Como achas que as novas tecnologias podem ajudar-nos a chegar a uma produção cientifica mais ética. **'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 23 
    date_time = datetime.datetime(2023, 5, 23, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia Mundial da Tartaruga*, por isso a {role.mention} é: **Já tiveste algum animal pouco convencional? As tartarugas têm um sentido de orientação incrivel conseguindo sempre voltar ao local de nascimento para desovar, conheces outro facto interessante sobre um animal?**'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 24 
    date_time = datetime.datetime(2023, 5, 24, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia Europeu dos Parques Naturais*, por isso a {role.mention} é: **Qual é o teu espaço verde favorito e como te sentes rodeado pela natureza?**'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 25 
    date_time = datetime.datetime(2023, 5, 25, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia de África*, por isso a {role.mention} é: **Que país africano mais gostarias de visitar e conheces alguma história ou conhecimento que gostarias de parilhar? **'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 26 
    date_time = datetime.datetime(2023, 5, 26, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia da Espiga*, por isso a {role.mention} é: **Gostas de fazer caminhadas? Se sim por onde é que gostas de andar? Tipo preferes uma aventura no meio de uma floresta ou um passeio calmo numa praia?**'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 27 
    date_time = datetime.datetime(2023, 5, 27, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia Mundial dos Vizinhos*, por isso a {role.mention} é: **Dás-te bem com os teus vizinhos ou nem por isso? E, como estamos no discord, qual é um server vizinho onde gostes de passar o tempo?**'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 28 
    date_time = datetime.datetime(2023, 5, 28, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia Internacional do Hambúrguer*, por isso a {role.mention} é: **Qual é o teu restaurante favorito para comer hambugueres? E o que é que costumas pedir? Qual é o menu que escolhes no clássico McDonalds ou Burguer King?**'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 29 
    date_time = datetime.datetime(2023, 5, 29, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia Internacional da Lontra*, por isso a {role.mention} é: **Qual é o teu meme, vine ou tiktok favorito? Ou o que não te saiu da cabeça durante bué tempo?**'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 30 
    date_time = datetime.datetime(2023, 5, 30, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia da Decoração*, por isso a {role.mention} é: **Preferias viver num castelo no campo, num apartamento no meio da cidade, numa mansão futuristica, num refúgio no meio de uma floresta ou numa cabana à beira mar? Se já tiveres planos para a tua futura casa manda fotos!**'
    await send_scheduled_message(channel, message, date_time)
    # Mensagem 31 
    date_time = datetime.datetime(2023, 5, 31, 12, 0)
    message = f'Bom tarde! Hoje é a *Dia do Sorriso*, por isso a {role.mention} é: **O que é que fazes para fazer alguém sorrir? E um desafio agora: Escreve alguma coisa no chat para fazer um arrombado aqui do soshi sorrir!**'
    await send_scheduled_message(channel, message, date_time)

try:
    client.run(token)
except RuntimeError as e:
    print(f'Caught a RuntimeError: {e}')


