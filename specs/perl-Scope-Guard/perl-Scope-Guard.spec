# $Id$
# Authority: dag
# Upstream: chocolateboy <chocolate,boy$email,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Scope-Guard

Summary: Lexically scoped resource management
Name: perl-Scope-Guard
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Scope-Guard/

Source: http://www.cpan.org/authors/id/C/CH/CHOCOLATE/Scope-Guard-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Lexically scoped resource management.

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
%doc %{_mandir}/man3/Scope::Guard.3pm*
%dir %{perl_vendorlib}/Scope/
#%{perl_vendorlib}/Scope/Guard/
%{perl_vendorlib}/Scope/Guard.pm

%changelog
* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
