<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

  <xsl:output method="text" encoding="UTF-8" />

  <xsl:template match="comps">
    <xsl:text>Essential:&#xA;</xsl:text>
    <xsl:for-each
      select="group[id='core']/packagelist/packagereq[@type='mandatory']">
      <xsl:sort select="." />
      <xsl:text>  </xsl:text>
      <xsl:value-of select="." />
      <xsl:text>&#xA;</xsl:text>
    </xsl:for-each>
  </xsl:template>

</xsl:stylesheet>
