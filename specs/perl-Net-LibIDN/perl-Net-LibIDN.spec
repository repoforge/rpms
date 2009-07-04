# $Id$
# Authority: dag
# Upstream: Thomas Jacob <jacob$internet24,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-LibIDN

Summary: Perl module with bindings for GNU Libidn
Name: perl-Net-LibIDN
Version: 0.12
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-LibIDN/

Source: http://www.cpan.org/modules/by-module/Net/Net-LibIDN-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: libidn-devel
Requires: perl

%description
Net-LibIDN is a Perl module with bindings for GNU Libidn.

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Artistic Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Net::LibIDN.3pm*
%dir %{perl_vendorarch}/auto/Net/
%{perl_vendorarch}/auto/Net/LibIDN/
%dir %{perl_vendorarch}/Net/
%{perl_vendorarch}/Net/LibIDN.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.12-1
- Updated to version 0.12.

* Fri Jan 16 2009 Christoph Maser <cmr@financial.com> - 0.11-1
- Updated to release 0.11.

* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 0.10-1
- Updated to release 0.10.

* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
