# TODO:
# - channel logos for Enigma, maybe from enElchi?
# - http://linux.kompiliert.net/contrib/DeepBlue.skin-recordinginfo.diff
# - where has DeepBlue gone?
# - where has sttng-blue gone?
# - manage symlinks with alternatives?

%define configdir %(vdr-config --configdir 2>/dev/null || echo ERROR)
%define datadir   %(vdr-config --datadir   2>/dev/null || echo ERROR)
%define vdr_group %(vdr-config --group     2>/dev/null || echo ERROR)
%define vdr_user  %(vdr-config --user      2>/dev/null || echo ERROR)

Name:           vdr-skins
Version:        20061119
Release:        1%{?dist}
Summary:        Collection of OSD skins for VDR

Group:          Applications/Multimedia
License:        GPL

# Non-linked tarballs prepared with source99

# http://home.arcor.de/bjoern.sturzrehm/vdr/
Source0:        http://home.arcor.de/bjoern.sturzrehm/vdr/SilverGreen-0.1.7.tar.bz2
# http://skins.vdr-developer.org/
Source1:        http://cachalot.mine.nu/src/misc/izegrey16-1.0-20050304-nologos.tar.bz2
# http://home.pages.at/brougs78/
# http://ventoso.org/luca/vdr/
Source2:        http://cachalot.mine.nu/src/misc/vdrskin-enigma-0.3a-nologos.tar.bz2
# http://vdr.pfroen.de/
# http://www.netholic.com/viewtopic.php?t=1464
Source3:        http://cachalot.mine.nu/src/misc/DeepBlue-0.1.4-nologos.tar.bz2
# http://www.saunalahti.fi/~rahrenbe/vdr/soppalusikka/
Source4:        http://cachalot.mine.nu/src/misc/vdrskin-enElchi-0.7.1-nologos.tar.bz2
# http://www.fdm-ware.de/vdrskin/
Source5:        http://cachalot.mine.nu/src/misc/Aluminium-1.0-demo-nologos.tar.bz2
# http://www.magoa.net/linux/contrib/
Source6:        http://www.magoa.net/linux/contrib/EgalSimple-1.0-demo.tar.bz2
# http://www.vdrskins.org/vdrskins/thumbnails.php?album=58
Source8:        http://www.magoa.net/sttng-blue.theme
Source99:       %{name}-prepare-tarballs.sh

Patch0:         %{name}-aluminium-i18n.patch
Patch1:         %{name}-egalsimple-i18n.patch
Patch2:         %{name}-izegrey16-i18n.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  vdr-devel
Requires:       vdr-text2skin >= 1.1, %{datadir}/text2skin
Requires:       bitstream-vera-fonts

%description
This package contains a collection of skins for VDR's on-screen display.


%prep
%setup -q -c -a1 -a2 -a3 -a4 -a5 -a6
find . -type d -exec chmod 755 {} ';'
find . -type f -exec chmod 644 {} ';'
find . -type d -name CVS* | xargs rm -r
sed -i -e 's/\r//g' SilverGreen/{HISTORY,README,SilverGreen.trans}
for f in DeepBlue/HISTORY enElchi/HISTORY Enigma/TODO \
    SilverGreen/{HISTORY,README*}; do
    iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f
done
%patch0
%patch1
%patch2

SKINS=$(find * -maxdepth 0 -type d)

mv DeepBlue/COPYING .
for s in $SKINS ; do
    for f in COPYING HISTORY README README.DE TODO ; do
       [ -f $s/$f ] && mv $s/$f $f.$s
    done
done

find . -type f -name "*.theme" -exec mv {} . ';'
for s in $SKINS ; do
    [ -f $s-default.theme ] || touch $s-default.theme
done

ln -sf mp3.png Aluminium/replay/mp3oss.png
rm Aluminium/{Aluminium.skin.*,MERKEN}

cd DeepBlue
mv images images-normal
ln -s images-normal images
mv logos logos-normal
ln -s logos-normal logos
cd ..

rm -r EgalSimple/{EgalSimple.skin.*,themes}

cd Enigma
rm -r themes
ln -sf %{_datadir}/fonts/bitstream-vera/VeraMono.ttf FontMonoSpaced.ttf
find . -type f -iname thumbs.db | xargs rm
mv icons icons-dxr3
ln -s icons-normal icons
cd ..

rm -rf enElchi/themes

sed -i -e \
    's|Vera\(Bd\)\?\.ttf|%{_datadir}/fonts/bitstream-vera/Vera\1.ttf|' \
    izegrey16/izegrey16.skin


%build


%install
rm -rf $RPM_BUILD_ROOT

install -dm 755 $RPM_BUILD_ROOT%{configdir}/themes
install -pm 644 *.theme %{SOURCE8} $RPM_BUILD_ROOT%{configdir}/themes/
echo "%%defattr(-,%{vdr_user},%{vdr_group},-)" > %{name}.themes
find $RPM_BUILD_ROOT%{configdir}/themes -name "*.theme" -size 0 \
    -printf "%%%%ghost %%p\n" >> %{name}.themes
