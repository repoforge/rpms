# $Id: _template.spec 471 2004-05-03 19:42:19Z dag $
# Authority: dag
# Upstream: Hisham Muhammad <lode@gobolinux.org>
# Upstream: <htop-general@lists.sf.net>

Summary: Interactive process viewer
Name: htop
Version: 0.2
Release: 1
License: GPL
Group: Applications/System
URL: http://htop.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/htop/htop-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel

%description
htop is an interactive process viewer for Linux.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#makeinstall
%{__install} -D -m0755 htop %{buildroot}%{_bindir}/htop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING README
%{_bindir}/*

%changelog
* Fri May 14 2004 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
