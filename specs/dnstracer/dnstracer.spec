# $Id$
# Authority: dag
# Upstream: Edwin Groothuis <edwin$mavetju,org>

Summary: Trace a chain of DNS servers to the source
Name: dnstracer
Version: 1.8
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.mavetju.org/unix/general.php

Source: http://www.mavetju.org/download/dnstracer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes: dnstrace <= %{version}

%description
dnstrace determines where a given Domain Name Server (DNS) gets its
information from, and follows the chain of DNS servers back to the
servers which know the data.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES CONTACT README
%doc %{_mandir}/man8/*
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.8-1.2
- Rebuild for Fedora Core 5.

* Thu Jul 08 2004 Dag Wieers <dag@wieers.com> - 1.8-1
- Updated to release 1.8.

* Mon Aug 25 2003 Dag Wieers <dag@wieers.com> - 1.7-1
- Updated to release 1.7.

* Sat Dec 28 2002 Dag Wieers <dag@wieers.com> - 1.6-0
- Updated to release 1.6 (name changed from dnstrace to dnstracer)

* Sun Jan 20 2002 Dag Wieers <dag@wieers.com> - 1.1-0
- Initial package.
