import os
from lxml import etree

rngpath = os.path.join(os.getcwd(),'addressbook.rng')
print(rngpath, os.path.exists(rngpath))
rng = etree.parse(rngpath)

xsl = '''<?xml version="1.0" ?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns:rng="http://relaxng.org/ns/structure/1.0"
exclude-result-prefixes="rng">
<xsl:output method="html" indent="yes" />

<xsl:template match="/">
  <html>
  <body>
  <h2>RNG2HTML</h2>
  <xsl:apply-templates />
  </body>
  </html>
</xsl:template>

<xsl:template match="rng:zeroOrMore">
<div class="zero-or-more"><xsl:apply-templates /></div>
</xsl:template>

<xsl:template match="rng:element[@name='addressBook']">
<div class='addressbook'><xsl:apply-templates/></div>
</xsl:template>

<xsl:template match="rng:element[@name='card']">
<div class='card'><xsl:apply-templates/></div>
</xsl:template>

<xsl:template match="rng:element[@name='name']">
<label>Name</label><input type="text"/>
</xsl:template>

<xsl:template match="rng:element[@name='email']">
<label>Email</label><input type="text"/>
</xsl:template>

</xsl:stylesheet>'''

RNG = etree.RelaxNG(rng)

xslNode = etree.fromstring(xsl)
xslt = etree.XSLT(xslNode)
res = xslt(rng)
print(res)
