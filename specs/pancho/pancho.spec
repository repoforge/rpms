# $Id$

# Authority: dag
# Upstream: <pancho-discuss@lunarmedia.net>

%define rname Pancho

Summary: Archive and manage remote nodes using SNMP and TFTP
Name: pancho
Version: 9.3.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.panchoproject.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.panchoproject.org/archives/pancho/pancho-v%{version}.tar.gz
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
%setup -n %{rname}-%{version}

%build
%{__perl} Makefile.PL NOASK \
	PREFIX="%{_prefix}" \
	CONFDIR="%{_sysconfdir}"

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	PREFIX="%{buildroot}%{_prefix}" \
	SYS_CONFDIR="%{buildroot}%{_sysconfdir}" \
	INSTALLSITELIB="%{buildroot}%{_libdir}"

%{__perl} -pi.orig -e 's|%{buildroot}||' blib/script/pancho

%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 blib/script/pancho %{buildroot}%{_bindir}

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -rf %{buildroot}%{_libdir}/perl5/site_perl/*/*-linux-thread-multi/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README license/* samples/*
%config(noreplace) %{_sysconfdir}/pancho.conf
%{_bindir}/*
%{_libdir}/perl5/site_perl/*/Pancho/

%changelog
* Wed Mar 10 2004 Dag Wieers <dag@wieers.com> - 9.3.1-1
- Updated to release 9.3.1.

* Sun Mar 07 2004 Dag Wieers <dag@wieers.com> - 9.3.0-1
- Initial package. (using DAR)
