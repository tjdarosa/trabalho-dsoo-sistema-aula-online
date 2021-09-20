

from limite.abstractTela import AbstractTela
from datetime import datetime
import PySimpleGUI as sg


class TelaAtividade(AbstractTela):
    def __init__(self) -> None:
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
            [sg.Text('Gerenciamento de Cadastro de Atividades', size=(35,1), font=('Times', 20), justification='c')],
            [sg.Button('Listar Atividades', key=1, size=30)],
            [sg.Button('Adicionar Atividade', key=2, size=30)],
            [sg.Button('Alterar Atividade', key=3, size=30)],
            [sg.Button('Excluir Atividade', key=4, size=30)],
            [sg.Button('Adicionar Atividade de Aluno', key=5, size=30)],
            [sg.Button('Adicionar Entrega de Aluno a Atividade', key=6, size=30)],
            [sg.Button('Avaliar Atividade de Aluno', key=7, size=30)],
            [sg.Button('Retornar', key=0, size=30)]
        ]
        self.__window = sg.Window('Gerenciamento de Cadastro de Atividades', element_justification='c').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def showMessage(self, titulo: str, mensagem: str):
        return super().showMessage(titulo, mensagem)

    def mostra_atividades(self, atividades):
        layout = []
        if atividades == {}:
            layout.append(
                [sg.Text('Não há atividades cadastradas!', size=(35,1), font=('Times', 20), justification='c')])
        else:
            for key, value in atividades.items():
                layout.append([
                    [sg.Text('Código:'), sg.Text(key)],
                    [sg.Text('Título:'), sg.Text(value['titulo'])],
                    [sg.Text('Descrição:'), sg.Text(value['descricao'])],
                    [sg.Text('Prazo de entrega:'), sg.Text(value['prazo_entrega'])],
                    [sg.Text('Professor responsável:'), sg.Text(value['professor'])],
                    [sg.Text('Disciplina:'), sg.Text(value['disciplina'])]
                ])
                if len(value['atividades_aluno']) == 0:
                    layout.append(
                        [sg.Text('Nenhuma atividade entregue até o momento')]
                    )
                else:
                    for atividade in value['atividades_aluno']:
                        layout.append(
                            [sg.Text('Aluno:'), sg.Text(atividade['nome'])],
                            [sg.Text('Data de entrega:'), sg.Text(atividade['data_que_foi_entregue'])],
                            [sg.Text('Nota:'), sg.Text(atividade['nota'])],
                            [sg.Text('Status:')], sg.Text(str(atividade['status']))
                        )
            layout.append([sg.Text('')])
        layout.append([sg.OK()])
        self.__window = sg.Window('Lstagem de Atividades', element_justification='c').Layout(layout)


    def pega_dados_atividade(self, disciplinas, professores):
        layout = [
            [sg.Text('Insira o código:'), sg.InputText('Código', key='codigo')],
            [sg.Text('Insira o título:'), sg.InputText('Título', key='titulo')],
            [sg.Text('Insira a descrição:'), sg.InputText('Descrição', key='descricao')],
            [sg.Text('Insira o Prazo de Entrega:'), sg.InputText('DD/MM/AAAA', key='prazo_entrega')],
            
            [sg.Text('Selecione a disciplina:'),
             sg.Combo(
                 [''] + ['{}, cod={}'.format(disciplina['nome'], disciplina['codigo']) for disciplina in disciplinas],
                 key='disciplina')],

            [sg.Text('Selecione o professor'),
            sg.Combo(
                [''] + ['{}, id={}'.format(professor['nome'], professor['id']) for professor in professores],
                 key='professor')],

            [sg.Submit('Confirmar', key='confirmar'), sg.Cancel('Cancelar', key='cancelar')]
            ]
        self.__window = sg.Window('Cadastro de Atividades', element_justification='c').Layout(layout)
        botao, dados = self.open()
        self.close()
        self.init_components()
        return botao, dados

    def seleciona_atividade_para_excluir(self):
        try:
            layout = [
            [sg.Text('Insira o código da atividade:'), sg.InputText('codigo (ex: 123)', key='codigo')],
            [sg.Submit('Confirmar', key='confirmar'), sg.Cancel('Cancelar', key='cancelar')]
            ]
            self.__window = sg.Window('Exclusão de Cadastro de Atividades', element_justification='c').Layout(layout)
            botao, dados = self.open()
            self.close()
            self.init_components()
            return botao, dados
        except Exception:
            self.showMessage(
                'ERRO',
                'Houve um problema ao selecionar o professor!')

    def seleciona_atividade_para_alterar(self):
        try:
            layout = [
            [sg.Text('Insira o código da atividade:'), sg.InputText('codigo (ex: 123)', key='codigo')],
            [sg.Submit('Confirmar', key='confirmar'), sg.Cancel('Cancelar', key='cancelar')]
            ]
            self.__window = sg.Window('Alteração de Cadastro de Atividades', element_justification='c').Layout(layout)
            botao, dados = self.open()
            self.close()
            self.init_components()
            return botao, dados
        except Exception:
            self.showMessage(
                'ERRO',
                'Houve um problema ao selecionar o professor!')

    def pega_novos_dados_atividade(self, disciplinas, professores):
        layout = [
            [sg.Text('Insira o código:'), sg.InputText('Código', key='codigo')],
            [sg.Text('Insira o título:'), sg.InputText('Título', key='titulo')],
            [sg.Text('Insira a descrição:'), sg.InputText('Descrição', key='descricao')],
            [sg.Text('Insira o Prazo de Entrega:'), sg.InputText('DD/MM/AAAA', key='prazo_entrega')],
            
            [sg.Text('Selecione a disciplina:'),
             sg.Combo(
                 [''] + ['{}, cod={}'.format(disciplina['nome'], disciplina['codigo']) for disciplina in disciplinas],
                 key='disciplina')],

            [sg.Text('Selecione o professor'),
            sg.Combo(
                [''] + ['{}, id={}'.format(professor['nome'], professor['id']) for professor in professores],
                 key='professor')],

            [sg.Submit('Confirmar', key='confirmar'), sg.Cancel('Cancelar', key='cancelar')]
            ]
        self.__window = sg.Window('Cadastro de Atividades', element_justification='c').Layout(layout)
        botao, dados = self.open()
        self.close()
        self.init_components()
        return botao, dados
    
    
    
    
    
    
    
    
    
    
  

    # def pega_dados_atividade_aluno(self):
    #     try:
    #         data_entrega = datetime.strptime(
    #             str(input("Insira a Data de Entrega no formato dd/MM/yyyy: ")), "%d/%m/%Y")
    #         return {"data_que_foi_entregue": data_entrega}
    #     except TypeError:
    #         self.mostra_msg("Insira um valor válido!")
    #     except Exception:
    #         self.mostra_msg("Ocorreu um erro ao inserir informações")

    # def pega_nota_atividade_aluno(self):
    #     try:
    #         nota = float(
    #             input("Insira a Nota: "))
    #         if(nota > 10 or nota < 0):
    #             print("Insira valores entre 0 e 10")
    #             return None
    #         return {"nota": nota}
    #     except TypeError:
    #         self.mostra_msg("Insira um valor válido!")
    #     except Exception:
    #         self.mostra_msg("Ocorreu um erro ao inserir informações")

    

    