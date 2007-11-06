# $Id$
# Authority: dries
# Upstream: Ruslan U. Zakirov <Ruslan,Zakirov$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Regexp-Common-net-CIDR

Summary: Provide patterns for CDIR blocks
Name: perl-Regexp-Common-net-CIDR
Version: 0.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Regexp-Common-net-CIDR/

Source: http://search.cpan.org//CPAN/authors/id/R/RU/RUZ/Regexp-Common-net-CIDR-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(Regexp::Common), perl(ExtUtils::MakeMaker)

%description
Provide patterns for CDIR blocks.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/Regexp::Common::net::CIDR*
%{perl_vendorlib}/Regexp/Common/net/CIDR.pm

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
