# $Id$
# Authority: dries
# Upstream: Aaron Dalton <noraa$snotlad,ac>

Summary: Library which grows dungeons
Name: dungeonmaker
Version: 1.01
Release: 2
License: GPL
Group: Development/Libraries
URL: http://dungeonmakerlib.sourceforge.net/

Source: http://dl.sf.net/dungeonmakerlib/dungeonmaker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
DungeonMaker-Lib is a fork of the project DungeonMaker, which has been 
abandoned. A fork was chosen as changes needed to be made to the original 
code to more easily accommodate scripting front-ends. The code forks from 
their 2.02 release. This library "grows" dungeons using artificial life 
algorithms for use in isometric games.

%prep
%setup -n dungeonmaker-%{version}

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D dungeonmaker %{buildroot}%{_bindir}/dungeonmaker
%{__install} -d %{buildroot}%{_datadir}/dungeonmaker
%{__install} design* %{buildroot}%{_datadir}/dungeonmaker/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README VERSION
%{_bindir}/dungeonmaker
%{_datadir}/dungeonmaker/

%changelog
* Sun Nov 27 2005 Dries Verachtert <dries@ulyssis.org> - 1.01-2
- Added the designs.

* Tue Nov 22 2005 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Updated to release 1.01.

* Wed Nov 16 2005 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Initial package.
