import turtle as t
import functools
import random
import math

LARGURA_JANELA = 1024
ALTURA_JANELA = 600
DEFAULT_TURTLE_SIZE = 40
DEFAULT_TURTLE_SCALE = 3
RAIO_JOGADOR = DEFAULT_TURTLE_SIZE / DEFAULT_TURTLE_SCALE
RAIO_BOLA = DEFAULT_TURTLE_SIZE / 2
PIXEIS_MOVIMENTO = 90/5
LADO_MAIOR_AREA = ALTURA_JANELA / 3
LADO_MENOR_AREA = 50
RAIO_MEIO_CAMPO = LADO_MAIOR_AREA / 4
START_POS_BALIZAS = ALTURA_JANELA / 4
BOLA_START_POS = (5, 5)
KeepItGoing = 1

# Funções responsáveis pelo movimento dos jogadores no ambiente. 
# O número de unidades que o jogador se pode movimentar é definida pela constante 
# PIXEIS_MOVIMENTO. As funções recebem um dicionário que contém o estado 
# do jogo e o jogador que se está a movimentar. 

def jogador_cima(estado_jogo, jogador):
    estado_jogo[jogador].pu()
    estado_jogo[jogador].goto(estado_jogo[jogador].xcor(), estado_jogo[jogador].ycor() + PIXEIS_MOVIMENTO)
    estado_jogo[jogador].pd()


def jogador_baixo(estado_jogo, jogador):
    estado_jogo[jogador].pu()
    estado_jogo[jogador].goto(estado_jogo[jogador].xcor(), estado_jogo[jogador].ycor() - PIXEIS_MOVIMENTO)
    estado_jogo[jogador].pd()


def jogador_direita(estado_jogo, jogador):
    estado_jogo[jogador].pu()
    estado_jogo[jogador].goto(estado_jogo[jogador].xcor() + PIXEIS_MOVIMENTO, estado_jogo[jogador].ycor())
    estado_jogo[jogador].pd()


def jogador_esquerda(estado_jogo, jogador):

    estado_jogo[jogador].pu()
    estado_jogo[jogador].goto(estado_jogo[jogador].xcor()-PIXEIS_MOVIMENTO, estado_jogo[jogador].ycor())
    estado_jogo[jogador].pd()


def desenha_linhas_campo():
    ''' Função responsável por desenhar as linhas do campo, 
    nomeadamente a linha de meio campo, o círculo central, e as balizas. '''

    t_linhas = t.Turtle()
    t_linhas.color("white")
    t_linhas.width(DEFAULT_TURTLE_SCALE)

    t_linhas.penup()
    t_linhas.goto(0, ALTURA_JANELA/2)
    t_linhas.pendown()
    t_linhas.right(90)
    t_linhas.fd(ALTURA_JANELA)

    t_linhas.penup()
    t_linhas.goto(0 - RAIO_MEIO_CAMPO, 0)
    t_linhas.pendown()
    t_linhas.circle(RAIO_MEIO_CAMPO)

    t_linhas.penup()
    t_linhas.goto(LARGURA_JANELA/2, ALTURA_JANELA/6)
    t_linhas.pendown()
    t_linhas.setheading(180)
    t_linhas.fd(LADO_MENOR_AREA)
    t_linhas.left(90)
    t_linhas.fd(LADO_MAIOR_AREA)
    t_linhas.left(90)
    t_linhas.fd(LADO_MENOR_AREA)

    t_linhas.penup()
    t_linhas.goto(-LARGURA_JANELA / 2, -ALTURA_JANELA / 6)
    t_linhas.pendown()
    t_linhas.setheading(0)
    t_linhas.fd(LADO_MENOR_AREA)
    t_linhas.left(90)
    t_linhas.fd(LADO_MAIOR_AREA)
    t_linhas.left(90)
    t_linhas.fd(LADO_MENOR_AREA)

    t_linhas.hideturtle()


def criar_bola():
    '''
    Função responsável pela criação da bola. 
    Deverá considerar que esta tem uma forma redonda, é de cor preta, 
    começa na posição BOLA_START_POS com uma direção aleatória. 
    Deverá ter em conta que a velocidade da bola deverá ser superior à dos jogadores. 
    A função deverá devolver um dicionário contendo 4 elementos: o objeto bola, 
    a sua direção no eixo dos xx, a sua direção no eixo dos yy, 
    e um elemento inicialmente a None que corresponde à posição anterior da mesma.
    '''
    bola = t.Turtle()
    bola.color("black")

    bola.penup()
    bola.goto(0, -RAIO_BOLA)
    bola.pendown()

    bola.begin_fill()
    bola.circle(RAIO_BOLA)
    bola.end_fill()

    bola.hideturtle()

    ANGULO = random.randint(0, 360)

    return bola, math.cos(math.radians(ANGULO)), math.sin(math.radians(ANGULO)), None


