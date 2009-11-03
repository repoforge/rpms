# $Id$
# Authority: dag

Summary: Server for Red Hat's up2date tools
Name: current
Version: 1.6.1
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://current.tigris.org/

Source: ftp://ftp.biology.duke.edu/pub/admin/current/current-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: docbook-style-xsl, docbook-style-dsssl, docbook-dtds
BuildRequires: docbook-utils, docbook-utils-pdf, python-devel >= 2.2
BuildRequires: xmlto
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
%{__make} install INSTALL_ROOT="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG LICENSE README RELEASE-NOTES TODO
%doc docs/*.txt docs/client/ docs/current-guide/ docs/developer_docs/ docs/FAQ
%config(noreplace) %{_sysconfdir}/current/current.conf
%dir %{_sysconfdir}/current/
%{_sbindir}/cadmin
%{_sbindir}/cinstall
%{_datadir}/current/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.6.1-1.2
- Rebuild for Fedora Core 5.

* Mon Jan 16 2006 Dag Wieers <dag@wieers.com> - 1.6.1-1
- Updated to release 1.6.1.

* Wed Mar 09 2005 Dag Wieers <dag@wieers.com> - 0.5.11-1
- Initial package. (using DAR)
