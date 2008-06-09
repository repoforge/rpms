%define pname     text2skin
%define plugindir %(vdr-config --plugindir  2>/dev/null || echo ERROR)
%define configdir %(vdr-config --configdir  2>/dev/null || echo ERROR)
%define datadir   %(vdr-config --datadir    2>/dev/null || echo ERROR)
%define apiver    %(vdr-config --apiversion 2>/dev/null || echo ERROR)

%define cvs 20051217

Name:           vdr-%{pname}
Version:        1.1
Release:        18.%{cvs}cvs%{?dist}
Summary:        OSD skin plugin for VDR

Group:          Applications/Multimedia
License:        GPL
URL:            http://linux.kompiliert.net/index.php?view=text2skin
#Source0:        http://linux.kompiliert.net/files/%{name}-%{version}.tgz
Source0:        http://linux.kompiliert.net/contrib/%{name}-%{version}cvs-%{cvs}.tgz
Source1:        %{name}.conf
Patch0:         %{name}-1.1cvs-cvsfixes.patch
Patch1:         %{name}-1.1cvs-freetype22.patch
Patch2:         %{name}-1.1cvs-skindir.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if 0%{?_with_imagemagick:1}
BuildRequires:  ImageMagick-c++-devel
%else
BuildRequires:  imlib2-devel
%endif
BuildRequires:  freetype-devel
BuildRequires:  vdr-devel >= 1.3.47
BuildRequires:  sed >= 3.95
BuildRequires:  which
Requires:       vdr(abi) = %{apiver}

%description
This plugin is designed to load and interpret a set of files
describing the layout of VDR's on screen display and to make this
"skin" available to VDR via Setup -> OSD in the main menu.  Of course
it is possible to load more than one text-based skin this way and to
choose between them while running VDR.  All skins may be themeable
(you can create your own color-theme) and translateable as the author
of the skin wishes.


%prep
%setup -q -c
cd text2skin
%patch0 -p0
%patch1 -p0
sed -e 's|/usr/share/vdr/|%{datadir}/|' %{PATCH2} | patch -p1
find . -depth -type d -name CVS | xargs rm -r
for f in HISTORY README.de Docs/*.txt ; do
    iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f
done
chmod -x contrib/*.pl
sed -i -e /strip/d -e /O2/d Makefile
sed -i -e '/^DVBDIR/d' -e 's|-I$(DVBDIR)\(/linux\)\?/include||g' Makefile
sed -i -e s/VDRVERSION/APIVERSION/g Makefile
cd ..


%build
opts=
%if 0%{!?_with_imagemagick:1}
opts="HAVE_IMLIB2=1 HAVE_IMAGEMAGICK="
%endif
make -C text2skin %{?_smp_mflags} $opts LIBDIR=. VDRDIR=%{_libdir}/vdr all


%install
rm -rf $RPM_BUILD_ROOT
cd text2skin
install -dm 755 $RPM_BUILD_ROOT%{plugindir}
install -pm 755 libvdr-%{pname}.so.%{apiver} $RPM_BUILD_ROOT%{plugindir}
install -Dpm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
cd ..
install -dm 755 $RPM_BUILD_ROOT%{datadir}/text2skin/fonts


%clean
rm -rf $RPM_BUILD_ROOT


%pre
if [ $1 -gt 1 -a -d %{configdir}/plugins/text2skin ] ; then
    # Migrate skins (can't overwrite a dir with a symlink)
    mkdir -p %{datadir}/text2skin && \
    cp -a %{configdir}/plugins/text2skin/* %{datadir}/text2skin || :
    rm -rf %{configdir}/plugins/text2skin
fi


%files
%defattr(-,root,root,-)
%doc text2skin/CONTRIBUTORS text2skin/COPYING text2skin/HISTORY
%doc text2skin/README text2skin/Docs/*.txt text2skin/contrib/skin_to_10.pl
%lang(de) %doc text2skin/README.de
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%{plugindir}/libvdr-%{pname}.so.%{apiver}
%{datadir}/text2skin/


%changelog
* Sun Apr  8 2007 Ville Skyttä <ville.skytta at iki.fi> - 1.1-18.20051217cvs
- Grab potential XML parse buffer overflow fix from upstream CVS.

* Sun Nov 19 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.1-16.20051217cvs
- Migrate real skins directory to /usr/share/vdr/text2skin.
- Patch for freetype 2.2 compatibility.

* Sat Nov  4 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.1-15.20051217
- Build with imlib2 instead of imagemagick by default due to #212478.
- Build for VDR 1.4.4.

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 1.1-14
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Sat Sep 23 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.1-13.20051217
- Rebuild for VDR 1.4.3.

* Sun Aug  6 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.1-12.20051217
- Rebuild for VDR 1.4.1-3.

* Sun Jun 11 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.1-11.20051217
- Rebuild for VDR 1.4.1.

* Sun Apr 30 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.1-10.20051217
- Rebuild for VDR 1.4.0.
