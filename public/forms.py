from django.forms import ModelForm
from django.forms.widgets import HiddenInput,Input,DateInput, Select,NumberInput

from .models import *


class FuncaoForm(ModelForm):
    class Meta:
        model = Funcao
        fields = '__all__'
        widgets = {'idusuarioedicao': HiddenInput(),'idusuariocadastro': HiddenInput(),'observacao': HiddenInput()}

class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'
        widgets = {
            'nome_empresa': Input(attrs={
                'style': 'width:600px'
            }),
            'razao_social': Input(attrs={
                'style': 'width:560px'
            }),
            'cpf': Input(attrs={
                'maskcpf': 'true',
                'type': 'text'
            }),
            'cnpj': Input(attrs={
               'maskcnpj': 'true',
                'type':'text'
            }),
            'telefone': Input(attrs={
                'masktelefone': 'true',
                'type': 'text'
            }),
            'telefone_fora': Input(attrs={
                'masktelefone': 'true',
                'type': 'text'
            }),
            'cep': Input(attrs={
                'maskcep': 'true',
                'type': 'text'
            }),
            'cep_cobranca': Input(attrs={
                'maskcep': 'true',
                'type': 'text'
            }),
            'data_fechamento': DateInput(attrs={
                'maskdate': 'true',
                'type': 'date'
            }),

            'inscricao_estadual': Input(attrs={
                'style': 'width:520px'
            }),
            'responsavel': Input(attrs={
                'style': 'width:555px'
            }),
            'endereco': Input(attrs={
                'style': 'width:575px'
            }),
            'email': Input(attrs={
                'style': 'width:605px'
            }),
            'endereco_cobranca': Input(attrs={
                'style': 'width:520px'
            }),
            'idusuarioedicao': HiddenInput(),
            'idusuariocadastro': HiddenInput(),
            'observacao': HiddenInput()
        }

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
                    'nome_paciente': Input(attrs={
                    'style': 'width:600px'
                    }),
                     'sexo': Select(attrs={
                     'style': 'width:100px'
                     }),
                    'endereco': Input(attrs={
                    'style': 'width:600px'
                    }),
                    'cpf': Input(attrs={
                    'maskcpf': 'true',
                    'type': 'text'
                    }),
                    'cep': Input(attrs={
                        'maskcep': 'true',
                        'type': 'text'
                    }),

                    'data_nascimento': DateInput( attrs={
                    'maskdate': 'true',
                    'type': 'date'}),

                    'telefone': Input(attrs={
                    'masktelefone': 'true',
                    'type': 'text'
                    }),

                   'idusuarioedicao': HiddenInput(),
                   'idusuariocadastro': HiddenInput(),
                   'observacao': HiddenInput()

                   }

class ExameForm(ModelForm):

    class Meta:
        model = Exame
        fields = '__all__'
        widgets = {
            'valor_ems': NumberInput(attrs={
                 'moeda': 'true',
                 'type': 'text'
            }),
            'valor_exame': Input(attrs={
                 'moeda': 'true',
                 'type': 'text'
            }),
            'valor_colaborador': Input(attrs={
                'moeda': 'true',
                'type': 'text'
            }),


            'idusuarioedicao': HiddenInput(),
            'idusuariocadastro': HiddenInput(),
            'observacao': HiddenInput()

                 }

        def __init__(self, *args, **kwargs):
            super(ExameForm, self).__init__(*args, **kwargs)
            self.fields['valor_exame'].localize = True
            self.fields['valor_exame'].widget.is_localized = True


class EspecialiadeMedicaForm(ModelForm):
    class Meta:
        model = EspecialidadeMedica
        fields = '__all__'
        widgets = {'idusuarioedicao': HiddenInput(),'idusuariocadastro': HiddenInput(),'observacao': HiddenInput()}


class PrestadorServicoForm(ModelForm):
    class Meta:
        model = PrestadorServico
        fields = '__all__'
        widgets = {
            'nome_prestador': Input(attrs={
                'style': 'width:600px'
            }),
            'endereco': Input(attrs={
                'style': 'width:600px'
            }),
            'cpf': Input(attrs={
                'maskcpf': 'true',
                'type': 'text'
            }),
            'cnpj': Input(attrs={
                'maskcnpj': 'true',
                'type': 'text'
            }),
            'telefone': Input(attrs={
                'masktelefone': 'true',
                'type': 'text'
            }),

            'idusuarioedicao': HiddenInput(),'idusuariocadastro': HiddenInput(),'observacao': HiddenInput()}