def cria_jogador(x_pos_inicial, y_pos_inicial, cor):
    ''' Função responsável por criar e devolver o objeto que corresponde a um jogador (um objecto Turtle). 
    A função recebe 3 argumentos que correspondem às coordenadas da posição inicial 
    em xx e yy, e a cor do jogador. A forma dos jogadores deverá ser um círculo, 
    cujo seu tamanho deverá ser definido através da função shapesize
    do módulo \texttt{turtle}, usando os seguintes parâmetros: 
    stretch_wid=DEFAULT_TURTLE_SCALE, stretch_len=DEFAULT_TURTLE_SCALE. '''

    jogador = t.Turtle()
    jogador.color(cor)
    jogador.shape("circle")
    jogador.shapesize(stretch_wid=DEFAULT_TURTLE_SCALE, stretch_len=DEFAULT_TURTLE_SCALE)

    jogador.pu()
    jogador.goto(x_pos_inicial, y_pos_inicial)
    jogador.pd()

    return jogador


def init_state():
    estado_jogo = {}
    estado_jogo['bola'] = None
    estado_jogo['jogador_vermelho'] = None
    estado_jogo['jogador_azul'] = None
    estado_jogo['var'] = {
        'bola' : [],
        'jogador_vermelho' : [],
        'jogador_azul' : [],
    }
    estado_jogo['pontuacao_jogador_vermelho'] = 0
    estado_jogo['pontuacao_jogador_azul'] = 0
    estado_jogo['KeepItGoing'] = 1
    return estado_jogo


def cria_janela():
    #create a window and declare a variable called window and call the screen()
    window=t.Screen()
    window.title("Foosball Game")
    window.bgcolor("green")
    window.setup(width = LARGURA_JANELA,height = ALTURA_JANELA)
    window.tracer(0)
    return window


def cria_quadro_resultados():
    #Code for creating pen for scorecard update
    quadro=t.Turtle()
    quadro.speed(0)
    quadro.color("Blue")
    quadro.penup()
    quadro.hideturtle()
    quadro.goto(0,260)
    quadro.write("Player A: 0\t\tPlayer B: 0 ", align="center", font=('Monaco',24,"normal"))
    return quadro


def terminar_jogo(estado_jogo):
    '''
     Função responsável por terminar o jogo. Nesta função, deverá atualizar o ficheiro 
     ''historico_resultados.csv'' com o número total de jogos até ao momento, 
     e o resultado final do jogo. Caso o ficheiro não exista, 
     ele deverá ser criado com o seguinte cabeçalho: 
     NJogo,JogadorVermelho,JogadorAzul.
    '''
    estado_jogo['KeepItGoing'] = 0


def setup(estado_jogo, jogar):
    janela = cria_janela()
    #Assign keys to play
    janela.listen()
    if jogar:
        janela.onkeypress(functools.partial(jogador_cima, estado_jogo, 'jogador_vermelho') ,'w')
        janela.onkeypress(functools.partial(jogador_baixo, estado_jogo, 'jogador_vermelho') ,'s')
        janela.onkeypress(functools.partial(jogador_esquerda, estado_jogo, 'jogador_vermelho') ,'a')
        janela.onkeypress(functools.partial(jogador_direita, estado_jogo, 'jogador_vermelho') ,'d')
        janela.onkeypress(functools.partial(jogador_cima, estado_jogo, 'jogador_azul') ,'Up')
        janela.onkeypress(functools.partial(jogador_baixo, estado_jogo, 'jogador_azul') ,'Down')
        janela.onkeypress(functools.partial(jogador_esquerda, estado_jogo, 'jogador_azul') ,'Left')
        janela.onkeypress(functools.partial(jogador_direita, estado_jogo, 'jogador_azul') ,'Right')
        janela.onkeypress(functools.partial(terminar_jogo, estado_jogo) ,'Escape')
        quadro = cria_quadro_resultados()
        estado_jogo['quadro'] = quadro
    desenha_linhas_campo()
    bola = criar_bola()
    jogador_vermelho = cria_jogador(-((ALTURA_JANELA / 2) + 10 * DEFAULT_TURTLE_SCALE), 0, "red")
    jogador_azul = cria_jogador(((ALTURA_JANELA / 2) + 10 * DEFAULT_TURTLE_SCALE), 0, "blue")
    estado_jogo['janela'] = janela
    estado_jogo['bola'] = bola
    estado_jogo['jogador_vermelho'] = jogador_vermelho
    estado_jogo['jogador_azul'] = jogador_azul


