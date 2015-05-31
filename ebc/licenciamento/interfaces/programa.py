from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from ebc.licenciamento import licenciamentoMessageFactory as _

class IPrograma(Interface):
    """Programa"""
    
    # -*- schema definition goes here -*-
    descricao_sumaria = schema.Text(
        title=_(u"Descricao Sumaria"), 
        required=True,
        description=_(u"Field description"),
    )

    descricao = schema.Text(
        title=_(u"Descricao"), 
        required=True,
        description=_(u"Field description"),
    )

    catalogo = schema.Bytes(
        title=_(u"Catalogo"), 
        required=True,
        description=_(u"Selecione o arquivo do catalogo"),
    )

    banner = schema.Bytes(
        title=_(u"Banner"), 
        required=True,
        description=_(u"Selecione o arquivo do banner"),
    )

    thumb = schema.Bytes(
        title=_(u"Thumb"), 
        required=True,
        description=_(u"Selecione a imagem para a listagem de programas"),
    )

    duracao = schema.TextLine(
        title=_(u"Duracao"), 
        required=False,
        description=_(u"Field description"),
    )

    temporadas = schema.TextLine(
        title=_(u"Temporadas"), 
        required=False,
        description=_(u"Field description"),
    )

    formato = schema.TextLine(
        title=_(u"Formato"), 
        required=False,
        description=_(u"Field description"),
    )

    categoria = schema.TextLine(
        title=_(u"Categoria"), 
        required=False,
        description=_(u"Field description"),
    )

    direcao = schema.TextLine(
        title=_(u"Direcao"), 
        required=False,
        description=_(u"Field description"),
    )

    pais = schema.TextLine(
        title=_(u"Pais de origem"), 
        required=False,
        description=_(u"Field description"),
    )

    titulo_original = schema.TextLine(
        title=_(u"Titulo Original"), 
        required=False,
        description=_(u"Field description"),
    )


