# $Id$
# Authority: dries
# Upstream: Xavier Guimard <x,guimard$free,fr>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lemonldap-NG-Manager

Summary: Perl extension for managing Lemonldap::NG Web-SSO system
Name: perl-Lemonldap-NG-Manager
Version: 0.90
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lemonldap-NG-Manager/

Source: http://www.cpan.org/modules/by-module/Lemonldap/Lemonldap-NG-Manager-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(CGI) >= 3.08                   
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(IO::String) 
BuildRequires: perl(Lemonldap::NG::Common) >= 0.93 
BuildRequires: perl(Lemonldap::NG::Handler) >= 0.91
BuildRequires: perl(LWP::UserAgent) 
BuildRequires: perl(XML::Simple) 


%description
Perl extension for managing Lemonldap::NG Web-SSO system.

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
find example/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README TODO example/
%doc %{_mandir}/man3/Lemonldap::NG::Manager.3pm*
%doc %{_mandir}/man3/Lemonldap::NG::Manager::*.3pm*
%dir %{perl_vendorlib}/auto/Lemonldap/
%dir %{perl_vendorlib}/auto/Lemonldap/NG/
%{perl_vendorlib}/auto/Lemonldap/NG/Manager/
%dir %{perl_vendorlib}/Lemonldap/
%dir %{perl_vendorlib}/Lemonldap/NG/
%{perl_vendorlib}/Lemonldap/NG/Manager/
%{perl_vendorlib}/Lemonldap/NG/Manager.pm

%changelog
* Thu Jul 23 2009 Christoph Maser <cmr@financial.com> - 0.90-1
- Updated to version 0.90.

* Thu Oct 09 2008 Dag Wieers <dag@wieers.com> - 0.86-1
- Updated to release 0.86.

* Tue Jun 24 2008 Dag Wieers <dag@wieers.com> - 0.85-1
- Updated to release 0.85.

* Sat May 10 2008 Dag Wieers <dag@wieers.com> - 0.84-1
- Updated to release 0.84.

* Fri Mar 07 2008 Dag Wieers <dag@wieers.com> - 0.83-1
- Updated to release 0.83.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.82-1
- Updated to release 0.82.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.44-1
- Initial package.
