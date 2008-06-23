# $Id$
# Authority: dries
# Upstream: Jason Moore <jmoore$sober,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-FastTemplate

Summary: Extension for managing templates and performing variable interpolation
Name: perl-CGI-FastTemplate
Version: 1.09
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-FastTemplate/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-FastTemplate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
CGI::FastTemplate manages templates and parses templates replacing
variable names with values.  It was designed for mid to large scale web
applications (CGI, mod_perl) where there are great benefits to separating
the logic of an application from the specific implementation details.

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
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/CGI/FastTemplate.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.09-1
- Initial package.
