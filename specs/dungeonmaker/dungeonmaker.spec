# $Id$
# Authority: dries
# Upstream: Aaron Dalton <noraa$snotlad,ac>

Summary: Library which grows dungeons
Name: dungeonmaker
Version: 2.03
Release: 1.2%{?dist}
License: GPL
Group: Development/Libraries
URL: http://dungeonmaker.sourceforge.net/

Source: http://dl.sf.net/dungeonmaker/dungeonmaker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
Dungeonmaker creates labyrinths and dungeons using artificial life methods.

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
%doc README.txt VERSION
%{_bindir}/dungeonmaker
%{_datadir}/dungeonmaker/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.03-1.2
- Rebuild for Fedora Core 5.

* Sun Dec 04 2005 Dries Verachtert <dries@ulyssis.org> - 2.03-1
- Updated to release 2.03.

* Sun Nov 27 2005 Dries Verachtert <dries@ulyssis.org> - 1.01-2
- Added the designs.

* Tue Nov 22 2005 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Updated to release 1.01.

* Wed Nov 16 2005 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Initial package.
