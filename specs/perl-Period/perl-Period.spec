# $Id: perl-Archive-Tar.spec 120 2004-03-15 17:26:20Z dag $

# Authority: dag

%define real_name Period

Summary: Perl module to deal with time periods. 
Name: perl-Period
Version: 1.20
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Period/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/P/PR/PRYAN/Period-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Perl module to deal with time periods.

%prep
%setup -n %{real_name}-%{version} 

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Thu Mar 04 2004 Dag Wieers <dag@wieers.com> - 1.20-1
- Initial package. (using DAR)
