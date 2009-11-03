# $Id$
# Authority: dag
# Upstream: Vipul Ved Prakash <mail$vipul,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Object-Persistence

Summary: Object Persistence with Data::Dumper
Name: perl-Object-Persistence
Version: 0.92
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Object-Persistence/

Source: http://www.cpan.org/modules/by-module/Persistence/Object-Persistence-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Object Persistence with Data::Dumper.

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
%doc Changes MANIFEST examples/
%doc %{_mandir}/man3/Persistence::Object::Simple.3pm*
%dir %{perl_vendorlib}/Persistence/
%{perl_vendorlib}/Persistence/Database.pm
%dir %{perl_vendorlib}/Persistence/Object/
%{perl_vendorlib}/Persistence/Object/Simple.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.92-1
- Initial package. (using DAR)
