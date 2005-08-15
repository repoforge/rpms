# $Id$
# Authority: dag
# Upstream: Michel Van den Bergh <michel,vandenbergh$uhasselt,be>

Summary: Rush Hour game
Name: pytraffic
Version: 2.5
Release: 1
License: GPL
Group: Amusements/Games
URL: http://alpha.uhasselt.be/Research/Algebra/Members/pytraffic/

Source: http://alpha.uhasselt.be/Research/Algebra/Members/pytraffic/pytraffic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: noarch
BuildRequires: python-devel >= 2.2
Requires: python >= 2.2 , python-game >= 1.6, pygtk2 >= 2.4
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
%{__python} setup.py install --root="%{buildroot}" --prefix=%{_prefix}

### FIXME: Remove unnecessary files. (Please fix upstream)
%{__rm} -rf %{buildroot}%{_datadir}/pytraffic*/{AUTHORS,CHANGELOG,COPYING,INSTALL,README,DOCS/}

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGELOG COPYING INSTALL README
%doc DOCS/*.htm DOCS/*.png
%{_datadir}/pytraffic*/
%{_bindir}/pytraffic
%{_datadir}/applications/pytraffic.desktop

%changelog
* Tue Aug 09 2005 Dag Wieers <dag@wieers.com> - 2.5-1
- Initial package. (using DAR)
