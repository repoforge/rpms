# $Id$
# Authority: matthias
# Upstream: <dev@rarlab.com>

Summary: Extract, test and view RAR archives
Name: unrar
Version: 3.3.6
Release: 1
License: Freeware
Group: Applications/Archiving
URL: http://www.rarlab.com/

Source0: http://www.rarlab.com/rar/unrarsrc-%{version}.tar.gz
Source1: unrar.1
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, libstdc++-devel
Requires: libstdc++

%description
The unRAR utility is a freeware program, distributed with source code
and developed for extracting, testing and viewing the contents of
archives created with the RAR archiver version 1.50 and above.

%prep
%setup -n %{name}

%build
%{__make} -f makefile.unix \
	CXXFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -m755 -D unrar %{buildroot}%{_bindir}/unrar
%{__install} -m644 -D %{SOURCE1} %{buildroot}%{_mandir}/man1/unrar.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.txt
%doc %{_mandir}/man1/unrar.1*
%{_bindir}/unrar

%changelog
* Thu Feb 26 2004 Matthias Saou <http://freshrpms.net/> 3.3.6-1.fr
- Update to 3.3.6.

* Mon Jan 19 2004 Matthias Saou <http://freshrpms.net/> 3.3.4-1.fr
- Update to 3.3.4.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 3.2.3-1.fr
- Update to 3.2.3.
- Rebuild for Fedora Core 1.

* Wed May 14 2003 Matthias Saou <http://freshrpms.net/>
- Update to 3.2.1.
- Added missing URL.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to 3.2.0.
- Rebuilt for Red Hat Linux 9.

* Mon Jan 13 2003 Matthias Saou <http://freshrpms.net/>
- Update to 3.1.3.

* Thu Oct 10 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup.

* Sat Oct  5 2002 Ville Skyttä <ville.skytta at iki.fi> 3.00-2cr
- Rebuild for Red Hat 8.0, using the compat GCC.

* Tue Sep 17 2002 Ville Skyttä <ville.skytta at iki.fi> 3.00-1cr
- RedHatified PLD version.

