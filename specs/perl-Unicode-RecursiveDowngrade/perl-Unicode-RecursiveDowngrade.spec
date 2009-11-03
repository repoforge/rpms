# $Id$
# Authority: dag
# Upstream: Koichi Taniguchi <taniguchi$livedoor,jp>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unicode-RecursiveDowngrade

Summary: Perl module to turn off the UTF-8 flags inside of complex variable
Name: perl-Unicode-RecursiveDowngrade
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unicode-RecursiveDowngrade/

Source: http://www.cpan.org/modules/by-module/Unicode/Unicode-RecursiveDowngrade-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Unicode-RecursiveDowngrade is a Perl module to turn off the UTF-8 flags
inside of complex variable.

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
%doc %{_mandir}/man3/Unicode::RecursiveDowngrade.3pm*
%dir %{perl_vendorlib}/Unicode/
#%{perl_vendorlib}/Unicode/RecursiveDowngrade/
%{perl_vendorlib}/Unicode/RecursiveDowngrade.pm

%changelog
* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 0.04-1
- Updated to release 0.04.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
