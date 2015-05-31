## Script (Python) "getVideo"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
path = '/'.join(context.getPhysicalPath())
video = context.portal_catalog.searchResults(Type='File', path=path)

return video
