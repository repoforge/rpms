# $Id: $

# Authority: dries
# Upstream: 

Summary: sudo shell
Name: sudosh
Version: 1.2.2
Release: 1
License: Open Software License
Group: Applications/System
URL: http://sourceforge.net/projects/sudosh

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/sudosh/sudosh-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: sudo

%description
sudosh works directly with sudo to provide a fully functional shell that
users may use to obtain full root access. Unlike providing a team of system
administrators full root access through sudo, it guarantees that detailed
logs are kept. It uses the script command in conjunction with a secure FIFO
and comes with a utility to view sessions and drill down deeper and see the
actual session output. 

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_bindir}
%{__install} sudosh %{buildroot}%{_bindir}/sudosh
%{__install} sudosh-show-sessions %{buildroot}%{_bindir}/sudosh-show-sessions
%{__install} sudosh-view-session %{buildroot}%{_bindir}/sudosh-view-session
%{__install} sudoshd %{buildroot}%{_bindir}/sudoshd

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING INSTALL
%{_bindir}/*

%changelog
* Mon Oct 18 2004 Dries Verachtert <dries@ulyssis.org> - 1.2.2-1
- Update to release 1.2.2.

* Sat Oct 02 2004 Dries Verachtert <dries@ulyssis.org> - 0.7.0-1
- Initial package.
