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
Version: 2.6.6
Release: 1%{?dist}
License: GPLv2+
Group: Applications/Editors
URL: http://www.abisource.com/

Source0: http://abisource.com/downloads/abiword/%{version}/source/abiword-%{version}.tar.gz
Source1: http://abisource.com/downloads/abiword/%{version}/source/abiword-plugins-%{version}.tar.gz
Source2: http://abisource.com/downloads/abiword/%{version}/source/abiword-extras-%{version}.tar.gz
Source3: http://abisource.com/downloads/abiword/%{version}/source/abiword-docs-%{version}.tar.gz
Source11: abiword.mime
Source12: abiword.keys
Source13: abiword.xml
Patch0: abiword-2.6.0-windowshelppaths.patch
Patch1: abiword-2.6.4-desktop.patch
Patch3: abiword-plugins-2.6.0-boolean.patch
Patch4: abiword-plugins-2.6.0-gcc44.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
BuildRequires: boost-devel
BuildRequires: bzip2-devel
BuildRequires: desktop-file-utils
BuildRequires: enchant-devel
BuildRequires: fribidi-devel
BuildRequires: gtk2-devel
BuildRequires: libglade2-devel
BuildRequires: libgnomeprintui22-devel
BuildRequires: libgnomeui-devel
BuildRequires: libgsf-devel
BuildRequires: libpng-devel
BuildRequires: librsvg2-devel
BuildRequires: libtool
BuildRequires: libwmf-devel
BuildRequires: loudmouth-devel
BuildRequires: poppler-devel >= 0.4.0
BuildRequires: popt
%{!?_without_popt_devel:BuildRequires: popt-devel}
BuildRequires: readline-devel
BuildRequires: t1lib-devel
BuildRequires: wv-devel
BuildRequires: zlib-devel
#Requires: mathml-fonts

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
%setup
%patch1 -p1 -b .desktop

# setup abiword-plugins
%setup -T -b 1 -n abiword-plugins-%{version}
%patch3 -p1 -b .boolean
%patch4 -p0 -b .gcc44

# setup abiword extras
%setup -T -b 2 -n abiword-extras-%{version}

# setup abiword documentation
%setup -T -b 3 -n abiword-docs-%{version}
%patch0 -p1 -b .windowshelppaths

%build
# build libabiword and abiword
cd %{_builddir}/abiword-%{version}
%configure --enable-libabiword
%{__make} %{?_smp_mflags}

# build abiword-plugins
cd %{_builddir}/abiword-plugins-%{version}
export PKG_CONFIG_PATH="%{_builddir}/abiword-%{version}"
CXXFLAGS="-L%{_builddir}/abiword-%{version}/src/wp/main/unix/" %configure --disable-gda --enable-libabiword --with-abiword=%{_builddir}/abiword-%{version}
# Remove libtool predep_objects and postdep_objects wonkiness so that
# building without -nostdlib doesn't include them twice.  Because we
# already link with g++, weird stuff happens if you don't let the
# compiler handle this.
sed 's/^predep_objects=.*/predep_objects=\"\"/' < libtool > libtool.foo
sed 's/^postdep_objects=.*/postdep_objects=\"\"/' < libtool.foo > libtool.foobar
sed 's/-shared -nostdlib/-shared/' < libtool.foobar > libtool
%{__make} %{?_smp_mflags}

# build the extras
cd %{_builddir}/abiword-extras-%{version}
# abiword-extras looks at the abiword-%{version}.pc pkg-config file to get its location info 
# however, that file is not installed yet, so just point to it in the abiword source tree 
export PKG_CONFIG_PATH="%{_builddir}/abiword-%{version}"
%configure
%{__make}

# build the documentation
cd %{_builddir}/abiword-docs-%{version}
ABI_DOC_PROG="$(pwd)/../abiword-%{version}/src/wp/main/unix/abiword" ./make-html.sh

%install
%{__rm} -rf %{buildroot}

# install abiword
cd %{_builddir}/abiword-%{version}/
%{__make} install DESTDIR="%{buildroot}"
# overwrite the static binary with the dynamic one
mv -f %{_builddir}/abiword-%{version}/src/wp/main/unix/abiword-dynamic %{buildroot}%{_bindir}/abiword

# install abiword-plugins
cd %{_builddir}/abiword-plugins-%{version}/
%{__make} install DESTDIR="%{buildroot}"

# install the extras
cd %{_builddir}/abiword-extras-%{version}/
%{__make} install DESTDIR="%{buildroot}"

# install the documentation
cd %{_builddir}/abiword-docs-%{version}/
%{__install} -d -m0755 %{buildroot}%{_datadir}/abiword-2.6/AbiWord/help/
%{__cp} -av help/* %{buildroot}%{_datadir}/abiword-2.6/AbiWord/help/
# some of the help dirs have bad perms (#109261)
find %{buildroot}%{_datadir}/abiword-2.6/AbiWord/help/ -type d -exec chmod -c o+rx {} \;

# finish up
%{__install} -d -m0755 %{buildroot}%{_datadir}/pixmaps/
%{__cp} -v %{_builddir}/abiword-extras-%{version}/icons/abiword_48.png %{buildroot}%{_datadir}/pixmaps/abiword_48.png

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
#%doc %{_builddir}/abiword-%{version}/COPYING
#%doc %{_builddir}/abiword-%{version}/COPYRIGHT.TXT
#%doc %{_builddir}/abiword-%{version}/CREDITS.TXT
#%doc %{_builddir}/abiword-%{version}/README.TXT
#%doc %{_builddir}/abiword-%{version}/docs/
%{_bindir}/abiword
%{_datadir}/applications/abiword.desktop
%{_datadir}/icons/abiword_48.png
%{_datadir}/mime-info/abiword.keys
%{_datadir}/mime-info/abiword.mime
%{_datadir}/mime/packages/abiword.xml
%{_datadir}/pixmaps/abiword_48.png

%files -n libabiword
#%doc %{_builddir}/abiword-%{version}/COPYING
#%doc %{_builddir}/abiword-%{version}/COPYRIGHT.TXT
#%doc %{_builddir}/abiword-%{version}/CREDITS.TXT
#%doc %{_builddir}/abiword-%{version}/README.TXT
#%doc %{_builddir}/abiword-%{version}/docs/
%{_datadir}/abiword-2.6/
%{_libdir}/libabiword-2.6.so
%{_libdir}/abiword-2.6/
%exclude %{_libdir}/abiword-2.6/plugins/*.la
%exclude %{_datadir}/abiword-2.6/dictionary/ispell_dictionary_list.xml

%files -n libabiword-devel
%{_includedir}/abiword-2.6/
%{_libdir}/pkgconfig/abiword-2.6.pc

%changelog
* Sun Feb 12 2012 Dag Wieers <dag@wieers.com> - 2.6.6-1
- Initial package. (based on fedora)
