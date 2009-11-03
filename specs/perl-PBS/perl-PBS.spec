# $Id$
# Authority: dag
# Upstream: Todd Merritt <tmerritt$email,arizona,edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name PBS

Summary: Perl module for PBS
Name: perl-PBS
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PBS/

Source: http://www.cpan.org/authors/id/T/TM/TMERRITT/PBS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: libtorque-devel
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-PBS is a Perl module for PBS.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/PBS.3pm*
#%doc %{_mandir}/man3/*.3pm*
%{perl_vendorarch}/PBS.pm
%{perl_vendorarch}/auto/PBS/

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
