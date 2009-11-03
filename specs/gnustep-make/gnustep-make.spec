# $Id$
# Authority: dries

Summary: GNUstep make
Name: gnustep-make
Version: 1.11.2
Release: 1.2%{?dist}
License: GPL
Group: Development/Libraries
URL: http://www.gnustep.org

Source: http://ftp.gnustep.org/pub/gnustep/core/gnustep-make-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This package contains the basic scripts, makefiles and directory layout
needed to run and compile any GNUstep software.

%prep
%setup

%{__cat} <<EOF >gnustep.sh
#!/bin/bash
source "%{_prefix}/GNUstep/System/Library/Makefiles/GNUstep.sh"
EOF

%{__cat} <<EOF >gnustep.csh
#!/bin/csh
source "%{_prefix}/GNUstep/System/Library/Makefiles/GNUstep.csh"
EOF


%build
%configure \
	--prefix="%{_prefix}/GNUstep" \
	--enable-import
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	special_prefix="%{buildroot}"

%{__install} -Dp -m0755 gnustep.sh %{buildroot}%{_sysconfdir}/profile.d/gnustep.sh
%{__install} -Dp -m0755 gnustep.csh %{buildroot}%{_sysconfdir}/profile.d/gnustep.csh

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ANNOUNCE COPYING FAQ GNUstep-HOWTO NEWS README
%config %{_sysconfdir}/profile.d/*
%{_prefix}/GNUstep/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.11.2-1.2
- Rebuild for Fedora Core 5.

* Sun Dec 25 2005 Dries Verachtert <dries@ulyssis.org> - 1.11.2-1
- Updated to release 1.11.2.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 1.11.1-1
- Updated to release 1.11.1.

* Sun Aug 07 2005 Dries Verachtert <dries@ulyssis.org> 1.11.0-1
- Updated to version 1.11.0.

* Sat Oct 02 2004 Dries Verachtert <dries@ulyssis.org> 1.10.0-1
- Updated to version 1.10.0.

* Mon Jun 14 2004 Dries Verachtert <dries@ulyssis.org> 1.9.2-1
- Updated to release 1.9.2.

* Thu Jun 10 2004 Dag Wieers <dag@wieers.com> - 1.9.1-1
- Updated to release 1.9.1.
- Cosmetic cleanup.

* Thu Dec 11 2003 Dries Verachtert <dries@ulyssis.org> 1.8.0-4
- added some BuildRequires

* Sun Nov 30 2003 Dries Verachtert <dries@ulyssis.org> 1.8.0-3
- specfile cleanup

* Mon Nov 10 2003 Dries Verachtert <dries@ulyssis.org> 1.8.0-2
- further packaging
- --enable-import added

* Sun Nov 9 2003 Dries Verachtert <dries@ulyssis.org> 1.8.0-1
- first packaging for Fedora Core 1
