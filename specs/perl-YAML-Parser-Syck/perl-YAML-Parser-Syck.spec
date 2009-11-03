# $Id$
# Authority: dries
# Upstream: Brian Ingerson <ingy$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name YAML-Parser-Syck

Summary: Wrapper for the YAML Parser Extension: libsyck
Name: perl-YAML-Parser-Syck
Version: 0.01
Release: 1.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YAML-Parser-Syck/

Source: http://www.cpan.org/modules/by-module/YAML/YAML-Parser-Syck-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: syck-devel
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Perl Wrapper for the YAML Parser Extension: libsyck.

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
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/YAML/
%dir %{perl_vendorarch}/YAML/Parser/
%{perl_vendorarch}/YAML/Parser/Syck.pm
%dir %{perl_vendorarch}/auto/YAML/
%dir %{perl_vendorarch}/auto/YAML/Parser/
%{perl_vendorarch}/auto/YAML/Parser/Syck/

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
