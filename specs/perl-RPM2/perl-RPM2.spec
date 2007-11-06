# $Id$
# Authority: dries
# Upstream: Chip Turner <cturner$pattern,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name RPM2

Summary: Perl bindings for the RPM Package Manager API
Name: perl-RPM2
Version: 0.67
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/RPM2/

Source: http://search.cpan.org//CPAN/authors/id/C/CH/CHIPT/RPM2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Perl bindings for the RPM Package Manager API.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/RPM2*.3pm*
%{perl_vendorarch}/RPM2.pm
%{perl_vendorarch}/auto/RPM2/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.67-1
- Initial package.
