# $Id$
# Authority: dries
# Upstream: Andy Murren <amurren$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-WML

Summary: Subclass of CGI.pm for WML output and WML methods
Name: perl-CGI-WML
Version: 0.09
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-WML/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-WML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl-XML-Parser
BuildRequires: perl(ExtUtils::MakeMaker)

%description
CGI::WML provides WML output and WML methods for CGI programming.
The purpose of the module is to retain the familiar CGI.pm way of
programming to enable experienced CGI programmers to use their
existing skills when creating WAP applications.

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
%{perl_vendorlib}/CGI/WML.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Initial package.
