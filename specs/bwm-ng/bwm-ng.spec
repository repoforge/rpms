# $Id$
# Authority: dag
# Upstream: Volker Gropp <gropp_v$informatik.haw-hamburg.de>

Summary: Curses based bandwidth monitor
Name: bwm-ng
Version: 0.5
Release: 1
License: GPL
Group: Applications/Internet
URL: http://users.informatik.haw-hamburg.de/~gropp_v/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://freshmeat.net/redir/bwm-ng/52961/url_tgz/bwm-ng-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel

%description
A small and simple curses Bandwidth Monitor.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} install \
#	DESTDIR="%{buildroot}"
%{__install} -D -m0755 src/bwm-ng %{buildroot}%{_bindir}/bwm-ng
%{__install} -D -m0644 bwm-ng.1 %{buildroot}%{_mandir}/man1/bwm-ng.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS changelog README bwm-ng.conf-example
%doc %{_mandir}/man1/bwm-ng.1*
%{_bindir}/bwm-ng

%changelog
* Tue Feb 22 2005 Dag Wieers <dag@wieers.com> - 0.5-1
- Updated to release 0.5.

* Fri Dec 10 2004 Dag Wieers <dag@wieers.com> - 0.3-2
- Fixed Group tag.

* Fri Sep 24 2004 Dag Wieers <dag@wieers.com> - 0.3-1
- Initial package. (using DAR)
