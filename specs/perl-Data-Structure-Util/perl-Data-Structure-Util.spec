# $Id$
# Authority: dag
# Upstream: Fotango Ltd <cpan$fotango,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Structure-Util

Summary: Perl module to change nature of data within a structure
Name: perl-Data-Structure-Util
Version: 0.12
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Structure-Util/

Source: http://www.cpan.org/modules/by-module/Data/Data-Structure-Util-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker), perl(Module::Build)
Requires: perl

%description
Data-Structure-Util is a Perl module to change nature of data
within a structure.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES MANIFEST META.yml README
%doc %{_mandir}/man1/packages.pl.1*
%doc %{_mandir}/man3/Data::Structure::Util.3pm*
%dir %{perl_vendorarch}/Data/
%dir %{perl_vendorarch}/Data/Structure/
%{perl_vendorarch}/Data/Structure/Util.pm
%dir %{perl_vendorarch}/auto/Data/
%dir %{perl_vendorarch}/auto/Data/Structure/
%{perl_vendorarch}/auto/Data/Structure/Util/
%{_bindir}/packages.pl

%changelog
* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 0.12-1
- Initial package. (using DAR)
