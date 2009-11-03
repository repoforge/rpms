# $Id$
# Authority: cmr

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Guard

Summary: Perl module named Guard
Name: perl-Guard
Version: 1.021
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Guard/

Source: http://www.cpan.org/authors/id/M/ML/MLEHMANN/Guard-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Guard is a Perl module.

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
%doc COPYING Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Guard.3pm*
%{perl_vendorarch}/auto/Guard/
%{perl_vendorarch}/Guard.pm

%changelog
* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 1.021-1
- Updated to version 1.021.

* Fri Jul 10 2009 Christoph Maser <cmr@financial.com> - 1.02-1
- Initial package. (using DAR)
