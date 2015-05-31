## Script (Python) "getProdutoras"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
path = '/'.join(context.getPhysicalPath())
imagens = context.portal_catalog.searchResults(Type='Image', path=path)

return imagens
