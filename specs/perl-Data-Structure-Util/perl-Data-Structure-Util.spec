# $Id$
# Authority: dag
# Upstream: Andy Armstrong <andy$hexten,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Structure-Util

Summary: Change nature of data within a structure
Name: perl-Data-Structure-Util
Version: 0.15
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Structure-Util/

Source: http://www.cpan.org/modules/by-module/Data/Data-Structure-Util-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Build)

%description
Change nature of data within a structure.

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
%doc CHANGES MANIFEST META.yml README SIGNATURE
#%doc %{_mandir}/man1/packages.pl.1*
%doc %{_mandir}/man3/Data::Structure::Util.3pm*
#%{_bindir}/packages.pl
%dir %{perl_vendorarch}/auto/Data/
%dir %{perl_vendorarch}/auto/Data/Structure/
%{perl_vendorarch}/auto/Data/Structure/Util/
%dir %{perl_vendorarch}/Data/
%dir %{perl_vendorarch}/Data/Structure/
%{perl_vendorarch}/Data/Structure/Util.pm

%changelog
* Tue Mar 11 2008 Dag Wieers <dag@wieers.com> - 0.15-1
- Updated to release 0.15.

* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 0.12-1
- Initial package. (using DAR)
