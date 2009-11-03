# $Id$
# Authority: matthias
# Upstream: <advancemame-devel$lists,sourceforge,net>

Summary: Recompression utilities for .PNG, .MNG and .ZIP files
Name: advancecomp
Version: 1.15
Release: 1%{?dist}
License: GPL
Group: Applications/Emulators
URL: http://advancemame.sourceforge.net/
Source: http://dl.sf.net/advancemame/advancecomp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, zlib-devel

%description
AdvanceCOMP is a set of recompression utilities for .PNG, .MNG and .ZIP files.
The main features are :
* Recompress ZIP, PNG and MNG files using the Deflate 7-Zip implementation.
* Recompress MNG files using Delta and Move optimization.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING HISTORY README
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Mon Aug 14 2006 Dag Wieers <dag@wieers.com> - 1.15-1
- Updated to release 1.15.

* Wed Feb 23 2005 Matthias Saou <http://freshrpms.net/> 1.14-1
- Update to 1.14.

* Mon Nov 29 2004 Matthias Saou <http://freshrpms.net/> 1.13-1
- Update to 1.13.

* Tue Nov  2 2004 Matthias Saou <http://freshrpms.net/> 1.12-1
- Update to 1.12.

* Tue Aug 24 2004 Matthias Saou <http://freshrpms.net/> 1.11-1
- Update to 1.11.

* Mon May 17 2004 Matthias Saou <http://freshrpms.net/> 1.10-1
- Update to 1.10.

* Mon Nov  3 2003 Matthias Saou <http://freshrpms.net/> 1.7-2
- Rebuild for Fedora Core 1.
- Added missing build dependencies, thanks to mach.

* Tue Aug 26 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.7.

* Thu May 22 2003 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

