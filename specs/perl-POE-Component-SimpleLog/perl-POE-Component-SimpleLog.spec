# $Id$
# Authority: dries
# Upstream: Apocalypse <perl$0ne,us>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-SimpleLog

Summary: Manage a simple logging system for POE
Name: perl-POE-Component-SimpleLog
Version: 1.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-SimpleLog/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-SimpleLog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Perl extension to manage a simple logging system for POE.

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
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%{perl_vendorlib}/POE/Component/SimpleLog.pm

%changelog
* Fri Jul  3 2009 Christoph Maser <cmr@financial.com> - 1.05-1
- Updated to version 1.05.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Initial package.
