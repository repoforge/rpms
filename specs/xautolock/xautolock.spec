# $Id$
# Authority: dries

Summary: Launches a program when your X session has been idle for some time
Name: xautolock
Version: 2.1
Release: 2
License: GPL
Group: Applications/Internet
URL: http://www.ibiblio.org/pub/Linux/X11/screensavers/

Source: http://www.ibiblio.org/pub/Linux/X11/screensavers/xautolock-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: XFree86-devel

%description
A program that launches a given program when 
your X session has been idle for a given time.

%prep
%setup
xmkmf

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 xautolock %{buildroot}%{_prefix}/usr/X11R6/bin/xautolock
%{__install} -Dp -m0644 xautolock._man %{buildroot}%{_prefix}/X11R6/man/man1/xautolock.1x

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_prefix}/X11R6/man/man1/xautolock.1x.gz
%{_prefix}/X11R6/bin/xautolock

%changelog
* Thu Feb 26 2004 Dries Verachtert <dries@ulyssis.org> 2.1-2
- fixed: man page not installed.
  bug found by Matt Thompson, thanks Matt!

* Wed Feb 25 2004 Dries Verachtert <dries@ulyssis.org> 2.1-1
- first packaging for Fedora Core 1
