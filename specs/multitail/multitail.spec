# $Id$

# Authority: dries

Summary: View one or multiple files like tail but with multiple windows.
Summary(nl): Bekijk 1 of meerdere bestanden zoals met tail maar met meerdere vensters.
Name: multitail
Version: 3.0.3
Release: 1
License: GPL
Group: Applications/Text
URL: http://www.vanheusden.com/multitail/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.vanheusden.com/multitail/%{name}-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc, make, ncurses-devel
Requires: ncurses

#(d) primscreenshot: http://www.vanheusden.com/multitail/multitail.png

%description
MultiTail lets you view one or multiple files like the original tail
program. The difference is that it creates multiple windows on your console
(with ncurses). Merging of 2 or even more logfiles is possible. It can also
use colors while displaying the logfiles (through regular expressions), for
faster recognition of what is important and what not. It can also filter
lines (again with regular expressions). It has interactive menus for editing
given regular expressions and deleting and adding windows.

%description -l nl
Multitail laat toe om 1 of meerdere bestanden te bekijken zoals met het
originele tail programma. Het toont meerdere vensters in console met
ncurses. Het samenvoegen van 2 of meerdere logbestanden is mogelijk. Het kan
ook kleuren gebruiken (met reguliere expressies) om sneller de belangrijke
stukken te kunnen vinden. Het kan ook lijnen filteren met reguliere
expressies en het heeft interactieve menus om deze reguliere expressies te
wijzigen en om vensters toe te voegen en te verwijderen.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
%{__make} %{?_smp_mflags}

%install
export DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man1
mkdir -p $RPM_BUILD_ROOT/etc
make install

%files
%defattr(-,root,root,0755)
%doc readme.txt
%config(noreplace) %{_sysconfdir}/multitail.conf
%{_bindir}/multitail
/usr/share/man/man1/multitail.1.gz

%changelog
* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 3.0.3-1
- cleanup of spec file
- update to 3.0.3

* Sat Dec 13 2003 Dries Verachtert <dries@ulyssis.org> 3.0.0-1
- first packaging for Fedora Core 1
