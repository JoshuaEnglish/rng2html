import os
from lxml import etree

rngpath = os.path.join(os.getcwd(),'rng', 'addressbook.rng')

rng = etree.parse(rngpath)

xsl = '''<?xml version="1.0" ?>
    <xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:rng="http://relaxng.org/ns/structure/1.0"
    exclude-result-prefixes="rng">
    <xsl:output method="html" indent="yes" />

    <xsl:template match="/">
      <div class="addressbook w3-container">
      <h2>Addresses</h2>
      <xsl:apply-templates />
      </div>
    </xsl:template>

    <xsl:template match="rng:zeroOrMore">
    % for card in addresses
    <xsl:apply-templates />
    % end
    </xsl:template>

    <xsl:template match="rng:element[@name='card']">
    <div class="w3-card"><xsl:apply-templates/></div>
    </xsl:template>

    <xsl:template match="rng:element[@name='name']">
    <p>{{card['name']}}</p>
    </xsl:template>

    <xsl:template match="rng:element[@name='email']">
    <p>{{card['email']}}</p>
    </xsl:template>

    </xsl:stylesheet>'''

# this is not working until I get a lot smarter about xslt
rng2view = '''<?xml version="1.0" ?>
    <xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:rng="http://relaxng.org/ns/structure/1.0"
    exclude-result-prefixes="rng">
    
    <xsl:output method="html" indent="yes" />
    
    
    <xsl:template match="/">
        <div class="w3-container">
        <xsl:copy-of select="@*|/@*[name() = 'name']"/>
        <xsl:apply-templates/>
        </div>
    </xsl:template>
    
    <xsl:template match="rng:zeroOrMore">
    
    </xsl:template>
    
    </xsl:stylesheet>
'''

def name(node): 
        return node.get('name')
    
def parent_name(node):
    return node.getparent().get('name')
        
class XSLTViewMaker:
    def __init__(self, rngTree):
        self.tree = rngTree
        self.doc = self.tree.getroot()
        self.text = self.export()
        
    def export(self):
    

        res = [] # list of strings
        res.append('''<?xml version="1.0" ?>
        <xsl:stylesheet version="1.0"
        xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
        xmlns:rng="http://relaxng.org/ns/structure/1.0"
        exclude-result-prefixes="rng">
        
        <xsl:output method="html" indent="yes" />''')
        
        # manage top level element
        res.append('''
        <xsl:template match="/">
            <div class="w3-container {}">
            <xsl:apply-templates/>
            </div>
        </xsl:template>'''.format(self.doc.get('name')))
        
        for kiddo in self.doc.iterchildren():
            res.extend(self.handle_child(kiddo))
        
        res.append('</xsl:stylesheet>')
        return '\n'.join(res)
        
    def handle_child(self, node):
        localname = node.tag.replace('{%s}' % node.nsmap[None], '')
        funcname = 'do_%s' % localname
        #print('looking for %s with %s' % (localname, node.attrib))
        if hasattr(self, funcname):
            return getattr(self, funcname)(node)
        return []
        
    def do_zeroOrMore(self, node):
        res = ['<xsl:template match="rng:zeroOrMore">',]
        for child in node.iterchildren():
            thing = child.get('name')
            stuff = node.getparent().get('name')
            res.append('% for {} in {}:'.format(thing, stuff)) 
            res.append('<xsl:apply-templates/>')
            res.append('% end')
        res.append('</xsl:template>')
        
        for child in node.iterchildren():
            res.extend(self.handle_child(child))
            
        return res

    def do_element(self, node):
        #etree.dump(node)
        
        
        if len(node) > 1:
            res = ['''<xsl:template match="rng:element[@name='{}']">'''.format(node.get('name'))]
            res.append('<div class="w3-card">')
            for child in node.iterchildren():
                res.extend(self.handle_child(child))
            res.append('</div>')
            res.append('</xsl:template>')
        elif len(node) == 1:
            etree.dump(node)
            label = ''
            if node.get('{cardview}label', 'no').lower() == 'yes':
                label = '<span class="label">%s</span>: ' % name(node).title()
            res = []
            res.append('<p>%s{{%s["%s"]}}</p>' % (label, parent_name(node), name(node)))
            print('\n'.join(res))
            
        
        return res
            
            

xslNode = etree.fromstring(XSLTViewMaker(rng).text)
#etree.dump(xslNode)
xslt = etree.XSLT(xslNode)
res = xslt(rng)
#print('-'*10)
#etree.dump(res.getroot())
#with open(os.path.join(os.getcwd(), 'views', 'addresses.tpl')) as f:
    #f.write(etree.tostring(res.getroot()))
    #res.write(f)
res.write(os.path.join(os.getcwd(), 'views', 'addresses.tpl'))
#import code
#code.interact(local=dict(rng=rng, etree=etree, res=res))
