# $Id$
# Authority: dag
# Upstream: Mark Overmeer <mark$overmeer,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Object-Realize-Later

Summary: Perl module that implements delayed creation of objects
Name: perl-Object-Realize-Later
Version: 0.18
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Object-Realize-Later/

Source: http://www.cpan.org/modules/by-module/Object/Object-Realize-Later-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Object-Realize-Later is a Perl module that implements
delayed creation of objects.

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
%doc %{_mandir}/man3/Object::Realize::Later.3pm*
%dir %{perl_vendorlib}/Object/
%dir %{perl_vendorlib}/Object/Realize/
%{perl_vendorlib}/Object/Realize/Later.pm
%{perl_vendorlib}/Object/Realize/Later.pod

%changelog
* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 0.18-1
- Initial package. (using DAR)
