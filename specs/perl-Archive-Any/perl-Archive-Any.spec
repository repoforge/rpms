# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Archive-Any

Summary: Perl module to deal with file archives
Name: perl-Archive-Any
Version: 0.0932
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Archive-Any/

Source: http://www.cpan.org/modules/by-module/Archive/Archive-Any-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Archive-Any is a perl module that implements a single interface to deal
with file archives.

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
%doc %{_mandir}/man3/Archive::Any.3pm*
%doc %{_mandir}/man3/Archive::Any::*.3pm*
%dir %{perl_vendorlib}/Archive/
%{perl_vendorlib}/Archive/Any/
%{perl_vendorlib}/Archive/Any.pm

%changelog
* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 0.0932-1
- Updated to release 0.0932.

* Fri Aug 03 2007 Dag Wieers <dag@wieers.com> - 0.093-1
- Initial package. (using DAR)
