# $Id: advancescan.spec,v 1.1 2004/02/26 10:51:55 thias Exp $

Summary: Command line rom manager for MAME, MESS and Raine.
Name: advancescan
Version: 1.7
Release: 2.fr
License: GPL
Group: Applications/Emulators
Source: http://prdownloads.sourceforge.net/advancemame/%{name}-%{version}.tar.gz
URL: http://advancemame.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-root
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
%doc AUTHORS COPYING HISTORY README advscan.rc.linux
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Sun Nov  2 2003 Matthias Saou <http://freshrpms.net/> 1.7-2.fr
- Rebuild for Fedora Core 1.
- Added missing build dependencies.

* Tue Aug 26 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.7.

* Thu May 22 2003 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

