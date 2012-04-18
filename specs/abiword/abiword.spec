# $Id$
# Authority: dag

%define desktop_vendor rpmforge

%{?el5:%define _without_popt_devel 1}
%{?el4:%define _without_popt_devel 1}
%{?el3:%define _without_popt_devel 1}
%{?el2:%define _without_popt_devel 1}

Summary: The AbiWord word processor
Name: abiword
Epoch: 1
Version: 2.8.6
Release: 1%{?dist}
License: GPLv2+
Group: Applications/Editors
URL: http://www.abisource.com/

Source0: http://abisource.com/downloads/abiword/%{version}/source/abiword-%{version}.tar.gz
Source1: http://abisource.com/downloads/abiword/%{version}/source/abiword-docs-%{version}.tar.gz
Source11: abiword.mime
Source12: abiword.keys
Source13: abiword.xml
Patch0: abiword-2.6.0-windowshelppaths.patch
Patch1: abiword-2.8.3-desktop.patch
Patch2: abiword-2.6.0-boolean.patch
Patch104: abiword-2.8.6-no-undefined.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: aiksaurus-devel
#BuildRequires: aiksaurus-gtk-devel
#BuildRequires: asio-devel
BuildRequires: autoconf
BuildRequires: bison
BuildRequires: boost-devel
BuildRequires: bzip2-devel
BuildRequires: dbus-glib-devel >= 0.70
BuildRequires: desktop-file-utils
BuildRequires: enchant-devel
BuildRequires: flex
BuildRequires: fribidi-devel
#BuildRequires: gtkmathview-devel >= 0.7.5
BuildRequires: gtk2-devel
BuildRequires: libgsf-devel
BuildRequires: libpng-devel
BuildRequires: librsvg2-devel
BuildRequires: libsoup-devel
BuildRequires: libtool
BuildRequires: libwmf-devel
#BuildRequires: libwpd-devel >= 0.9.0
BuildRequires: libwpg-devel
#BuildRequires: link-grammar-devel >= 4.2.2
BuildRequires: loudmouth-devel
#BuildRequires: ots-devel >= 0.4.2
BuildRequires: poppler-devel >= 0.4.0
%{!?_without_popt_devel:BuildRequires: popt-devel}
BuildRequires: readline-devel
BuildRequires: t1lib-devel
BuildRequires: wv-devel
BuildRequires: zlib-devel
Requires: libabiword = %{epoch}:%{version}-%{release}

%description
AbiWord is a cross-platform Open Source word processor. It is full-featured,
while still remaining lean.

%package -n libabiword
Summary: Library for developing applications based on AbiWord's core
Group: System Environment/Libraries

%description -n libabiword
Library for developing applications based on AbiWord's core.

%package -n libabiword-devel
Summary: Files for developing with libabiword
Group: Development/Libraries
Requires: libabiword = %{epoch}:%{version}-%{release}

%description -n libabiword-devel
Includes and definitions for developing with libabiword.

%prep
# setup abiword
%setup

# patch abiword
%patch1 -p1 -b .desktop
%patch2 -p1 -b .boolean
%patch104 -p1 -b .no-undefined

# setup abiword documentation
%setup -T -b 1 -n abiword-docs-%{version}
%patch0 -p1 -b .windowshelppaths

%build
# build libabiword and abiword
cd %{_builddir}/abiword-%{version}/
# we need to update the generated configuration files because of patch104
autoreconf --force --install
%configure \
    --disable-static \
    --enable-clipart \
    --enable-dynamic \
    --enable-plugins \
    --enable-templates
### Disable wordperfect since EL5 and EL6 ship with old libwpd
#    --enable-wordperfect="no"
%{__make} %{?_smp_mflags} V=1

# build the documentation
cd %{_builddir}/abiword-docs-%{version}/
ABI_DOC_PROG="$(pwd)/../abiword-%{version}/src/abiword" ./make-html.sh

%install

