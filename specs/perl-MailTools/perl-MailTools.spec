# Authority: dag

%define rname MailTools

Summary: MailTools module for perl 
Name: perl-MailTools
Version: 1.60
Release: 0
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MailTools/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.cpan.org/authors/id/G/GB/GBARR/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

Obsoletes: perl-Mail

BuildArch: noarch
BuildRequires: perl >= 0:5.00503 %{?rh73:, perl-libnet >= 1.05}
Requires: perl >= 0:5.00503 %{?rh73:, perl-libnet >= 1.05}

%description
MailTools module for perl

%prep
%setup -n %{rname}-%{version} 

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README* ChangeLog
%doc %{_mandir}/man?/*
%{_libdir}/perl5/

%changelog
* Fri Nov 28 2003 Dag Wieers <dag@wieers.com> - 1.60-0
- Updated to release 1.60.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 1.58-0
- Updated to release 1.58.

* Sun Jan 23 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
