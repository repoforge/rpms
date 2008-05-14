# $Id$
# Authority: dag
# Upstream: Andreas 'ac0v' Specht - ACID$cpan,org

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Std-Fast
%define real_version 0.000006

Summary: Faster but less secure than Class::Std
Name: perl-Class-Std-Fast
Version: 0.0.6
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Std-Fast/

Source: http://www.cpan.org/modules/by-module/Class/Class-Std-Fast-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::More)

%description
Faster but less secure than Class::Std.

%prep
%setup -n %{real_name}-v%{version}

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
%doc %{_mandir}/man3/Class::Std::Fast.3pm*
%doc %{_mandir}/man3/Class::Std::Fast::*.3pm*
%dir %{perl_vendorlib}/Class/
%dir %{perl_vendorlib}/Class/Std/
%{perl_vendorlib}/Class/Std/Fast/
%{perl_vendorlib}/Class/Std/Fast.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.0.6-1
- Initial package. (using DAR)
