# $Id$
# Authority: dries

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: MPD (Music Player Daemon) client
Name: sonata
Version: 1.6.2
Release: 1%{?dist}
License: GPL
# GPLv3, but it includes mmkeys which is GPLv2
Group: Applications/Multimedia
URL: http://sonata.berlios.de/

Source: http://download.berlios.de/sonata/sonata-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python
Requires: python

%description
Sonata is a client for the Music Player Damon (MPD), written in pyton and gtk.

%prep
%setup

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
# FIXME: install fails with --skip-build
%{__python} setup.py install -O1 --root="%{buildroot}" --prefix="%{_prefix}"
%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc COPYING README TODO
%doc %{_mandir}/man1/sonata.1*
%{_bindir}/sonata
%{_datadir}/pixmaps/sonata*.png
%{_datadir}/applications/sonata.desktop
%{_datadir}/sonata/
%{python_sitelib}/mmkeys.so
%{python_sitelib}/sonata/
%{python_sitelib}/Sonata-%{version}-*.egg-info

%changelog
* Mon Jun  1 2009 Dries Verachtert <dries@ulyssis.org> - 1.6.2-1
- Initial package.
