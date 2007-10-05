# $Id$
# Authority: dag
# Upstream: Michael Peppler <mpeppler$peppler,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-Sybase

Summary: Perl module named DBD-Sybase
Name: perl-DBD-Sybase
Version: 1.08
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-Sybase/

Source: http://www.cpan.org/modules/by-module/DBD/DBD-Sybase-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-DBD-Sybase is a Perl module.

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

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS CHANGES MANIFEST META.yml README README.freetds README.vms eg/
%doc %{_mandir}/man3/DBD::Sybase.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/DBD/
%{perl_vendorarch}/DBD/Sybase.pm
%dir %{perl_vendorarch}/auto/DBD/
%{perl_vendorarch}/auto/DBD/Sybase/

%changelog
* Fri Oct 05 2007 Dag Wieers <dag@wieers.com> - 1.08-1
- Initial package. (using DAR)
