# $Id$
# Authority: dag
# Upstream: Darxus <darxus$chaosreigns,com>

Summary: Implementation of /dev/speech
Name: speechd
Version: 0.56
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://www.speechio.org/

Source: http://www.speechio.org/dl/speechd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: festival

%description
Speechd implements the /dev/speech device, which will recite any text
written to it.

%prep
%setup -n %{name}

%{__perl} -pi.orig -e 's|--owner=\$\(\w+\) --group=\$\(\w+\)||' Makefile

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man1/ \
			%{buildroot}%{_sysconfdir} \
			%{buildroot}/dev/
%makeinstall \
	INSTALL_MANDIR="%{buildroot}%{_mandir}/man1" \
	INSTALL_BINDIR="%{buildroot}%{_bindir}" \
	INSTALL_RCDIR="%{buildroot}%{_sysconfdir}" \
	SPEECHD_FIFO="%{buildroot}/dev/speech"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGELOG COPYING INSTALL README TODO
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/*
/dev/speech

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.56-1.2
- Rebuild for Fedora Core 5.

* Wed Mar 17 2004 Dag Wieers <dag@wieers.com> - 0.56-1
- Initial package. (using DAR)
