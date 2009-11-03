# $Id$
# Authority: dag
# Upstream: Petr Baudis <pasky@ucw.cz>

Summary: Attach processes running on other terminals
Name: retty
Version: 1.0
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://pasky.or.cz/~pasky/dev/retty/

Source: http://pasky.or.cz/~pasky/dev/retty/retty-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
retty is a tiny tool that lets you attach processes running on other
terminals. So you were running that mutt outside of screen at your
home machine and now wanna check your mail? Attach it with retty,
do whatever you want, detach it again and everything is as it was
before. You don't have to run them all in screen just in case.

Note that the tool is only very lightly tested, so take some care.
Always check first if attaching given application works before you
will do it for real.

We send SIGWINCHs around to make the applications recheck window
dimensions and redraw the screen - if they don't, try pressing Ctrl-L.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 retty %{buildroot}%{_bindir}/retty
%{__install} -Dp -m0644 retty.1 %{buildroot}%{_mandir}/man1/retty.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%doc %{_mandir}/man1/retty.1*
%{_bindir}/retty

%changelog
* Thu Aug 17 2006 Dag Wieers <dag@wieers.com> - 1.0-1
- Updated to release 1.0.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 0.1-1
- Initial package. (using DAR)