find $RPM_BUILD_ROOT%{configdir}/themes -name "*.theme" ! -size 0 \
    -print >> %{name}.themes
%{__perl} -pi -e "s|$RPM_BUILD_ROOT||" %{name}.themes

install -dm 755 $RPM_BUILD_ROOT%{datadir}/text2skin
cp -pR $(find * -maxdepth 0 -type d) $RPM_BUILD_ROOT%{datadir}/text2skin/


%clean
rm -rf $RPM_BUILD_ROOT


%triggerin -- vdr-dxr3
for l in DeepBlue/{images,logos} enElchi/logos Enigma/icons ; do
    [ -L %{datadir}/text2skin/$l -o ! -e %{datadir}/text2skin/$l ] && \
    rm -f %{datadir}/text2skin/$l && \
    ln -s $(basename $l)-dxr3 %{datadir}/text2skin/$l || :
done

%triggerun -- vdr-dxr3
if [ $2 -eq 0 ] ; then
    for l in DeepBlue/{images,logos} enElchi/logos Enigma/icons ; do
        [ -L %{datadir}/text2skin/$l -o ! -e %{datadir}/text2skin/$l ] && \
        rm -f %{datadir}/text2skin/$l && \
        ln -s $(basename $l)-normal %{datadir}/text2skin/$l || :
    done
fi


%files -f %{name}.themes
%defattr(-,root,root,-)
%doc COPYING* HISTORY.* README.*

%{datadir}/text2skin/Aluminium/

%dir %{datadir}/text2skin/DeepBlue/
%{datadir}/text2skin/DeepBlue/DeepBlue.*
%{datadir}/text2skin/DeepBlue/images-*
%verify(not link) %{datadir}/text2skin/DeepBlue/images
%{datadir}/text2skin/DeepBlue/logos-*
%verify(not link) %{datadir}/text2skin/DeepBlue/logos

%{datadir}/text2skin/EgalSimple/

%dir %{datadir}/text2skin/enElchi/
%{datadir}/text2skin/enElchi/enElchi*
%verify(not link) %{datadir}/text2skin/enElchi/logos
%{datadir}/text2skin/enElchi/logos-*/
%{datadir}/text2skin/enElchi/symbols/

%dir %{datadir}/text2skin/Enigma/
%{datadir}/text2skin/Enigma/Enigma*
%{datadir}/text2skin/Enigma/Font*
%{datadir}/text2skin/Enigma/fonts/
%{datadir}/text2skin/Enigma/hqlogos/
%{datadir}/text2skin/Enigma/icons-*/
%verify(not link) %{datadir}/text2skin/Enigma/icons
%{datadir}/text2skin/Enigma/pics/
%{datadir}/text2skin/Enigma/symbols/

%{datadir}/text2skin/izegrey16/

%{datadir}/text2skin/SilverGreen/


%changelog
* Sun Nov 19 2006 Ville Skyttä <ville.skytta at iki.fi> - 20061119-3
- Install skins to /usr/share/vdr/text2skin.
- Don't ship channel logos.

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 20060924-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Sun Sep 24 2006 Ville Skyttä <ville.skytta at iki.fi> - 20060924-1
- Add DXR3 compatible image set for DeepBlue from cccache.

* Sun May 21 2006 Ville Skyttä <ville.skytta at iki.fi> - 20060311-2
- Fix some enElchi logos.

* Sat Mar 18 2006 Thorsten Leemhuis <fedora at leemhuis.info> - 20060311-1
- drop 0.lvn from release

* Sat Mar 11 2006 Ville Skyttä <ville.skytta at iki.fi> - 20060311-0.lvn.1
- Update SilverGreen to 0.1.7, translations included upstream.

* Wed Mar  1 2006 Ville Skyttä <ville.skytta at iki.fi> - 20060301-0.lvn.1
- Update SilverGreen to 0.1.6 and enElchi to 0.7.1 (fixes applied upstream).

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Wed Nov 30 2005 Ville Skyttä <ville.skytta at iki.fi> - 20051130-0.lvn.1
- First livna release.

* Wed Nov 23 2005 Ville Skyttä <ville.skytta at iki.fi> - 20051123-0.1
- Add DXR3-compatible icons for Enigma from Luca Olivetti.
- Fix monospaced font for Enigma.
- Fix linefeeds in docs and convert them to UTF-8.

* Sat Oct 22 2005 Ville Skyttä <ville.skytta at iki.fi> - 20051022-0.1
- Add some Finnish translations.

* Fri Oct 21 2005 Ville Skyttä <ville.skytta at iki.fi> - 20051021-0.1
- Update enElchi to 0.7.0, add vdr-dxr3 triggers.

* Fri Aug 19 2005 Ville Skyttä <ville.skytta at iki.fi> - 20050819-0.1
- First build, with SilverGreen 0.1.4, izegrey16 1.0-20050304,
  Enigma 0.3a, DeepBlue 0.1.4, enElchi 0.6.0, Aluminium (unofficial),
  EgalSimple (unofficial), and a blue theme for ST:TNG.
