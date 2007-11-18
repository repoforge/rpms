# $Id$
# Authority: dag
# Upstream: Stevan Little <stevan$iinteractive,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-MOP

Summary: Perl module that implements a Meta Object Protocol
Name: perl-Class-MOP
Version: 0.45
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-MOP/

Source: http://www.cpan.org/modules/by-module/Class/Class-MOP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Test::Exception) >= 0.21
#BuildRequires: perl(Test::More) >= 0.62

%description
Class-MOP is a Perl module that implements a Meta Object Protocol.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README TODO examples/
%doc %{_mandir}/man3/Class::MOP.3pm*
%doc %{_mandir}/man3/Class::MOP::*.3pm*
%doc %{_mandir}/man3/metaclass.3pm*
%dir %{perl_vendorlib}/Class/
%{perl_vendorlib}/Class/MOP/
%{perl_vendorlib}/Class/MOP.pm
%{perl_vendorlib}/metaclass.pm

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.45-1
- Updated to release 0.45.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.42-1
- Updated to release 0.42.

* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 0.37-1
- Initial package. (using DAR)
