# $Id$
# Authority: dries
# Upstream: Max Kellerman <max$duempel,org>

Summary: Proxy server for ultima online
Name: uoproxy
Version: 0.1.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://max.kellermann.name/projects/uoproxy/

Source: http://download.berlios.de/uoproxy/uoproxy-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: which

%description
uoproxy is a proxy server for Ultima Online. It adds features like 
disconnected operation, automatic reconnection, multi-headed gameplay, 
and much more.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D src/uoproxy %{buildroot}%{_bindir}/uoproxy
%{__install} -D conf/uoproxy.conf %{buildroot}%{_sysconfdir}/uoproxy.conf

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README TODO
%config(noreplace) %{_sysconfdir}/uoproxy.conf
%{_bindir}/uoproxy

%changelog
* Tue Dec 27 2005 Dries Verachtert <dries@ulyssis.org> - 0.1.1-1
- Updated to release 0.1.1.

* Thu Dec 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.1.0-1
- Initial package.
