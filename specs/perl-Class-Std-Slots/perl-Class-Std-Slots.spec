# $Id$
# Authority: dag
# Upstream: Andy Armstrong <andy$hexten,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Std-Slots

Summary: Provide signals and slots for standard classes
Name: perl-Class-Std-Slots
Version: 0.31
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Std-Slots/

Source: http://www.cpan.org/modules/by-module/Class/Class-Std-Slots-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Class::Std)
BuildRequires: perl(Module::Build)

%description
Provide signals and slots for standard classes.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL --installdirs vendor --destdir %{buildroot}
./Build


%install
%{__rm} -rf %{buildroot}
./Build pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/Class::Std::Slots.3pm*
%dir %{perl_vendorlib}/Class/
%dir %{perl_vendorlib}/Class/Std/
#%{perl_vendorlib}/Class/Std/Slots/
%{perl_vendorlib}/Class/Std/Slots.pm

%changelog
* Thu Jul 16 2009 Christoph Maser <cmr@financial.com> - 0.31-1
- Updated to version 0.31.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
