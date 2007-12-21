# $Id$
# Authority: dag
# Upstream: Michel Van den Bergh <michel,vandenbergh$uhasselt,be>

Summary: Rush Hour game
Name: pytraffic
Version: 2.5.4
Release: 1
License: GPL
Group: Amusements/Games
URL: http://alpha.uhasselt.be/Research/Algebra/Members/pytraffic/

Source: http://alpha.uhasselt.be/Research/Algebra/Members/pytraffic/pytraffic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: noarch
BuildRequires: python-devel >= 2.2, SDL_mixer-devel, SDL-devel
Requires: python >= 2.2 , pygtk2 >= 2.4
Obsoletes: ttraffic

%description
PyTraffic is a python version of the board game Rush Hour created
by Binary Arts Coporation. The goal is to remove the red car out
of the grid through the slot on the right. To do this you have to
slide the other cars out of the way.

PyTraffic comes with about 19.000 puzzles ranging from intermediate
to expert.

%prep
%setup

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root="%{buildroot}" --prefix="%{_prefix}"

### FIXME: Remove unnecessary files. (Please fix upstream)
%{__rm} -rf %{buildroot}%{_datadir}/pytraffic*/{AUTHORS,CHANGELOG,COPYING,INSTALL,README,DOCS/}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGELOG COPYING INSTALL README
%doc doc/*.htm doc/*.png
%{_bindir}/pytraffic
%{_datadir}/applications/pytraffic.desktop
%{_datadir}/icons/hicolor/*/apps/pytraffic.png
%{_datadir}/pytraffic*/
#%{_libdir}/pytraffic/
%{_prefix}/lib/pytraffic/

%changelog
* Thu Mar 01 2007 Dag Wieers <dag@wieers.com> - 2.5.4-1
- Updated to release 2.5.4.

* Tue Aug 09 2005 Dag Wieers <dag@wieers.com> - 2.5-1
- Initial package. (using DAR)
