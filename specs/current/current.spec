# $Id$
# Authority: dag

Summary: Server for Red Hat's up2date tools
Name: current
Version: 1.5.11
Release: 1
License: GPL
Group: System Environment/Daemons
URL: http://current.tigris.org/

Source: ftp://ftp.quackmaster.net/current/current-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

BuildArch: noarch
BuildRequires: docbook-style-xsl, docbook-style-dsssl, docbook-dtds
BuildRequires: docbook-utils, docbook-utils-pdf, python-devel >= 2.2
Requires: python >= 2.2, rpm-python >= 4.0.2-8
Requires: httpd, mod_python, mod_ssl

%description
Current is a RHN server implementation for Red Hat's up2date tools. It's
designed for small to medium departments to be able to set up and run their
own up2date server, feeding new applications and security patches to
workstations/servers.

%prep 
%setup

%build
%{__make} all

%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALL_ROOT="$RPM_BUILD_ROOT"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG LICENSE README RELEASE-NOTES TODO
%doc docs/*.txt docs/FAQ/ docs/client/ docs/developer_docs/ docs/current-guide/
%config(noreplace) %{_sysconfdir}/current/current.conf
%config %{_sysconfdir}/current/
%{_sbindir}/*
%{_datadir}/current/


%changelog
* Wed Mar 09 2005 Dag Wieers <dag@wieers.com> - 0.5.11-1 - $Rev$
- Initial package. (using DAR)