# install abiword
cd %{_builddir}/abiword-%{version}/
%{__make} install DESTDIR="%{buildroot}"

# install the documentation
cd %{_builddir}/abiword-docs-%{version}/
%{__install} -d -m0755 %{buildroot}%{_datadir}/abiword-2.8/AbiWord/help/
%{__cp} -av help/* %{buildroot}%{_datadir}/abiword-2.8/AbiWord/help/
# some of the help dirs have bad perms (#109261)
find %{buildroot}%{_datadir}/abiword-2.8/AbiWord/help/ -type d -exec chmod -c o+rx {} \;

# finish up
%{__install} -d -m0755 %{buildroot}%{_datadir}/pixmaps/
%{__cp} -v %{_builddir}/abiword-%{version}/abiword_48.png %{buildroot}%{_datadir}/pixmaps/abiword_48.png

#cd %{_builddir}/abiword-%{version}/
#%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
#desktop-file-install \
#    --vendor %{desktop_vendor} \
#    --add-category Applications \
#    --add-category Office \
#    --dir %{buildroot}%{_datadir}/applications \
#    ./abiword.desktop
#%{__rm} -f %{buildroot}/%{_datadir}/applications/abiword.desktop

%{__install} -Dp -m0644 %{SOURCE11} %{buildroot}%{_datadir}/mime-info/abiword.mime
%{__install} -Dp -m0644 %{SOURCE12} %{buildroot}%{_datadir}/mime-info/abiword.keys
%{__install} -Dp -m0644 %{SOURCE13} %{buildroot}%{_datadir}/mime/packages/abiword.xml

%clean
%{__rm} -rf %{buildroot}

%post
update-mime-database %{_datadir}/mime &>/dev/null || :
update-desktop-database %{_datadir}/applications &>/dev/null || :

%postun
update-mime-database %{_datadir}/mime &>/dev/null || :
update-desktop-database %{_datadir}/applications &>/dev/null || :

%files
%defattr(-, root, root, 0755)
#%doc %{_builddir}/abiword-%{version}/AUTHORS
#%doc %{_builddir}/abiword-%{version}/ChangeLog
#%doc %{_builddir}/abiword-%{version}/COPYING
#%doc %{_builddir}/abiword-%{version}/COPYRIGHT.TXT
#%doc %{_builddir}/abiword-%{version}/NEWS
#%doc %{_builddir}/abiword-%{version}/README
%doc %{_mandir}/man1/abiword.1*
%{_bindir}/abiword
%{_datadir}/applications/*
%{_datadir}/icons/*.png
%{_datadir}/mime-info/abiword.keys
%{_datadir}/mime-info/abiword.mime
%{_datadir}/mime/packages/abiword.xml
%{_datadir}/pixmaps/*.png
# Abiword help
%dir %{_datadir}/abiword-2.8/
%{_datadir}/abiword-2.8/AbiWord/

%files -n libabiword
#%doc %{_builddir}/abiword-%{version}/AUTHORS
#%doc %{_builddir}/abiword-%{version}/ChangeLog
#%doc %{_builddir}/abiword-%{version}/COPYING
#%doc %{_builddir}/abiword-%{version}/COPYRIGHT.TXT
#%doc %{_builddir}/abiword-%{version}/NEWS
#%doc %{_builddir}/abiword-%{version}/README
%{_datadir}/abiword-2.8/
%{_libdir}/libabiword-2.8.so
%{_libdir}/abiword-2.8/
# Abiword help - included in GUI app
%exclude %{_datadir}/abiword-2.8/AbiWord/
%exclude %{_libdir}/abiword-2.8/plugins/*.la
%exclude %{_libdir}/libabiword-2.8.la

%files -n libabiword-devel
%{_includedir}/abiword-2.8/
%{_libdir}/pkgconfig/abiword-2.8.pc

%changelog
* Sun Feb 12 2012 Dag Wieers <dag@wieers.com> - 2.8.6-1
- Initial package. (based on fedora)
