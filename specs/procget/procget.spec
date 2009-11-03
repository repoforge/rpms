# $Id$
# Authority: dag
# Upstream: <info$rndsoftware,com>

Summary: Save proc filesystem content for forensic analysis
Name: procget
Version: 0.1.0
Release: 2.2%{?dist}
License: distributable
Group: Applications/System
URL: http://www.rndsoftware.com/products.shtml

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
%{__install} -Dp -m0755 procget %{buildroot}%{_sbindir}/procget
%{__install} -Dp -m0755 procsave %{buildroot}%{_sbindir}/procsave

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_sbindir}/procget
%{_sbindir}/procsave

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.0-2.2
- Rebuild for Fedora Core 5.

* Wed Mar 31 2004 Dag Wieers <dag@wieers.com> - 0.1.0-2
- Cosmetic rebuild for Group-tag.

* Wed Mar 17 2004 Dag Wieers <dag@wieers.com> - 0.1.0-1
- Initial package. (using DAR)
