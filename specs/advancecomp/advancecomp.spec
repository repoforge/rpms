# $Id: advancecomp.spec,v 1.1 2004/02/26 10:51:55 thias Exp $

Summary: Recompression utilities for .PNG, .MNG and .ZIP files.
Name: advancecomp
Version: 1.7
Release: 2.fr
License: GPL
Group: Applications/Emulators
Source: http://dl.sf.net/advancemame/%{name}-%{version}.tar.gz
URL: http://advancemame.sf.net/
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: gcc-c++, zlib-devel

%description
AdvanceCOMP is a set of recompression utilities for .PNG, .MNG and .ZIP files.
The main features are :
* Recompress ZIP, PNG and MNG files using the Deflate 7-Zip implementation.
* Recompress MNG files using Delta and Move optimization. 

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING HISTORY README
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Mon Nov  3 2003 Matthias Saou <http://freshrpms.net/> 1.7-2.fr
- Rebuild for Fedora Core 1.
- Added missing build dependencies, thanks to mach.

* Tue Aug 26 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.7.

* Thu May 22 2003 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

