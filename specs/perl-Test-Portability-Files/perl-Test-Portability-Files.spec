# $Id$
# Authority: dag
# Upstream: Sébastien Aperghis-Tramoni <maddingue$free,fr>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Portability-Files

Summary: Perl module to check file names portability
Name: perl-Test-Portability-Files
Version: 0.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Portability-Files/

Source: http://www.cpan.org/modules/by-module/Test/Test-Portability-Files-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Test-Portability-Files is a Perl module to check file names portability.

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
%doc Changes LICENSE LICENSE.Artistic LICENSE.GPL MANIFEST META.yml README
%doc %{_mandir}/man3/Test::Portability::Files.3pm*
%dir %{perl_vendorlib}/Test/
%dir %{perl_vendorlib}/Test/Portability/
%{perl_vendorlib}/Test/Portability/Files.pm

%changelog
* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
