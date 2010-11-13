# $Id$
# Authority: dag
# Upstream: Michal Suszycki <mike$wizard,ae,krakow,pl>

Summary: Display information about users currently logged on users
Name: whowatch
Version: 1.4
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://wizard.ae.krakow.pl/~mike/

Source: http://wizard.ae.krakow.pl/~mike/download/whowatch-%{version}.tar.gz
Patch0: gcc4-fix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel

%description
Whowatch is an interactive console utility that displays informations about
the users currently logged on to the machine, in real time. Besides standard
information (login, tty, host, user's process) you can see type of login
(ie. ssh, telnet). You can also see selected user's processes tree or all
system processes tree.  In the process tree mode there is ability to send
INT or KILL signal to selected process.

%prep
%setup
%patch0 -p1

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/ \
			%{buildroot}%{_bindir}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING KEYS README TODO
%doc %{_mandir}/man1/whowatch.1*
%{_bindir}/whowatch

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.4-1.2
- Rebuild for Fedora Core 5.

* Fri Nov 05 2004 Dag Wieers <dag@wieers.com> - 1.4-1
- Initial package. (using DAR)
