# $Id$
# Authority: dries
# Upstream: Simon Wistow <simonw$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Google-Calendar

Summary: Access to Google's Calendar API
Name: perl-Net-Google-Calendar
Version: 0.4
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Google-Calendar/

Source: http://www.cpan.org/modules/by-module/Net/Net-Google-Calendar-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Programmatic access to Google's Calendar API.

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
%doc Changes Readme TODO USAGE
%doc %{_mandir}/man3/Net::Google::Calendar*
%{perl_vendorlib}/Net/Google/Calendar.pm
%{perl_vendorlib}/Net/Google/Calendar/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.4-1
- Initial package.
