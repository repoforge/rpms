# $Id$
# Authority: dag
# Upstream: Volker Gropp <gropp_v$informatik.haw-hamburg.de>

Summary: Curses based bandwidth monitor
Name: bwm-ng
Version: 0.3
Release: 2
License: GPL
Group: Applications/Internet
URL: http://users.informatik.haw-hamburg.de/~gropp_v/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://users.informatik.haw-hamburg.de/~gropp_v/bwm-ng-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel

%description
A small and simple curses Bandwidth Monitor.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 bwm-ng %{buildroot}%{_bindir}/bwm-ng

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/bwm-ng

%changelog
* Fri Dec 10 2004 Dag Wieers <dag@wieers.com> - 0.3-2
- Fixed Group tag.

* Fri Sep 24 2004 Dag Wieers <dag@wieers.com> - 0.3-1
- Initial package. (using DAR)
