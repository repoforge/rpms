# $Id$
# Authority: dries
# Upstream: Marcel Grünauer <marcel$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tie-Scalar-Timeout

Summary: Scalar variables that time out
Name: perl-Tie-Scalar-Timeout
Version: 1.33
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-Scalar-Timeout/

Source: http://www.cpan.org/modules/by-module/Tie/Tie-Scalar-Timeout-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0 
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::Compile)
BuildRequires: perl(Test::More)
BuildRequires: perl(UNIVERSAL::require)
Requires: perl >= 0:5.6.0 

%description
This module allows you to tie a scalar variable whose value will be
reset (subject to an expiry policy) after a certain time and/or a
certain number of uses. One possible application for this module might
be to time out session variables in mod_perl programs.

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
%doc %{_mandir}/man3/Tie::Scalar::Timeout.3pm*
%dir %{perl_vendorlib}/Tie/
%dir %{perl_vendorlib}/Tie/Scalar/
#%{perl_vendorlib}/Tie/Scalar/Timeout/
%{perl_vendorlib}/Tie/Scalar/Timeout.pm

%changelog
* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 1.33-1
- Updated to release 1.33.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.2-1
- Initial package.
