# $Id: gnustep-make.spec,v 1.1 2004/03/01 15:41:10 driesve Exp $

# Authority: dries

# NeedsCleanup

%define	_name		gnustep-make
%define	_version	1.8.0
%define _release	4.dries

Summary: GNUstep make
Summary(nl): GNUstep make

BuildRoot:	%{_tmppath}/%{name}-root
Name:		%{_name}
License:	GPL
Version:	%{_version}
Release:	%{_release}
Group: Development/Libraries
BuildRequires: gcc, make
URL: http://www.gnustep.org
Source0: ftp://ftp.gnustep.org/pub/gnustep/core/gnustep-make-1.8.0.tar.gz

%description
GNUstep make

%description -l nl
GNUstep make

%prep
rm -rf $RPM_BUILD_ROOT
%setup
%build
rm -f config.cache
./configure --enable-import

sed -i "s/special_prefix =.*/special_prefix= ${RPM_BUILD_ROOT//\//\\/}/g;" GNUmakefile
make

%install
%makeinstall

%clean
# rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc README NEWS ANNOUNCE COPYING FAQ GNUstep-HOWTO
/usr/GNUstep/System/Library/Makefiles/config.guess
/usr/GNUstep/System/Library/Makefiles/config.sub
/usr/GNUstep/System/Library/Makefiles/install-sh
/usr/GNUstep/System/Library/Makefiles/mkinstalldirs
/usr/GNUstep/System/Library/Makefiles/user_home
/usr/GNUstep/System/Library/Makefiles/which_lib
/usr/GNUstep/System/Library/Makefiles/*.template
/usr/GNUstep/System/Library/Makefiles/*.make
/usr/GNUstep/System/Library/Makefiles/*.sh
/usr/GNUstep/System/Library/Makefiles/*.csh
/usr/GNUstep/System/Library/Makefiles/Master/*.make
/usr/GNUstep/System/Library/Makefiles/Instance/*.make
/usr/GNUstep/System/Library/Makefiles/Instance/Shared/*.make
/usr/GNUstep/System/Library/Makefiles/Instance/Documentation/*.make
/usr/GNUstep/System/Tools/debugapp
/usr/GNUstep/System/Tools/openapp
/usr/GNUstep/System/Tools/opentool
/usr/GNUstep/System/share/config.site

%changelog
* Thu Dec 11 2003 Dries Verachtert <dries@ulyssis.org> 1.8.0-4.dries
- added some BuildRequires

* Sun Nov 30 2003 Dries Verachtert <dries@ulyssis.org> 1.8.0-3.dries
- specfile cleanup

* Mon Nov 10 2003 Dries Verachtert <dries@ulyssis.org> 1.8.0-2.dries
- further packaging
- --enable-import added

* Sun Nov 9 2003 Dries Verachtert <dries@ulyssis.org> 1.8.0-1.dries
- first packaging for Fedora Core 1
