# $Id$
# Authority: dag
# Upstream: Tatsuhiko Miyagawa <miyagawa$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Untaint-email

Summary: Perl module to validate an email address.
Name: perl-CGI-Untaint-email
Version: 0.03
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Untaint-email/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-Untaint-email-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
CGI-Untaint-email is a Perl module to validate an email address.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/CGI::Untaint::email.3pm*
%dir %{perl_vendorlib}/CGI/
%dir %{perl_vendorlib}/CGI/Untaint/
%{perl_vendorlib}/CGI/Untaint/email.pm

%changelog
* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
