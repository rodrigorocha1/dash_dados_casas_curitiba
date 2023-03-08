from dash import Dash, html, dcc
import dash_bootstrap_components as dbc


class APP:
    def __init__(self):
        self.app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
        self.app.config['suppress_callback_exceptions'] = True
        self.app.scripts.config.serve_locally = True
        self.app.layout = self.gerar_layout()

    def gerar_layout(self):
        return html.Div(
            [
                dbc.Row(
                    'inputs',
                    id='id_linha_inputs'
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                dbc.Card(
                                                    [
                                                        html.H4(f'{i} - Total Casassss')
                                                    ],
                                                    className='class-card-cartoes'
                                                )
                                            ],
                                            md=3
                                        ) for i in range(1, 4)
                                    ]
                                ),
                                dbc.Row(
                                    dcc.Graph(id='id_grafico')
                                ),
                            ],
                            id='coluna_cartoes_graficos',
                            className='class_coluna_cartões_graficos',
                            md=10),
                        dbc.Col('2 coluna', md=2)
                    ],
                    id='id_segunda_linha'
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Row('wdefef', className='class_coluna_segunda_linha'),
                            md=6,

                        ),
                        dbc.Col(
                            dbc.Row('wdefef', className='class_coluna_segunda_linha'),
                            md=6,

                        )
                    ],
                    id='id_terceira_linha'
                ),
            ], id='id_main_div'
        )

    def rodar_aplicacao(self):
        self.app.run_server(debug=True, port=8044)


pp = APP()
server = pp.app.server

if __name__ == '__main__':
    pp.rodar_aplicacao()
