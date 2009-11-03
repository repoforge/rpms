# $Id$
# Authority: dag
# Upstream: Sam Vilain <sam$vilain,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Lazy

Summary: "lazy" (defered/on-demand) variables
Name: perl-Data-Lazy
Version: 0.6
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Lazy/

Source: http://www.cpan.org/modules/by-module/Data/Data-Lazy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
"lazy" (defered/on-demand) variables.

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/Data::Lazy.3pm*
%dir %{perl_vendorlib}/Data/
#%{perl_vendorlib}/Data/Lazy/
%{perl_vendorlib}/Data/Lazy.pm

%changelog
* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.6-1
- Initial package. (using DAR)
