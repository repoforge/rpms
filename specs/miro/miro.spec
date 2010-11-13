# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define python_version %(%{__python} -c 'import sys; print sys.version.split(" ")[0]')


%define _with_mozilla 1

%{?el5:%define mozilla xulrunner-devel nspr-devel}
%{?el4:%define mozilla seamonkey-devel}
%{?el3:%define mozilla seamonkey-devel}

%define real_name Miro

Summary: Free and Open Source Internet TV and video player
Name: miro
Version: 1.1
Release: 2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.getmiro.com/

Source: ftp://ftp.osuosl.org/pub/pculture.org/miro/src/Miro-%{version}.tar.gz
Patch0: miro-0.9.9.1-svn.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: boost-devel
%{?_with_mozilla:BuildRequires: %{mozilla}}
BuildRequires: libfame
BuildRequires: pyrex
BuildRequires: python-devel
BuildRequires: xine-lib-devel
Requires: dbus-python
Requires: firefox
Requires: gnome-python2-gtkmozembed
Requires: gnome-python2-gconf
Requires: libfame
Requires: python >= %{python_version}
Requires: python-sqlite2
Requires: xine-lib

Obsoletes: Miro <= %{version}-%{release}
Provides: Miro = %{version}-%{release}

ExclusiveArch: i386 x86_64

%description
Free and Open Source Internet TV and video player.

%prep
%setup -n %{real_name}-%{version}
#patch0 -p0

%build
cd platform/gtk-x11
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
cd platform/gtk-x11
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
cd -
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%post
update-desktop-database %{_datadir}/applications

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc CREDITS LAYOUT license.txt platform/gtk-x11/README
%doc %{_mandir}/man1/miro.1*
%{_bindir}/miro
%{_bindir}/miro.real
%{_datadir}/applications/miro.desktop
%{_datadir}/mime/packages/miro.xml
%{_datadir}/miro/
%{_datadir}/pixmaps/miro-*.png
%{_libexecdir}/xine_extractor
%{python_sitearch}/miro/
%ghost %{python_sitearch}/miro/*.pyo
%ghost %{python_sitearch}/miro/*/*.pyo
%ghost %{python_sitearch}/miro/*/*/*.pyo

%changelog
* Tue Jul 14 2009 Dag Wieers <dag@wieers.com> - 1.1-2
- Rebuild against firefox 3.0.x.

* Mon Feb 04 2008 Dag Wieers <dag@wieers.com> - 1.1-1
- Updated to release 1.1.

* Fri Nov 16 2007 Dag Wieers <dag@wieers.com> - 1.0-1
- Updated to release 1.0.

* Fri Nov 16 2007 Dag Wieers <dag@wieers.com> - 0.9.9.1-1
- Initial package. (using DAR)