def update_board(estado_jogo):
    estado_jogo['quadro'].clear()
    estado_jogo['quadro'].write("Player A: {}\t\tPlayer B: {} ".format(estado_jogo['pontuacao_jogador_vermelho'], estado_jogo['pontuacao_jogador_azul']),align="center",font=('Monaco',24,"normal"))


def movimenta_bola(estado_jogo):
    '''
    Função responsável pelo movimento da bola que deverá ser feito tendo em conta a
    posição atual da bola e a direção em xx e yy.
    '''

    bola, x_dir, y_dir, past_pos = estado_jogo['bola']

    coords = bola.pos()
    new_x = coords[0] + x_dir * 0.5
    new_y = coords[1] + y_dir * 0.5

    bola.clear()

    bola.pu()
    bola.goto(new_x, new_y)
    bola.pd()

    bola.begin_fill()
    bola.circle(RAIO_BOLA)
    bola.end_fill()

    bola.hideturtle()

    estado_jogo['bola'] = [bola, x_dir, y_dir, coords]


def angle_things(pos_bola, past_pos):
    dx = pos_bola[0] - past_pos[0]
    dy = pos_bola[1] - past_pos[1]

    current_angle = math.degrees(math.atan2(dy, dx))

    return current_angle


def move(jogador, x, y):
    jogador.pu()
    jogador.goto(x, y)
    jogador.pd()


def verifica_jogador(jogador):

    jogador_pos = jogador.pos()
    x = jogador_pos[0]
    y = jogador_pos[1]

    if y + 10*DEFAULT_TURTLE_SCALE > ALTURA_JANELA/2:
        y = ALTURA_JANELA/2 - 10*DEFAULT_TURTLE_SCALE
        move(jogador, x, y)

    if y - 10*DEFAULT_TURTLE_SCALE < -ALTURA_JANELA/2:
        y = -ALTURA_JANELA / 2 + 10 * DEFAULT_TURTLE_SCALE
        move(jogador, x, y)

    if x + 10 * DEFAULT_TURTLE_SCALE > LARGURA_JANELA / 2:
        x = LARGURA_JANELA/2 - 10*DEFAULT_TURTLE_SCALE
        move(jogador, x, y)

    if x - 10*DEFAULT_TURTLE_SCALE < -LARGURA_JANELA/2:
        x = -LARGURA_JANELA/2 + 10*DEFAULT_TURTLE_SCALE
        move(jogador, x, y)


def verifica_colisoes_ambiente(estado_jogo):
    '''
    Função responsável por verificar se há colisões com os limites do ambiente, 
    atualizando a direção da bola. Não se esqueça de considerar que nas laterais, 
    fora da zona das balizas, a bola deverá inverter a direção onde atingiu o limite.
    '''

    # Cima 180 + angulo (dir->esq) // -angulo
    # Baixo 180 - angulo (dir->esq) // angulo
    # Esquerda

    verifica_jogador(estado_jogo['jogador_azul'])
    verifica_jogador(estado_jogo['jogador_vermelho'])

    bola, x_dir, y_dir, past_pos = estado_jogo['bola']
    pos_bola = bola.pos()

    if pos_bola[1] + RAIO_BOLA > ALTURA_JANELA/2:

        angle = angle_things(pos_bola, past_pos)

        if past_pos[0] > pos_bola[0]:
            angle = 180 - angle
            estado_jogo['bola'] = bola, math.cos(math.radians(180 + angle)), math.sin(math.radians(180 + angle)), pos_bola
        else:
            estado_jogo['bola'] = bola, math.cos(math.radians(-angle)), math.sin(math.radians(-angle)), pos_bola

    if pos_bola[1] - RAIO_BOLA < -ALTURA_JANELA/2:

        angle = angle_things(pos_bola, past_pos)

        if past_pos[0] > pos_bola[0]:
            estado_jogo['bola'] = bola, math.cos(math.radians(180 - (180 + angle))), math.sin(math.radians(180 - (180 + angle))), pos_bola
        else:
            estado_jogo['bola'] = bola, math.cos(math.radians(-angle)), math.sin(math.radians(-angle)), pos_bola

    if pos_bola[0] + RAIO_BOLA > LARGURA_JANELA / 2:

        angle = angle_things(pos_bola, past_pos)

        if past_pos[1] > pos_bola[1]:
            estado_jogo['bola'] = bola, math.cos(math.radians(180 - angle)), math.sin(math.radians(180 - angle)), pos_bola
        else:
            estado_jogo['bola'] = bola, math.cos(math.radians(180 - angle)), math.sin(math.radians(180-angle)), pos_bola

    if pos_bola[0] - RAIO_BOLA < -LARGURA_JANELA / 2:

        angle = angle_things(pos_bola, past_pos)

        if past_pos[1] > pos_bola[1]:
            estado_jogo['bola'] = bola, math.cos(math.radians(- (180 + angle))), math.sin(math.radians(- (180 + angle))), pos_bola
        else:
            estado_jogo['bola'] = bola, math.cos(math.radians(- (180 + angle))), math.sin(math.radians(- (180 + angle))), pos_bola


