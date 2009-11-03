# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Compile

Summary: Perl Module Compilation
Name: perl-Module-Compile
Version: 0.20
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Compile/

Source: http://www.cpan.org/modules/by-module/Module/Module-Compile-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
Requires: perl >= 0:5.6.0

%description
Perl Module Compilation.

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
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Module/
%dir %{perl_vendorlib}/Module/Install/
%dir %{perl_vendorlib}/Module/Install/Admin/
%{perl_vendorlib}/Module/Compile.pm
%{perl_vendorlib}/Module/Install/Admin/PMC.pm
%{perl_vendorlib}/Module/Install/PMC.pm
%{perl_vendorlib}/Module/Optimize.pm

%changelog
* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 0.20-1
- Initial package. (using DAR)
