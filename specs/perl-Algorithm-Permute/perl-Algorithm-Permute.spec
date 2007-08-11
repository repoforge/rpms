# $Id$
# Authority: dries
# Upstream: Edwin Pratomo <edwin$poskanzer,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Algorithm-Permute

Summary: Fast permutation
Name: perl-Algorithm-Permute
Version: 0.06
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Algorithm-Permute/

Source: http://search.cpan.org/CPAN/authors/id/E/ED/EDPRATOMO/Algorithm-Permute-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
Handy and fast permutation with object oriented interface.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Algorithm/
%{perl_vendorarch}/Algorithm/Permute.pm
%dir %{perl_vendorarch}/auto/Algorithm/
%{perl_vendorarch}/auto/Algorithm/Permute/

%changelog
* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
