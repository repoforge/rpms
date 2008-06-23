# $Id$
# Authority: dries
# Upstream: Smylers <smylers$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Lite

Summary: Process and decode WWW forms and cookies
Name: perl-CGI-Lite
Version: 2.02
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Lite/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-Lite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
You can use this module to decode form and query information, including file
uploads, as well as cookies in a very simple manner; you need not concern
yourself with the actual details behind the decoding process.

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
%doc CHANGES README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/CGI/Lite.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.02-1
- Initial package.
