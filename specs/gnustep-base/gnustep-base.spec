# $Id$

# Authority: dries

# NeedsCleanup

Summary: GNUstep base
Summary(nl): GNUstep base
Name: gnustep-base
License: GPL
Version: 1.8.0
Release: 4
Group: Development/Libraries
URL: http://www.gnustep.org/

Source0: ftp://ftp.gnustep.org/pub/gnustep/core/gnustep-base-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: /usr/GNUstep/System/Library/Makefiles/GNUstep.sh, diffutils, openssl-devel, gcc-objc, ffcall-devel, gnustep-make
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
rm -f config.cache
. /usr/GNUstep/System/Library/Makefiles/GNUstep.sh
./configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
. /usr/GNUstep/System/Library/Makefiles/GNUstep.sh
mkdir -p ${RPM_BUILD_ROOT}
make install \
	INSTALL_ROOT_DIR="%{buildroot}" \
	GNUSTEP_INSTALLATION_DIR="%{buildroot}/usr/GNUstep/"
chmod -s-t ${RPM_BUILD_ROOT}/usr/GNUstep/Tools/gdomap

%clean
%{__rm} -rf %{buildroot}

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
* Thu Dec 11 2003 Dries Verachtert <dries@ulyssis.org> 1.8.0.4
- added some BuildRequires
- removed the setuid of gdomap

* Sun Nov 30 2003 Dries Verachtert <dries@ulyssis.org> 1.8.0-3
- cleanup of spec file

* Tue Nov 11 2003 Dries Verachtert <dries@ulyssis.org> 1.8.0-2
- fixed the make install

* Mon Nov 10 2003 Dries Verachtert <dries@ulyssis.org> 1.8.0-1
- first packaging for Fedora Core 1
