# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?el5: %define _with_apr1 1}
%{?el5: %define _with_apu1 1}

%define desktop_vendor rpmforge

Summary: Graphical front-end for the Subversion concurrent versioning system.
Name: rapidsvn
Version: 0.9.6
Release: 2
License: BSD
Group: Development/Tools
URL: http://rapidsvn.tigris.org/

Source: http://www.rapidsvn.org/download/release/%{version}/rapidsvn-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: apr-devel, apr-util-devel, neon-devel, gcc-c++
BuildRequires: autoconf >= 2.53, libtool >= 1.4.2
BuildRequires: docbook-style-xsl >= 1.58.1, doxygen, libxslt >= 1.0.27
BuildRequires: subversion-devel >= 1.0.0
BuildRequires: wxGTK-devel >= 2.4.2
BuildRequires: desktop-file-utils
# for /usr/bin/convert:
BuildRequires: ImageMagick
Requires: subversion

%description
Subversion does the same thing CVS does (Concurrent Versioning System) but has
major enhancements compared to CVS.

This is a graphical front-end for Subversion.

%prep
%setup

%{__cat} <<EOF >rapidsvn.desktop
[Desktop Entry]
Name=RapidSVN Subversion Client
Comment=Manage SVN repositories
Icon=rapidsvn.png
Exec=rapidsvn
Terminal=false
Type=Application
Categories=Application;Development;
EOF

%build
export CPPFLAGS="-I/usr/include/subversion-1"
%configure \
    --disable-no-exceptions \
    --with-docbook-xsl="%{_datadir}/sgml/docbook/xsl-stylesheets" \
    --with-svn-lib="%{_libdir}" \
%{?_with_apr1:--with-apr-config="%{_bindir}/apr-1-config"} \
%{?_with_apu1:--with-apu-config="%{_bindir}/apu-1-config"}
#    --with-svn-include="%{_includedir}/subversion-1" \
#    --with-wx-config="%{_bindir}/wxgtk-2.4-config" \
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

convert src/res/svn.ico rapidsvn.png
%{__install} -Dp -m0644 rapidsvn.png.0 %{buildroot}%{_datadir}/pixmaps/rapidsvn.png || :
%{__install} -Dp -m0644 rapidsvn-0.png %{buildroot}%{_datadir}/pixmaps/rapidsvn.png || :

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
    --add-category X-Red-Hat-Base              \
    --dir %{buildroot}%{_datadir}/applications \
    rapidsvn.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
#doc %{_mandir}/man1/rapidsvn.1*
%{_bindir}/rapidsvn
%{_datadir}/applications/%{desktop_vendor}-rapidsvn.desktop
%{_datadir}/pixmaps/rapidsvn.png
%{_includedir}/svncpp/
%{_libdir}/libsvncpp.so*
%exclude %{_libdir}/libsvncpp.a
%exclude %{_libdir}/libsvncpp.la

%changelog
* Wed Sep 17 2008 Dag Wieers <dag@wieers.com> - 0.9.6-2
- Rebuild against wxGTK 2.8.8.

* Wed Jun 04 2008 Dag Wieers <dag@wieers.com> - 0.9.6-1
- Updated to release 0.9.6.

* Mon Dec 11 2006 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Updated to release 0.9.4.

* Tue Oct 10 2006 Dag Wieers <dag@wieers.com> - 0.7.2-2
- Fixed group name.

* Sat Apr 09 2005 Dag Wieers <dag@wieers.com> - 0.7.2-1
- Fix for change in ImageMagick 6.2's convert. (Thomas Zehetbauer)

* Tue Jan 04 2005 Dag Wieers <dag@wieers.com> - 0.7.2-1
- Initial package. (using DAR)
