# $Id$
# Authority: dag
# Upstream:

Summary: Simple remote administration tool, pydsh and pydcp
Name: pydsh
Version: 0.5.4
Release: 2.2
License: GPL
Group: System Environment/Base
URL: http://pydsh.sourceforge.net/

Source: http://dl.sf.net/pydsh/pydsh-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch

BuildRequires: python
Requires: python, python-expect

%description
PyDSH is a simple remote administration toolkit, consisting of
two tools: pydsh and pydcp.

%prep
%setup

%{__perl} -pi.orig -e 's|/usr/local/etc/pydsh/groups/all|%{_sysconfdir}/pydsh/groups/all|' SRC/pydsh.py

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 SRC/pydsh.py %{buildroot}%{_bindir}/pydsh
%{__ln_s} -f pydsh %{buildroot}%{_bindir}/pydcp
%{__install} -D -m0644 DOC/pydcp.8.gz %{buildroot}%{_mandir}/man8/pydcp.8.gz
%{__install} -D -m0644 DOC/pydsh.8.gz %{buildroot}%{_mandir}/man8/pydsh.8.gz

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/pydsh/groups/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING INSTALL README
%doc %{_mandir}/man8/pydcp.8*
%doc %{_mandir}/man8/pydsh.8*
%config(noreplace) %{_sysconfdir}/pydsh/
%{_bindir}/pydcp
%{_bindir}/pydsh

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.4-2.2
- Rebuild for Fedora Core 5.

* Tue Sep 13 2005 Dag Wieers <dag@wieers.com> - 0.5.4-2
- Changed requirement to python-expect.

* Sun May 29 2005 Dag Wieers <dag@wieers.com> - 0.5.4-1
- Initial package. (using DAR)