def verifica_golo_jogador_vermelho(estado_jogo):
    '''
    Função responsável por verificar se um determinado jogador marcou golo. 
    Para fazer esta verificação poderá fazer uso das constantes: 
    LADO_MAIOR_AREA e 
    START_POS_BALIZAS. 
    Note que sempre que há um golo, deverá atualizar a pontuação do jogador, 
    criar um ficheiro que permita fazer a análise da jogada pelo VAR, 
    e reiniciar o jogo com a bola ao centro. 
    O ficheiro para o VAR deverá conter todas as informações necessárias 
    para repetir a jogada, usando as informações disponíveis no objeto 
    estado_jogo['var']. O ficheiro deverá ter o nome 
    
    replay_golo_jv_[TotalGolosJogadorVermelho]_ja_[TotalGolosJogadorAzul].txt 
    
    onde [TotalGolosJogadorVermelho], [TotalGolosJogadorAzul] 
    deverão ser substituídos pelo número de golos marcados pelo jogador vermelho 
    e azul, respectivamente. Este ficheiro deverá conter 3 linhas, estruturadas 
    da seguinte forma:
    Linha 1 - coordenadas da bola;
    Linha 2 - coordenadas do jogador vermelho;
    Linha 3 - coordenadas do jogador azul;
    
    Em cada linha, os valores de xx e yy das coordenadas são separados por uma 
    ',', e cada coordenada é separada por um ';'.
    '''
    bola, x_dir, y_dir, last = estado_jogo['bola']
    pos_bola = bola.pos()

    if pos_bola[0] >= LARGURA_JANELA / 2 - RAIO_BOLA:
        if START_POS_BALIZAS / 2 - RAIO_BOLA > pos_bola[1] > -START_POS_BALIZAS / 2 + RAIO_BOLA:
            estado_jogo['pontuacao_jogador_vermelho'] += 1
            bola.clear()
            update_board(estado_jogo)
            estado_jogo['bola'] = criar_bola()
            Escreve_ficheiro(estado_jogo['var'], estado_jogo['pontuacao_jogador_azul'], estado_jogo['pontuacao_jogador_vermelho'])


def verifica_golo_jogador_azul(estado_jogo):
    '''
    Função responsável por verificar se um determinado jogador marcou golo. 
    Para fazer esta verificação poderá fazer uso das constantes: 
    LADO_MAIOR_AREA e 
    START_POS_BALIZAS. 
    Note que sempre que há um golo, deverá atualizar a pontuação do jogador, 
    criar um ficheiro que permita fazer a análise da jogada pelo VAR, 
    e reiniciar o jogo com a bola ao centro. 
    O ficheiro para o VAR deverá conter todas as informações necessárias 
    para repetir a jogada, usando as informações disponíveis no objeto 
    estado_jogo['var']. O ficheiro deverá ter o nome 
    
    replay_golo_jv_[TotalGolosJogadorVermelho]_ja_[TotalGolosJogadorAzul].txt 
    
    onde [TotalGolosJogadorVermelho], [TotalGolosJogadorAzul] 
    deverão ser substituídos pelo número de golos marcados pelo jogador vermelho 
    e azul, respectivamente. Este ficheiro deverá conter 3 linhas, estruturadas 
    da seguinte forma:
    Linha 1 - coordenadas da bola;
    Linha 2 - coordenadas do jogador vermelho;
    Linha 3 - coordenadas do jogador azul;
    
    Em cada linha, os valores de xx e yy das coordenadas são separados por uma 
    ',', e cada coordenada é separada por um ';'.
    '''
    bola, x_dir, y_dir, last = estado_jogo['bola']
    pos_bola = bola.pos()

    if pos_bola[0] <= -LARGURA_JANELA/2 + RAIO_BOLA:
        if START_POS_BALIZAS/2 - RAIO_BOLA > pos_bola[1] > -START_POS_BALIZAS/2 + RAIO_BOLA:
            estado_jogo['pontuacao_jogador_azul'] += 1
            bola.clear()
            update_board(estado_jogo)
            estado_jogo['bola'] = criar_bola()
            Escreve_ficheiro(estado_jogo['var'], estado_jogo['pontuacao_jogador_azul'], estado_jogo['pontuacao_jogador_vermelho'])


