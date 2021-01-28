from django.db import models
from autoslug import AutoSlugField
from django.utils.translation import gettext_lazy as _


class Base(models.Model):
    criacao = models.DateTimeField('Criação', auto_now_add=True)
    modificado = models.DateTimeField('Modificado', auto_now=True)
    idusuariocadastro = models.IntegerField('idusuariocadastro',  blank=True, null=True)
    idusuarioedicao = models.IntegerField('idusuarioedicao', blank=True, null=True)
    ativo = models.BooleanField('Ativo?', default=True)
    observacao = models.TextField('observacao', blank=True)

    class Meta:
        abstract = True

class Funcao(Base):
    nome_funcao = models.CharField('Nome função', max_length=255)
    cbo = models.CharField('cbo', max_length=50)
    tipo_cbo = models.CharField('tipo_cbo', max_length=15, null=True)
    slug = AutoSlugField(populate_from='nome_funcao', default='', unique=True)

    class Meta:
        verbose_name = 'Função'
        verbose_name_plural = 'Funções'
        ordering = ['id']

    def __str__(self):
        return self.nome_funcao

class Pais(Base):
    sigla = models.CharField('sigla', max_length=5)
    codigo = models.IntegerField('codigo', null=False, unique=True)
    nomepais = models.CharField('nome país', max_length=150)

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.nomepais

