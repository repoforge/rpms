# $Id$
# Authority: dag
# Upstream: Kurt Garloff <garloff$suse,de>

Summary: Filesystem benchmark tool
Name: bonnie
Version: 1.5
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.garloff.de/kurt/linux/bonnie/

Source: http://www.garloff.de/kurt/linux/bonnie/bonnie-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Bonnie is a popular performance benchmark that targets various aspects
of Unix file systems.

%prep
%setup -n bonnie

%build
%{__make} CC="%{__cc}" CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" MANDIR="%{_mandir}"

%files
%defattr(-, root, root, 0755)
%doc bonnie.doc Instructions README
%doc %{_mandir}/man1/bonnie.1.gz
%{_bindir}/bonnie

%changelog
* Sun Feb 05 2012 Dag Wieers <dag@wieers.com> - 1.5-1
- Updated to release 1.5.

* Sat Nov 08 2008 Dag Wieers <dag@wieers.com> - 1.4-1
- Initial package. (using DAR)
