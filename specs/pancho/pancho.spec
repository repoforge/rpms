# $Id$
# Authority: dag
# Upstream: <pancho-discuss$lunarmedia,net>

%define perl_sitelib  %(eval "`perl -V:installsitelib`"; echo $installsitelib)

%define real_name Pancho

Summary: Archive and manage remote nodes using SNMP and TFTP
Name: pancho
Version: 9.3.9
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.pancho.org/

Source: http://www.pancho.org/archives/pancho/pancho-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503, perl-Net-SNMP, perl-Config-IniFiles, perl-Parallel-ForkManager
Requires: perl >= 0:5.00503

%description
Pancho is a Perl based project which allows network administrators to
archive device configurations as well as make changes to these remote
nodes through the use of SNMP and TFTP.

Pancho is module based in the sense that support for new vendors may
be written by users based on a template provided with the distribution
and shared with the community via the Pancho Project website.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL NOASK \
	PREFIX="%{_prefix}" \
	CONFDIR="%{_sysconfdir}"

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	PREFIX="%{buildroot}%{_prefix}" \
	SYS_CONFDIR="%{buildroot}%{_sysconfdir}" \
	LIB="%{buildroot}%{perl_sitelib}"

%{__perl} -pi.orig -e 's|%{buildroot}||' blib/script/pancho

%{__install} -Dp -m0755 blib/script/pancho %{buildroot}%{_bindir}/pancho

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
                %{buildroot}%{perl_sitearch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README license/* samples/*
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/pancho.conf
%{_bindir}/*
%{perl_sitelib}/*

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 9.3.9-1
- Updated to release 9.3.9.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 9.3.7-1.2
- Rebuild for Fedora Core 5.

* Wed May 04 2005 Dag Wieers <dag@wieers.com> - 9.3.7-1
- Updated to release 9.3.7.

* Fri Sep 24 2004 Dag Wieers <dag@wieers.com> - 9.3.6-1
- Updated to release 9.3.6.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 9.3.5-1
- Updated to release 9.3.5.

* Wed May 26 2004 Dag Wieers <dag@wieers.com> - 9.3.2-1
- Updated to release 9.3.2.

* Wed Mar 10 2004 Dag Wieers <dag@wieers.com> - 9.3.1-1
- Updated to release 9.3.1.

* Sun Mar 07 2004 Dag Wieers <dag@wieers.com> - 9.3.0-1
- Initial package. (using DAR)
