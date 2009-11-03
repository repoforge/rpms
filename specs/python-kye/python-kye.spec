# $Id$
# Authority: dries
# Upstream: Colin Phipps <cph$moria,org,uk>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name kye

Summary: Puzzle game
Name: python-kye
Version: 0.9.3
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://games.moria.org.uk/kye/pygtk

Source: http://games.moria.org.uk/kye/download/kye-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python, python-devel
Requires: python

%description
Kye is a puzzle game which takes ideas from Sokoban and the genre of
falling-rocks puzzle games. However, it includes a wider range of
objects, allowing a larger variety of puzzles to be constructed. It
is a clone of the original, shareware, Kye for Windows, and is
compatible with the large number of existing extra levels designed
for the Windows version of Kye. 

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_bindir}/Kye
%{_bindir}/Kye-edit
%{python_sitelib}/kye/
%{_datadir}/kye/

%changelog
* Mon Feb 12 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.3-1
- Updated to release 0.9.3.

* Mon Nov 13 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.2-1
- Updated to release 0.9.2.

* Fri May 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.9-1
- Updated to release 0.9.

* Sat Apr 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Updated to release 0.8.

* Fri Apr 07 2006 Dries Verachtert <dries@ulyssis.org> - 0.7-1
- Updated to release 0.7.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.6-1
- Updated to release 0.6.

* Mon Jan 09 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.0-1
- Updated to release 0.5.0.

* Fri Dec 23 2005 Dries Verachtert <dries@ulyssis.org> - 0.4.0-1
- Initial package.
