# $Id$

# Authority: dag
# Upstream: <info@rndsoftware.com>

Summary: Save proc filesystem content for forensic analysis
Name: procget
Version: 0.1.0
Release: 1
License: distributable
Group: Applications/System
URL: http://www.rndsoftware.com/products.shtml

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.rndsoftware.com/binaries/procget-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
procget is used to save the contents of the proc filesystem from a Linux
server under investigation, and procsave is used to recreate that filesystem
on a separate workstation.

%prep
%setup -c

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir}
%{__install} -m0755 * %{buildroot}%{_sbindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_sbindir}/*

%changelog
* Wed Mar 17 2004 Dag Wieers <dag@wieers.com> - 0.1.0-1
- Initial package. (using DAR)
