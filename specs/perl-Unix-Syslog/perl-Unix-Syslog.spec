# $Id$

# Authority: dag

%define rname Unix-Syslog

Summary: Syslog module for perl 
Name: perl-Unix-Syslog
Version: 0.100
Release: 0
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unix-Syslog/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.cpan.org/authors/id/M/MH/MHARNISCH/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Syslog module for perl

%prep
%setup -n %{rname}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/%{_target_cpu}-linux-thread-multi/
%{__rm} -rf %{buildroot}%{_libdir}/perl5/vendor_perl/*/%{_target_cpu}-linux-thread-multi/

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes Artistic
%doc %{_mandir}/man?/*
%{_libdir}/perl5/

%changelog
* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 0.100-0
- Updated to release 0.100.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
