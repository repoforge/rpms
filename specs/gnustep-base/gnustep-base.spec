# $Id$

# Authority: dries

# NeedsCleanup

%define	_name		gnustep-base
%define	_version	1.8.0
%define _release	4.dries


Summary: GNUstep base
Summary(nl): GNUstep base

BuildRoot:	%{_tmppath}/%{name}-root
Name:		%{_name}
License: 	GPL
Version:	%{_version}
Release:	%{_release}
Group: 		Development/Libraries

URL: http://www.gnustep.org
Source0: ftp://ftp.gnustep.org/pub/gnustep/core/gnustep-base-1.8.0.tar.gz
BuildRequires: /usr/GNUstep/System/Library/Makefiles/GNUstep.sh, diffutils, openssl-devel, gcc-objc, ffcall-devel, gnustep-make, gcc
Requires: ffcall

%description
todo

%description -l nl
todo

%prep
rm -rf $RPM_BUILD_ROOT
%setup
%build
rm -f config.cache
. /usr/GNUstep/System/Library/Makefiles/GNUstep.sh
./configure
make

%install
. /usr/GNUstep/System/Library/Makefiles/GNUstep.sh
mkdir -p ${RPM_BUILD_ROOT}
make install INSTALL_ROOT_DIR=${RPM_BUILD_ROOT} GNUSTEP_INSTALLATION_DIR=${RPM_BUILD_ROOT}/usr/GNUstep/
chmod -s-t ${RPM_BUILD_ROOT}/usr/GNUstep/Tools/gdomap

%clean
# rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
/usr/GNUstep/Library/DTDs/*
/usr/GNUstep/Library/DocTemplates/*
/usr/GNUstep/Library/Documentation/*
/usr/GNUstep/Library/Headers/*
/usr/GNUstep/Library/Libraries/*
/usr/GNUstep/System/Library/Makefiles/Additional/base.make
/usr/GNUstep/Tools/*
/usr/GNUstep/Library/Bundles/SSL.bundle/Resources/Info-gnustep.plist
/usr/GNUstep/Library/Bundles/SSL.bundle/SSL
/usr/GNUstep/Library/Bundles/SSL.bundle/stamp.make

%changelog
* Thu Dec 11 2003 Dries Verachtert <dries@ulyssis.org> 1.8.0.4.dries
- added some BuildRequires
- removed the setuid of gdomap

* Sun Nov 30 2003 Dries Verachtert <dries@ulyssis.org> 1.8.0-3.dries
- cleanup of spec file

* Tue Nov 11 2003 Dries Verachtert <dries@ulyssis.org> 1.8.0-2.dries
- fixed the make install

* Mon Nov 10 2003 Dries Verachtert <dries@ulyssis.org> 1.8.0-1.dries
- first packaging for Fedora Core 1
