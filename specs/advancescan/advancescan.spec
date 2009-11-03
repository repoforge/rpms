# $Id$
# Authority: matthias
# Upstream: <advancemame-devel$lists,sourceforge,net>

Summary: Command line rom manager for MAME, MESS and Raine
Name: advancescan
Version: 1.13
Release: 2%{?dist}
License: GPL
Group: Applications/Emulators
URL: http://advancemame.sourceforge.net/
Source: http://dl.sf.net/advancemame/advancescan-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, zlib-devel

%description
AdvanceSCAN is a command line rom manager for MAME, MESS, AdvanceMAME,
AdvanceMESS and Raine. The main features are :
* Directly read, write zip archives without decompressing and recompressing
  them for the best performance.
* Add, copy, move and rename files in the zip archives. Any rom that you
  have is placed automatically in the correct zip.
* Recognize the text files added by rom sites and delete them.
* Recognize the text files added by the rom dumpers and keep or delete them.
* It's safe. On all the zip operations any file removed or overwritten is
  saved in the `rom_unknown' `sample_unknown' directories and kept for
  future uses. This will prevent any unwanted remove operation.
* Generate differential rom sets.


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
%doc AUTHORS COPYING HISTORY README advscan.rc.linux
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 1.13-2
- Release bump to drop the disttag number in FC5 build.

* Thu Dec  9 2004 Matthias Saou <http://freshrpms.net/> 1.13-1
- Update to 1.13.

* Mon Nov 29 2004 Matthias Saou <http://freshrpms.net/> 1.12-1
- Update to 1.12.

* Fri Sep 24 2004 Dag Wieers <dag@wieers.com> - 1.11-1
- Updated to release 1.11.

* Mon Aug 23 2004 Matthias Saou <http://freshrpms.net/> 1.10-1
- Update to 1.10.

* Mon Jul 26 2004 Matthias Saou <http://freshrpms.net/> 1.9-1
- Update to 1.9.

* Thu Apr 22 2004 Matthias Saou <http://freshrpms.net/> 1.8-1
- Update to 1.8.

* Sun Nov  2 2003 Matthias Saou <http://freshrpms.net/> 1.7-2
- Rebuild for Fedora Core 1.
- Added missing build dependencies.

* Tue Aug 26 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.7.

* Thu May 22 2003 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

