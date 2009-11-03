# $Id$

Summary: Command line tool to test HTTP performance of Web servers and Web applications
Name: wbox
Version: 4
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://hping.org/wbox/

Source: http://hping.org/wbox/wbox-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Wbox is a command line tool to test HTTP performance of Web servers and Web 
applications, to test HTTP compression, to perform stress tests simulating 
multiple HTTP clients, and to test virtual domain configurations before DNS 
propagation. It also implements a configuration-free Web server for file 
sharing.

%prep
%setup -n wbox

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 wbox %{buildroot}%{_bindir}/wbox

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS Changelog README TODO
%{_bindir}/wbox

%changelog
* Mon Jun 11 2007 Laurent Papier <papier[at]tuxfan.net> - 4-1
- created spec file