def Escreve_ficheiro(Params, azul, vermelho):
    f = open('Replay_golos/replay_golo_jv_{gol_v}_ja_{gol_a}.txt'.format(gol_v=vermelho, gol_a=azul), "w")

    for pos in Params['bola']:
        f.write(str(pos[0]) + "," + str(pos[1]) + ";")
    f.write('\n')
    for pos in Params['jogador_vermelho']:
        f.write(str(pos[0]) + "," + str(pos[1]) + ";")
    f.write('\n')
    for pos in Params['jogador_azul']:
        f.write(str(pos[0]) + "," + str(pos[1]) + ";")

    f.close()
    Params['bola'] = []
    Params['jogador_vermelho'] = []
    Params['jogador_azul'] = []


def verifica_golos(estado_jogo):
    verifica_golo_jogador_vermelho(estado_jogo)
    verifica_golo_jogador_azul(estado_jogo)


def verifica_toque_jogador_azul(estado_jogo):
    '''
    Função responsável por verificar se o jogador tocou na bola. 
    Sempre que um jogador toca na bola, deverá mudar a direção desta.
    '''
    bola, x_dir, y_dir, last = estado_jogo['bola']
    pos_bola = bola.pos()
    jogador = estado_jogo['jogador_azul']
    pos_jogador = jogador.pos()

    distance = math.sqrt((pos_jogador[0] - pos_bola[0]) ** 2 + (pos_jogador[1] - pos_bola[1]) ** 2)

    if distance <= 10 * DEFAULT_TURTLE_SCALE + RAIO_BOLA:

        v1 = 1, 0
        v2 = pos_bola[0] - pos_jogador[0], pos_bola[1] - pos_jogador[1]

        numerador = (v1[0] * v2[0]) + (v1[1] * v2[1])
        denominador = (math.sqrt(v1[0]*v1[0] + v1[1]*v1[1]))*(math.sqrt(v2[0]*v2[0] + v2[1]*v2[1]))
        coisa = numerador/denominador
        teta = math.acos(coisa)
        angle = angle_things(pos_bola, last)
        estado_jogo['bola'] = bola, math.cos(angle + x_dir), math.sin(angle + y_dir), pos_bola


def verifica_toque_jogador_vermelho(estado_jogo):
    '''
    Função responsável por verificar se o jogador tocou na bola. 
    Sempre que um jogador toca na bola, deverá mudar a direção desta.
    '''
    pass


def guarda_posicoes_para_var(estado_jogo):
    estado_jogo['var']['bola'].append(estado_jogo['bola'][0].pos())
    estado_jogo['var']['jogador_vermelho'].append(estado_jogo['jogador_vermelho'].pos())
    estado_jogo['var']['jogador_azul'].append(estado_jogo['jogador_azul'].pos())


def main():
    estado_jogo = init_state()
    setup(estado_jogo, True)
    while estado_jogo['KeepItGoing']:
        estado_jogo['janela'].update()
        guarda_posicoes_para_var(estado_jogo)
        if estado_jogo['bola'] is not None:
            movimenta_bola(estado_jogo)
        verifica_colisoes_ambiente(estado_jogo)
        verifica_golos(estado_jogo)
        if estado_jogo['jogador_vermelho'] is not None:
            verifica_toque_jogador_azul(estado_jogo)
        if estado_jogo['jogador_azul'] is not None:
            verifica_toque_jogador_vermelho(estado_jogo)
    print("Adeus")
    estado_jogo['janela'].bye()

if __name__ == '__main__':
    main()
