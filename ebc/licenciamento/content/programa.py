# -*- coding: utf-8 -*-
"""Definition of the Programa content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from ebc.licenciamento import licenciamentoMessageFactory as _
from ebc.licenciamento.interfaces import IPrograma
from ebc.licenciamento.config import PROJECTNAME

ProgramaSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-



    atapi.StringField(
        'titulo_original',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Titulo original"),
            description=_(u"Informe o titulo original."),
        ),
    ),

    atapi.ImageField(
        'banner',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ImageWidget(
            label=_(u"Banner"),
            description=_(u"Selecione o arquivo do banner"),
        ),
        required=True,
        validators=('isNonEmptyFile'),
    ),

    atapi.TextField(
        'descricao',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Descricao"),
            description=_(u"Field description"),
        ),
        required=True,
    ),

    atapi.StringField(
        'pais',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Pais de origem"),
            description=_(u"Informe o pais de origem."),
        ),
    ),

    atapi.StringField(
        'direcao',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Direcao"),
            description=_(u"Informe o nome do diretor ou diretora."),
        ),
    ),

    atapi.StringField(
        'categoria',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Categoria"),
            description=_(u"Selecione a categoria"),
        ),
    ),

    atapi.StringField(
        'formato',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Formato"),
            description=_(u"Selecione o formato"),
        ),
    ),

    atapi.StringField(
        'temporadas',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Temporadas"),
            description=_(u"Informe o numero de temporadas"),
        ),
    ),

    atapi.StringField(
        'episodios',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Episodios"),
            description=_(u"Informe o numero de episodios"),
        ),
    ),

    atapi.StringField(
        'duracao',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Duracao"),
            description=_(u"Informe a duracao"),
        ),
    ),




    atapi.ImageField(
        'thumb',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ImageWidget(
            label=_(u"Thumb"),
            description=_(u"Selecione a imagem para a listagem de programas"),
        ),
        required=True,
        validators=('isNonEmptyFile'),
    ),

    atapi.TextField(
        'descricao_sumaria',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Descricao Sumaria"),
            description=_(u"Informe a descricao sumaria para a listagem de programas"),
        ),
        required=True,
    ),

    atapi.ImageField(
        'catalogo',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ImageWidget(
            label=_(u"Catalogo"),
            description=_(u"Selecione a imagem para a capa"),
        ),
        validators=('isNonEmptyFile'),
    ),


))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

ProgramaSchema['title'].storage = atapi.AnnotationStorage()
ProgramaSchema['description'].storage = atapi.AnnotationStorage()

ProgramaSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
ProgramaSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
ProgramaSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
ProgramaSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
ProgramaSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
ProgramaSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
ProgramaSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
ProgramaSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
ProgramaSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
ProgramaSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
ProgramaSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
ProgramaSchema['nextPreviousEnabled'].widget.visible = {"edit": "invisible", "view": "invisible"}



schemata.finalizeATCTSchema(
    ProgramaSchema,
    folderish=True,
    moveDiscussion=False
)

class Programa(folder.ATFolder):
    """Programa"""
    implements(IPrograma)

    meta_type = "Programa"
    schema = ProgramaSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    catalogo = atapi.ATFieldProperty('catalogo')

    descricao_sumaria = atapi.ATFieldProperty('descricao_sumaria')

    descricao = atapi.ATFieldProperty('descricao')

    banner = atapi.ATFieldProperty('banner')

    thumb = atapi.ATFieldProperty('thumb')

    duracao = atapi.ATFieldProperty('duracao')

    temporadas = atapi.ATFieldProperty('temporadas')

    formato = atapi.ATFieldProperty('formato')

    categoria = atapi.ATFieldProperty('categoria')

    direcao = atapi.ATFieldProperty('direcao')

    pais = atapi.ATFieldProperty('pais')

    titulo_original = atapi.ATFieldProperty('titulo_original')



atapi.registerType(Programa, PROJECTNAME)
