# $Id$
# Authority: dries

Summary: GNUstep base library package
Name: gnustep-base
Version: 1.11.2
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://www.gnustep.org/

Source: http://ftp.gnustep.org/pub/gnustep/core/gnustep-base-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: /usr/GNUstep/System/Library/Makefiles/GNUstep.sh
BuildRequires: diffutils, openssl-devel, gcc-objc, ffcall-devel
BuildRequires: gnustep-make, libxml2-devel, gmp-devel
Requires: ffcall

%description
The GNUstep Base Library is a library of general-purpose,
non-graphical Objective C objects.  For example, it includes classes
for strings, object collections, byte streams, typed coders,
invocations, notifications, notification dispatchers, moments in time,
network ports, remote object messaging support (distributed objects),
and event loops.

%prep
%setup

%build
source /usr/GNUstep/System/Library/Makefiles/GNUstep.sh
%configure \
	--prefix="%{_prefix}/GNUstep"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source /usr/GNUstep/System/Library/Makefiles/GNUstep.sh
#%{__install} -d -m0755 %{buildroot}
%makeinstall \
	INSTALL_ROOT_DIR="%{buildroot}" \
	GNUSTEP_INSTALLATION_DIR="%{buildroot}%{_prefix}/GNUstep"
chmod -s-t %{buildroot}%{_prefix}/GNUstep/Tools/gdomap

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_prefix}/GNUstep/

%changelog
* Sun Dec 25 2005 Dries Verachtert <dries@ulyssis.org> - 1.11.2-1
- Updated to release 1.11.2.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 1.11.1-1
- Updated to release 1.11.1.

* Sun Aug 07 2005 Dries Verachtert <dries@ulyssis.org> 1.11.0-1
- Update to version 1.11.0.

* Mon Nov 08 2004 Dries Verachtert <dries@ulyssis.org> 1.10.1-1
- Update to version 1.10.1.

* Sat Oct 02 2004 Dries Verachtert <dries@ulyssis.org> 1.10.0-1
- Update to version 1.10.0.

* Mon Jun 14 2004 Dries Verachtert <dries@ulyssis.org> 1.9.2-1
- update to 1.9.2

* Thu Jun 10 2004 Dag Wieers <dag@wieers.com> - 1.9.1-1
- Updated to release 1.9.1.
- Cosmetic cleanup.

* Thu Dec 11 2003 Dries Verachtert <dries@ulyssis.org> 1.8.0-4
- added some BuildRequires
- removed the setuid of gdomap

* Sun Nov 30 2003 Dries Verachtert <dries@ulyssis.org> 1.8.0-3
- cleanup of spec file

* Tue Nov 11 2003 Dries Verachtert <dries@ulyssis.org> 1.8.0-2
- fixed the make install

* Mon Nov 10 2003 Dries Verachtert <dries@ulyssis.org> 1.8.0-1
- first packaging for Fedora Core 1
