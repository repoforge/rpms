# $Id$

# Authority: dag

# Upstream: <info@figlet.org>

%define real_version 221

Summary: program for making large letters out of ordinary text
Name: figlet
Version: 2.2.1
Release: 1
Group: Applications/Text
License: GPL
URL: http://www.figlet.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.figlet.org/pub/figlet/program/unix/%{name}%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
FIGlet is a program for making large letters out of ordinary text.

%prep
%setup -n %{name}%{real_version}

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}" DEFAULTFONTDIR="%{_datadir}/figlet"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_mandir}/man6 \
			%{buildroot}%{_bindir}
%makeinstall \
	DESTDIR="%{buildroot}%{_bindir}" \
	MANDIR="%{buildroot}%{_mandir}/man6" \
	DEFAULTFONTDIR="%{buildroot}%{_datadir}/figlet"

### FIXME: Change executable permission of binaries (should go into Makefile)
%{__chmod} a+x %{buildroot}%{_bindir}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Artistic-license.txt CHANGES FAQ README
%doc %{_mandir}/man6/*
%{_bindir}/*
%{_datadir}/figlet/

%changelog
* Mon Jun 10 2003 Dag Wieers <dag@wieers.com> - 2.2.1-1
- Change executable permission of binaries. (Koenraad Heijlen)

* Thu Apr 24 2003 Dag Wieers <dag@wieers.com> - 2.2.1-0
- Initial package. (using DAR)
