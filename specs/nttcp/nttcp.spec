# $Id$

# Authority: dag

# Upstream: Elmar Bartel <bartel$informatik,tu-muenchen,de>

Summary: tool to do memory to memory performance measurements with TCP/IP.
Name: nttcp
Version: 1.47
Release: 0.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.leo.org/~elmar/nttcp/

Source: http://www.leo.org/~elmar/nttcp/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
The TTCP program is used to do memory to memory performance measurements
with TCP/IP. The program we use, comes from the public domain and has
been adapted and modified by several persons.

%prep
%setup

### FIXME: Make program use standard autotools directories.
%{__perl} -pi.orig -e '
		s|\$\(prefix\)/bin|\$(bindir)|;
		s|\$\(prefix\)/man/man1|\$(mandir)/man1|;
	' Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.47-0.2
- Rebuild for Fedora Core 5.

* Mon Aug 04 2003 Dag Wieers <dag@wieers.com> - 1.47-0
- Initial package. (using DAR)
