# $Id$

# Authority: dries

Summary: Launches a program when your X session has been idle for some time
Name: xautolock
Version: 2.1
Release: 2
License: GPL
Group: Applications/Internet
URL: http://www.ibiblio.org/pub/Linux/X11/screensavers/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.ibiblio.org/pub/Linux/X11/screensavers/xautolock-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: XFree86-devel

%description
A program that launches a given program when 
your X session has been idle for a given time.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup
xmkmf

%build
%{__make} %{?_smp_mflags}

%install
strip xautolock
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin/
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/man/man1/
%{__install} -v -c   xautolock $RPM_BUILD_ROOT/usr/X11R6/bin/xautolock
%{__install} -v -c -m 0444 xautolock._man $RPM_BUILD_ROOT/usr/X11R6/man/man1/xautolock.1x

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root, 0755)
/usr/X11R6/bin/xautolock
/usr/X11R6/man/man1/xautolock.1x.gz

%changelog
* Thu Feb 26 2004 Dries Verachtert <dries@ulyssis.org> 2.1-2
- fixed: man page not installed.
  bug found by Matt Thompson, thanks Matt!

* Wed Feb 25 2004 Dries Verachtert <dries@ulyssis.org> 2.1-1
- first packaging for Fedora Core 1
