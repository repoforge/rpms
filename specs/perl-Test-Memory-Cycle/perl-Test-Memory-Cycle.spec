# $Id$
# Authority: dag

### EL6 ships with perl-Test-Memory-Cycle-1.04-7.1.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Memory-Cycle

Summary: Verifies code hasn't left circular references
Name: perl-Test-Memory-Cycle
Version: 1.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Memory-Cycle/

Source: http://www.cpan.org/modules/by-module/Test/Test-Memory-Cycle-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Verifies code hasn't left circular references.

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
%doc %{_mandir}/man3/Test::Memory::Cycle.3pm*
%dir %{perl_vendorlib}/Test/
%dir %{perl_vendorlib}/Test/Memory/
%{perl_vendorlib}/Test/Memory/Cycle.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.04-1
- Initial package. (using DAR)
