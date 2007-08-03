# $Id$
# Authority: dag
# Upstream: Paul T. Seamons <perlspam$seamons,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Taint-Runtime

Summary: Perl module named Taint-Runtime
Name: perl-Taint-Runtime
Version: 0.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Taint-Runtime/

Source: http://www.cpan.org/modules/by-module/Taint/Taint-Runtime-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
perl-Taint-Runtime is a Perl module.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Taint::Runtime.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Taint/
%{perl_vendorarch}/Taint/Runtime.pm
%{perl_vendorarch}/Taint/is_taint_bench.pl
%dir %{perl_vendorarch}/auto/Taint/
%{perl_vendorarch}/auto/Taint/Runtime/

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