class Estado(Base):
    abreviatura = models.CharField('abreviatura', max_length=5)
    nomeestado = models.CharField('nome estado', max_length=100, unique=True)
    pais = models.ForeignKey(Pais, null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return self.nomeestado

class Cidade(Base):
    nomecidade = models.CharField('Nome Cidade', max_length=200)
    estado = models.ForeignKey(Estado, null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return self.nomecidade

class Turno(Base):
    nome_turno = models.CharField('Descrição Turno', max_length=20, null=True)

    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'

    def __str__(self):
        return self.nometurno

class TipoSanguineo(Base):
    fator = models.CharField('Fator RH', max_length=20, null=True)

    class Meta:
        verbose_name = 'Tipo Sanguíneo'
        verbose_name_plural = 'Tipos Sanguíneos'

    def __str__(self):
        return self.fator

class UnidadeClinica(Base):
    nome_unidade = models.CharField('nomeunidade', max_length=100, null=True)
    cnpj = models.CharField('cnpj', max_length=100, null=True)
    endereco = models.CharField('endereco', max_length=255, null=True)
    telefone = models.CharField('telefone', max_length=100, null=True)
    cep = models.CharField('cep', max_length=100, null=True)
    cidade = models.ForeignKey(Cidade, null=False, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Unidade Clínica'
        verbose_name_plural = 'Unidades Clínicas'

    def __str__(self):
        return self.nome_unidade

class Empresa(Base):
    nome_empresa = models.CharField('Nome', max_length=255, null=True)
    razao_social = models.CharField('Razão Social', max_length=100, null=False)
    cnpj = models.CharField('Cnpj', max_length=100, null=True)
    cpf = models.CharField('Cpf', max_length=30, null=False)
    inscricao_estadual = models.CharField('Inscricao Estadual', max_length=50, null=True)
    responsavel = models.CharField('Responsavel', max_length=200, null=True)
    endereco = models.CharField('Endereco', max_length=150, null=True)
    telefone = models.CharField('Telefone', max_length=30, null=True)
    cep = models.CharField('Cep', max_length=20, null=True)
    email = models.EmailField('Email', max_length=150, null=True)
    endereco_cobranca = models.CharField('Endereço Cobrança', max_length=255, null=True)
    cep_cobranca = models.CharField('Cep Cobrança', max_length=30, null=True)
    cidade_cobranca = models.CharField('Cidade Cobrança', max_length=200, null=True)
    empresa_fora = models.BooleanField('Empresa Fora', default=False)
    telefone_fora = models.CharField('Telefone Fora', max_length=30, null=True)
    data_fechamento = models.DateField('Data Fechamento', null=False)
    convenio = models.BooleanField('Convênio', default=False)
    situacao_convenio= models.BooleanField('Situacao Convênio', default=False)
    slug = AutoSlugField(populate_from='cnpj', default='', unique=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nome_empresa

class Sexo(models.TextChoices):
        Selecione = '-', _('Selecione')
        Masculino = 'M', _('Masculino')
        Femenino = 'F', _('Feminino')
        Outro = 'o', _('Outro')

class Paciente(Base):

    nome_paciente = models.CharField('Nome', max_length=255, null=False)
    data_nascimento = models.DateField('Data Nacimeno', max_length=20, null=False)
   # sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=True)
    sexo = models.CharField(
        max_length=2,
        choices=Sexo.choices,
        default=Sexo.Selecione,
    )
    rg = models.CharField('Rg', max_length=15, null=True)
    cpf = models.CharField('Cpf', max_length=20, null=False)
    endereco = models.CharField('Endereço', max_length=255, null=True)
    telefone = models.CharField('Telefone', max_length=255, null=True)
    cep = models.CharField('Cep', max_length=20, null=True)
    slug = AutoSlugField(populate_from='cpf', default='', unique=True)


    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return self.nome_paciente

class EspecialidadeMedica(Base):
    especialidade_medica = models.CharField('Especialidade Médica', max_length=255, null=False)
    slug = AutoSlugField(populate_from='especialidade_medica', default='', unique=True)

    class Meta:
        verbose_name = 'Especialidade Medica'
        verbose_name_plural = 'Especialidades Medicas'

    def __str__(self):
        return self.especialidade_medica


class Exame(Base):
    nome_exame = models.CharField('Exame Médico', max_length=150, null=False)
    idespecialidademedica = models.ForeignKey(EspecialidadeMedica, verbose_name="Especialidade", on_delete=models.CASCADE, null=False)
    valor_colaborador = models.CharField('Valor Colaborador R$', max_length=15, null=False)
    valor_ems = models.CharField('Valor Ems R$', max_length=15, null=False)
    valor_exame = models.CharField('Valor Exame R$', max_length=15, null=False)
    slug = AutoSlugField(populate_from='nome_exame', default='', unique=True)

    class Meta:
        verbose_name = 'Exame'
        verbose_name_plural = 'Exames'

    def __str__(self):
        return self.nome_exame



class PrestadorServico(Base):
    nome_prestador = models.CharField('Prestador Serviço', max_length=255, null=False)
    crm = models.CharField('Crm', max_length=20, null=True)
    cpf = models.CharField('Cpf', max_length=20, null=True)
    cnpj = models.CharField('Cnpj', max_length=30, null=True)
    telefone = models.CharField('Telefone', max_length=20, null=False)
    endereco = models.CharField('Endereço', max_length=150, null=True)
    email = models.EmailField('Email', max_length=200, null=True)
    slug = AutoSlugField(populate_from='nome_prestador', default='', unique=True)

    class Meta:
        verbose_name = 'Prestador Serviço'
        verbose_name_plural = 'Prestadores de Serviço'

    def __str__(self):
        return self.nome_prestador

class FichaExame(Base):

    idpaciente = models.IntegerField(null=False)
    idexame = models.IntegerField(null=False)
    idempresa = models.IntegerField(null=False)
    numeroexame = models.IntegerField(default=0, null=False)
    periodo = models.CharField('Período', max_length=20, null=False)
    tipo_pagamento = models.CharField('Tipo Pagamento', max_length=20, null=False)
    matricula_esocial = models.CharField('Matricula Esocial', max_length=50, null=True)
    valor_exame_estimado = models.DecimalField(max_digits=8, decimal_places=2)
    valor_prestador_servico = models.DecimalField(max_digits=8, decimal_places=2)
    valor_exame_clinica = models.DecimalField(max_digits=8, decimal_places=2)
    valor_exame_pago = models.DecimalField(max_digits=8, decimal_places=2)
    data_exame = models.DateField('Data Exame', null=False)
    faturado = models.BooleanField(default=False)
    exame_conferido = models.BooleanField(default=False)
    aso_pendente = models.BooleanField(default=False)
    exame_liberado = models.BooleanField(default=False)
    prestador_visualizou_exame = models.BooleanField(default=False)
    paciente_preferencial = models.BooleanField(default=False)
    senha = models.CharField(max_length=20, null=True)

    #cria um auto-increment para o numero do exame
    def save(self, *args, **kwargs):
        self.numeroexame = self.numeroexame + 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name='FichaExame'
        verbose_name_plural = "FichaExames"

    def __str__(self):
        return self.numeroexame

class FichaExameExcluido(Base):

    idpaciente = models.IntegerField(null=False)
    idexame = models.IntegerField(null=False)
    idempresa = models.IntegerField(null=False)
    numeroexame = models.IntegerField(null=False)
    periodo = models.CharField('Período', max_length=20, null=False)
    tipo_pagamento = models.CharField('Tipo Pagamento', max_length=20, null=False)
    matricula_esocial = models.CharField('Matricula Esocial', max_length=50, null=True)
    valor_exame_estimado = models.DecimalField(max_digits=8, decimal_places=2)
    valor_prestador_servico = models.DecimalField(max_digits=8, decimal_places=2)
    valor_exame_clinica = models.DecimalField(max_digits=8, decimal_places=2)
    valor_exame_pago = models.DecimalField(max_digits=8, decimal_places=2)
    data_exame = models.DateField('Data Exame', null=False)
    faturado = models.BooleanField(default=False)
    exame_conferido = models.BooleanField(default=False)
    aso_pendente = models.BooleanField(default=False)
    exame_liberado = models.BooleanField(default=False)
    prestador_visualizou_exame = models.BooleanField(default=False)
    paciente_preferencial = models.BooleanField(default=False)
    senha = models.CharField(max_length=20, null=True)

    class Meta:
        verbose_name = 'FichaExameExcluido'
        verbose_name_plural = "FichaExamesExcluidos"

    def __str__(self):
        return self.numeroexame

class FichaExameEditado(Base):

    idfichaexame = models.IntegerField(null=False)
    motivo_edicao = models.TextField(null=False)
    idfuncao_antiga = models.IntegerField(null=False)
    idfuncao_nova = models.IntegerField(null=False)
    idpaciente_antigo = models.IntegerField(null=False)
    idpaciente_novo = models.IntegerField(null=False)
    idempresa_antigo = models.IntegerField(null=False)
    idempresa_novo = models.IntegerField(null=False)
    tipo_pagamento_antigo = models.CharField(max_length=20, null=True)
    tipo_pagamento_novo = models.CharField(max_length=20, null=False)

    class Meta:
        verbose_name = 'FichaExameEditado'
        verbose_name_plural = 'FichaExamesEdiados'

    def __str__(self):
        return self.idfichaexame

class AvaliacaoMedica(Base):
    idfichaexame = models.IntegerField(null=False)
    idquestionario_avaliacao_medica = models.IntegerField(null=False)
    data_avaliacao = models.DateTimeField(null=False)
    respondido = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Avaliação Medica'
        verbose_name_plural = "Avalições Medicas"

    def __str__(self):
        return self.idfichaexame

class QuestionarioAvaliacaoMedica(Base):
    idpergunta = models.IntegerField(null=True)
    resposta = models.CharField(max_length=50, null=False)

    class Meta:
        verbose_name = 'Questionário Avaliação Médica'
        verbose_name_plural = "Questionário Avaliações Médicas"

    def __str__(self):
        self.id

class Pergunta(Base):
    descricao_pergunta = models.CharField('Descrição pergunta', max_length=255, null=False)
    tipo_resposta = models.CharField('Tipo Resposta', max_length=20)

    class Meta:
        verbose_name = 'Pergunta'
        verbose_name_plural = 'Perguntas'

    def __str__(self):
        return self.descricao_pergunta

class Alternativa(Base):
    item = models.CharField('Item', max_length=255)
    idpergunta = models.IntegerField(null=False)

    class Meta:
        verbose_name = 'Alternativa'
        verbose_name_plural = 'Alternativas'

    def __str__(self):
        return self.item
