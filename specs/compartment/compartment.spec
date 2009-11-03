# $Id$
# Authority: dag
# Upstream: Marc Heuse <marc$suse,de>

Summary: Confine services in a limited environment
Name: compartment
Version: 1.1
Release: 0.2%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://www.suse.de/~marc/

Source: http://www.suse.de/~marc/compartment-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
Compartment was designed to allow safe execution of priviliged and/or
untrusted executables and services. It has got all possible features
included, which can be used to minimize the risk of a trojanized or
vulnerable program/service.

%prep
%setup

%build
%{__make} %{?_smp_mflags} compartment

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 compartment %{buildroot}%{_bindir}/compartment
%{__install} -Dp -m0644 compartment.1 %{buildroot}%{_mandir}/man1/compartment.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENCE README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1-0.2
- Rebuild for Fedora Core 5.

* Sun May 04 2003 Dag Wieers <dag@wieers.com> - 1.1-0
- Initial package. (using DAR)
