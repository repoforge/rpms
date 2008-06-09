#!/bin/sh

set -e

[ ! -e izegrey16-1.0-20050304.tar.gz ] && \
wget -q http://skins.vdr-developer.org/text2skin/files/izegrey16-1.0-20050304.tar.gz
rm -rf izegrey16
tar zxf izegrey16-1.0-20050304.tar.gz
rm -f izegrey16/{*.tar,*.ttf,logos/{*.mng,*.png,*.xpm}}
tar jcf izegrey16-1.0-20050304-nologos.tar.bz2 izegrey16
rm -rf izegrey16

[ ! -e vdrskin-enigma-0.3a.tar.bz2 ] && \
wget -q http://home.pages.at/brougs78/files/vdrskin-enigma-0.3a.tar.bz2
[ ! -e icons-low-low-col.tar.gz ] && \
wget -q http://ventoso.org/luca/vdr/Enigma/icons-low-low-col.tar.gz
rm -rf Enigma
tar jxf vdrskin-enigma-0.3a.tar.bz2
find Enigma -type d -exec chmod +x {} ';'
mv Enigma/icons Enigma/icons-normal
tar zx -C Enigma -f $PWD/icons-low-low-col.tar.gz
rm -rf Enigma/{hqlogos/*,fonts/ttf-bitstream-vera*,patches}
tar jcf vdrskin-enigma-0.3a-nologos.tar.bz2 Enigma
rm -rf Enigma

[ ! -e DeepBlue-0.1.4.tar.gz ] && \
wget -q http://vdr.pfroen.de/download/DeepBlue-0.1.4.tar.gz
[ ! -e DeepBlueDXR3.tar.bz2 ] && \
wget -q http://koti.mbnet.fi/cccatch/vdr/DeepBlueDXR3.tar.bz2
rm -rf DeepBlue DeepBlueDXR3
tar zxf DeepBlue-0.1.4.tar.gz
tar jxf DeepBlueDXR3.tar.bz2
find DeepBlueDXR3 -type d -exec chmod +x {} ';'
rm -rf DeepBlue/logos/*
mv DeepBlueDXR3/HISTORY DeepBlue
mv DeepBlueDXR3/images DeepBlue/images-dxr3
tar jcf DeepBlue-0.1.4-nologos.tar.bz2 DeepBlue
rm -rf DeepBlue DeepBlueDXR3

[ ! -e vdrskin-enElchi-0.7.1.tgz ] && \
wget -q http://www.saunalahti.fi/~rahrenbe/vdr/soppalusikka/files/vdrskin-enElchi-0.7.1.tgz
rm -rf enElchi
tar zxf vdrskin-enElchi-0.7.1.tgz
rm -f enElchi/logos-*/*
tar jcf vdrskin-enElchi-0.7.1-nologos.tar.bz2 enElchi
rm -rf enElchi

[ ! -e Aluminium-1.0-demo.tar.bz2 ] && \
wget -q http://linux.kompiliert.net/contrib/Aluminium-1.0-demo.tar.bz2
rm -rf Aluminium
tar jxf Aluminium-1.0-demo.tar.bz2
rm -f Aluminium/logos/*
tar jcf Aluminium-1.0-demo-nologos.tar.bz2 Aluminium
rm -rf Aluminium
