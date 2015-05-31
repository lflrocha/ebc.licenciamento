## Script (Python) "getImagensCatalogo"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
imagens = context.portal_catalog.searchResults(Type='Programa', review_state='published')

vet = []

for imagem in imagens:

  obj = imagem.getObject()
  cat = obj.getCatalogo()
  if len(cat) > 0:
    vet.append(imagem)

return vet
