# $Id$
# Authority: dag
# Upstream: Audrey Tang <cpan@audreyt.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Object-Declare

Summary: Declarative object constructor
Name: perl-Object-Declare
Version: 0.22
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Object-Declare/

Source: http://www.cpan.org/modules/by-module/Object/Object-Declare-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
Requires: perl >= 0:5.6.0

%description
Declarative object constructor.

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
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/Object::Declare.3pm*
%dir %{perl_vendorlib}/Object/
#%{perl_vendorlib}/Object/Declare/
%{perl_vendorlib}/Object/Declare.pm

%changelog
* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.22-1
- Initial package. (using DAR)
