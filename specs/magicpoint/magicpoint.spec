# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}
%{?fedora: %{expand: %%define fc%{fedora} 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

Summary: Presentation software
Name: magicpoint
Version: 1.11b
Release: 1
License: BSD
Group: Applications/Productivity
URL: http://member.wide.ad.jp/wg/mgp/

Source: ftp://sh.wide.ad.jp/WIDE/free-ware/mgp/magicpoint-%{version}.tar.gz
Patch0: magicpoint-1.11b-debian.patch
Patch1: magicpoint-1.11b-64bit.patch
Patch2: magicpoint-1.09a-rpath.patch
Patch3: magicpoint-1.11a-fix-gcc-warnings.patch
Patch4: magicpoint-1.11b-embed.patch
Patch6: magicpoint-1.10a-longline.patch
Patch10: magicpoint-1.10a-fix-usleep.patch
Patch11: magicpoint-1.10a-fix-gcc34.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildPrereq: freetype-devel
BuildRequires: autoconf, automake, libtool, byacc, flex
BuildRequires: libungif-devel, libpng-devel, libmng-devel, imlib-devel
BuildRequires: fontconfig-devel
#Requires: VFlib2 >= 2.25.6-8, VFlib2-conf-ja >= 2.25.6-8
%{!?_without_modxorg:BuildRequires: libXt-devel, libXext-devel, libXft-devel, libXmu-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
Requires: imlib
Obsoletes: mgp <= %{version}-%{release}
Obsoletes: MagicPoint <= %{version}-%{release}
Provides: mgp = %{version}-%{release}
Provides: MagicPoint = %{version}-%{release}

%description
MagicPoint is an X11 based presentation tool. MagicPoint's
presentation files (typically .mgp files) are plain text so you can
create presentation files quickly with your favorite editor.

%prep
%setup
%patch0 -p1
%patch1 -p1 -z .64bit
%patch2 -p1 -b .rpath
%patch3 -p1 -b .warnings
%patch4 -p1 -z .embed
%patch6 -p1 -b .longline
%patch10 -p1 -b .usleep
%patch11 -p1 -b .gcc34

%build
%configure \
	--x-libraries="%{_libdir}/X11" \
	--x-includes="%{_includedir}/X11" \
	--disable-vflib \
	--enable-freetype \
	--enable-freetype-charset16 \
	--enable-gif \
	--enable-imlib \
	--enable-locale \
	--enable-xft2
xmkmf -a
%{__make} %{?_smp_mflags} LIBDIR="%{_datadir}"

%install
%{__rm} -rf %{buildroot}
%{__make} install install.man DESTDIR="%{buildroot}" LIBDIR="%{_datadir}" BINDIR="%{_bindir}" MANDIR="%{_mandir}/man1"
%{__install} -Dp -m0755 contrib/mgp2html.pl %{buildroot}%{_bindir}/mgp2html
%{__install} -Dp -m0755 contrib/mgp2latex.pl %{buildroot}%{_bindir}/mgp2latex

### Clean up docdir
%{__rm} -rf sample/{.cvsignore,Imakefile*,Makefile}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYRIGHT* FAQ README* RELNOTES SYNTAX TODO* USAGE* sample/
%doc %{_mandir}/man1/mgp.1x*
%doc %{_mandir}/man1/mgp2ps.1x*
%doc %{_mandir}/man1/mgpembed.1x*
%doc %{_mandir}/man1/mgpnet.1x*
%doc %{_mandir}/man1/xwintoppm.1x*
%{_bindir}/mgp
%{_bindir}/mgp2html
%{_bindir}/mgp2latex
%{_bindir}/mgp2ps
%{_bindir}/mgpembed
%{_bindir}/mgpnet
%{_bindir}/xwintoppm
%{_datadir}/mgp/

%changelog
* Mon Jan 08 2006 Dag Wieers <dag@wieers.com> - 1.11b-1
- Initial package. (using DAR)
