# $Id$
# Authority: dag
# Upstream: <glchess-devel$lists,sf,net>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define desktop_vendor rpmforge

Summary: 3D chess interface
Name: glchess
Version: 1.0.2
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://glchess.sourceforge.net/

Source: http://dl.sf.net/glchess/glchess-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: gettext, gtk+-devel >= 1.2.0, python-devel, python
#BuildRequires: gtkglarea

%description
glChess is a 3D OpenGL based chess game that interfaces via the Chess Engine
Communication Protocol (CECP) by Tim Mann. This means it can currently use
Crafty and GNU Chess as AIs. You can also play Human vs. Human, but so far
not over a netwerk (see TODO).

%prep
%setup

%build
%{__make} translations
python setup.py build

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc BUGS ChangeLog COPYING INSTALL README TODO
%{_bindir}/glchess
%{_datadir}/applications/glchess.desktop
%{_datadir}/games/glchess/
%{_datadir}/pixmaps/glchess.svg
%{_datadir}/mime/packages/glchess.xml
%{python_sitelib}/glchess/
%{_datadir}/gconf/schemas/glchess.schemas
%ghost %{python_sitelib}/glchess/*.pyo
%ghost %{python_sitelib}/glchess/*/*.pyo

%changelog
* Sun Feb 11 2007 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2.

* Tue Jan 09 2007 Dries Verachtert <dries@ulyssis.org> - 1.0.1-1
- Updated to release 1.0.1.

* Sun Nov 12 2006 Dag Wieers <dag@wieers.com> - 1.0-1
- Updated to release 1.0.

* Sun Nov 12 2006 Dag Wieers <dag@wieers.com> - 0.9.12-1
- Updated to release 0.9.12.

* Wed Oct 04 2006 Dag Wieers <dag@wieers.com> - 0.9.11-1
- Updated to release 0.9.11.

* Mon Oct 02 2006 Dag Wieers <dag@wieers.com> - 0.9.10-1
- Updated to release 0.9.10.

* Sun Oct 01 2006 Dag Wieers <dag@wieers.com> - 0.9.9-1
- Updated to release 0.9.9.

* Thu Sep 14 2006 Dag Wieers <dag@wieers.com> - 0.9.8-1
- Updated to release 0.9.8.
- Converted to python installation. (Andrew Ziem)

* Sat Apr 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.6-1
- Updated to release 0.9.6.

* Sat Apr 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.0-1
- Updated to release 0.9.0.

* Wed Feb 19 2003 Dag Wieers <dag@wieers.com> - 0.4.7-0
- Initial package. (using DAR)
