# $Id$
# Authority: dag
# Upstream: <info$rndsoftware,com>

Summary: Save memory content for forensic analysis
Name: memget
Version: 0.1.0
Release: 2.2%{?dist}
License: distributable
Group: Applications/System
URL: http://www.rndsoftware.com/products.shtml

Source: http://www.rndsoftware.com/binaries/memget-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
memget is used to save the contents of memory from a Linux server under
investigation, and mempeek is used to examine that memory on a separate
workstation.

%prep
%setup -c

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir}
%{__install} -p -m0755 memget %{buildroot}%{_sbindir}/memget
%{__install} -p -m0755 mempeek %{buildroot}%{_sbindir}/mempeek

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_sbindir}/memget
%{_sbindir}/mempeek

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.0-2.2
- Rebuild for Fedora Core 5.

* Wed Mar 31 2004 Dag Wieers <dag@wieers.com> - 0.1.0-2
- Cosmetic rebuild for Group-tag.

* Wed Mar 17 2004 Dag Wieers <dag@wieers.com> - 0.1.0-1
- Initial package. (using DAR)
