# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-Valid

Summary: Check validity of Internet email addresses
Name: perl-Email-Valid
Version: 0.15
Release: 1.2
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Valid/

Source: http://www.cpan.org/modules/by-module/Email/Email-Valid-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Check validity of Internet email addresses

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
%doc Changes README
%doc %{_mandir}/man3/Email::Valid.3pm*
%dir %{perl_vendorlib}/Email/
%{perl_vendorlib}/Email/Valid.pm

%changelog
* Sat Aug 07 2004 Dag Wieers <dag@wieers.com> - 1.2-1
- Initial package. (using DAR)
