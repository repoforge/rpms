# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Spiffy

Summary: Spiffy Perl Interface Framework For You
Name: perl-Class-Spiffy
Version: 0.15
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Spiffy/

Source: http://www.cpan.org/modules/by-module/Class/Class-Spiffy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.6.1
Requires: perl >= 1:5.6.1

%description
Spiffy Perl Interface Framework For You.

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
%doc %{_mandir}/man3/Class::Spiffy.3pm*
%dir %{perl_vendorlib}/Class/
%{perl_vendorlib}/Class/Spiffy/
%{perl_vendorlib}/Class/Spiffy.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.15-1
- Initial package. (using DAR)
