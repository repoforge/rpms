# $Id: _template.spec 471 2004-05-03 19:42:19Z dag $
# Authority: dag
# Upstream: Dag Wieers <dag@wieers.com>

Summary: Tool to create a local RPM repository from ISO files and RPM packages
Name: yam
Version: 0.3
Release: 1
License: GPL
Group: System Environment/Base
URL: http://dag.wieers.com/home-made/yam/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dag.wieers.com/home-made/yam/yam-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: python

%description
Yam builds a local Apt/Yum RPM repository from local ISO files,
downloaded updates and extra packages from 3rd party repositories.

It can download all updates and extras automatically, creates
the repository structure and meta-data, enables HTTP access to 
the repository and creates a directory-structure for PXE/TFTP.

With yam, you can enable your laptop or a local server to provide
updates for the whole network and provide the proper files to
allow installations via the network.

By default it works out of the box with:

	Fedora Core 1 and 2
	Red Hat Enterprise Linux 2.1 and 3 (WS, ES, AS)
	TaoLinux 1
	CentOS 2.1 and 3
	Red Hat Linux 6.2, 7.3, 8.0 and 9

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/www/yam


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README THANKS TODO
%config(noreplace) %{_sysconfdir}/yam.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/yam.conf
%config %{_initrddir}/yam
%{_bindir}/yam
%{_libdir}/yam/
%dir %{_localstatedir}/www/yam/

%changelog
* Fri May 21 2004 Dag Wieers <dag@wieers.com> - 0.3-1
- Updated to release 0.3.

* Fri May 14 2004 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
