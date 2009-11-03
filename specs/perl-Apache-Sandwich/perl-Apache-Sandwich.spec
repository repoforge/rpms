# $Id$
# Authority: dag
# Upstream: Vivek Khera <vivek$khera,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-Sandwich

Summary: Perl module that provides a layered document (sandwich) maker
Name: perl-Apache-Sandwich
Version: 2.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-Sandwich/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-Sandwich-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Apache-Sandwich is a Perl module that provides a layered
document (sandwich) maker.

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
%doc ChangeLog Changes MANIFEST README
%doc %{_mandir}/man3/Apache::Sandwich.3pm*
%dir %{perl_vendorlib}/Apache/
%{perl_vendorlib}/Apache/Sandwich.pm

%changelog
* Wed Oct 10 2007 Dag Wieers <dag@wieers.com> - 2.05-1
- Initial package. (using DAR)
