# $Id$
# Authority: dag
# Upstream: Paul Marquess <pmqs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Filter

Summary: Perl module that implements Perl source filters
Name: perl-Filter
Version: 1.34
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Filter/

Source: http://www.cpan.org/modules/by-module/Filter/Filter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Filter is a Perl module that implements Perl source filters.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README examples/
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorarch}/Filter/
%{perl_vendorarch}/filter-util.pl
%{perl_vendorarch}/perlfilter.pod
%{perl_vendorarch}/auto/Filter/


%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 1.34-1
- Initial package. (using DAR)
