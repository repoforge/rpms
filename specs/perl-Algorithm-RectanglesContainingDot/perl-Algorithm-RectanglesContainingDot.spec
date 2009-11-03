# $Id$
# Authority: cmr
# Upstream: Salvador Fandiño García <salva$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Algorithm-RectanglesContainingDot

Summary: Perl module named Algorithm-RectanglesContainingDot
Name: perl-Algorithm-RectanglesContainingDot
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Algorithm-RectanglesContainingDot/

Source: http://www.cpan.org/modules/by-module/Algorithm/Algorithm-RectanglesContainingDot-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::More)

%description
perl-Algorithm-RectanglesContainingDot is a Perl module.

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
%doc %{_mandir}/man3/Algorithm::RectanglesContainingDot.3pm*
%dir %{perl_vendorlib}/Algorithm/
#%{perl_vendorlib}/Algorithm/RectanglesContainingDot/
%{perl_vendorlib}/Algorithm/RectanglesContainingDot.pm

%changelog
* Tue Sep 29 2009 Christoph Maser <cmr@financial.com> - 0.02-1
- Initial package. (using DAR)
