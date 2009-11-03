# $Id$
# Authority: dag
# Upstream: Maciej Ceglowski <mceglows$middlebury,edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Bloom-Filter

Summary: Perl module that implements a sample Perl Bloom filter
Name: perl-Bloom-Filter
Version: 1.0
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Bloom-Filter/

Source: http://www.cpan.org/modules/by-module/Bloom/Bloom-Filter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Bloom-Filter is a Perl module that implements a sample Perl Bloom filter.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Bloom::Filter.3pm*
%dir %{perl_vendorlib}/Bloom/
%{perl_vendorlib}/Bloom/Filter.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
