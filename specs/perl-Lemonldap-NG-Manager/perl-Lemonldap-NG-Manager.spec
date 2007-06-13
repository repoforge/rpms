# $Id$
# Authority: dries
# Upstream: Xavier Guimard <perl$astola,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lemonldap-NG-Manager

Summary: Perl extension for managing Lemonldap::NG Web-SSO system
Name: perl-Lemonldap-NG-Manager
Version: 0.44
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lemonldap-NG-Manager/

Source: http://search.cpan.org//CPAN/authors/id/G/GU/GUIMARD/Lemonldap-NG-Manager-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Perl extension for managing Lemonldap::NG Web-SSO system.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Lemonldap::NG::Manager*
%{perl_vendorlib}/Lemonldap/NG/Manager.pm
%{perl_vendorlib}/Lemonldap/NG/Manager/
%{perl_vendorlib}/auto/Lemonldap/NG/Manager/
%dir %{perl_vendorlib}/Lemonldap/NG/
%dir %{perl_vendorlib}/auto/Lemonldap/NG/
%dir %{perl_vendorlib}/Lemonldap/
%dir %{perl_vendorlib}/auto/Lemonldap/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.44-1
- Initial package.
