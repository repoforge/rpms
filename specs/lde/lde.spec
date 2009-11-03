# $Id$
# Authority: dag
# Upstream: Scott Heavner <scottheavner$users,sf,net>

# Distcc: 0

Summary: Console-based disk editor
Name: lde
Version: 2.6.1
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://lde.sourceforge.net/

Source: http://dl.sf.net/lde/lde-%{version}.tar.gz
#Patch: lde-2.6.0-build.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bison, gpm-devel, ncurses-devel

%description
lde is a disk editor for Linux, originally written to help recover
deleted files. It has a simple ncurses interface that resembles an
old version of Norton Disk Edit for DOS.

%prep
%setup -n %{name}
#patch

### FIXME: Make buildsystem use standard autotools directories (Please fix upstream)
%{__perl} -pi.orig -e 's|(\$\(mandir\))|$1/man8|' macros/Makefile.in

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

### FIXME: Makefile doesn't create target directories (Please fix upstream)
%{__install} -d -m0755 %{buildroot}%{_sbindir} \
			%{buildroot}%{_datadir}/man/man8/

%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/*.tex doc/UNERASE README* src/ChangeLog TODO WARNING
%doc %{_mandir}/man?/*
%{_sbindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.6.1-1.2
- Rebuild for Fedora Core 5.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 2.6.1-1
- Updated to release 2.6.1.

* Fri Apr 17 2004 Dag Wieers <dag@wieers.com> - 2.6.0-1
- Initial package. (using DAR)
