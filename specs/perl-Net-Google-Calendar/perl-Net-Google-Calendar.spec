# $Id$
# Authority: dries
# Upstream: Simon Wistow <simonw$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Google-Calendar

Summary: Access to Google's Calendar API
Name: perl-Net-Google-Calendar
Version: 0.4
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Google-Calendar/

Source: http://search.cpan.org//CPAN/authors/id/S/SI/SIMONW/Net-Google-Calendar-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Programmatic access to Google's Calendar API.

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
%doc Changes Readme TODO USAGE
%doc %{_mandir}/man3/Net::Google::Calendar*
%{perl_vendorlib}/Net/Google/Calendar.pm
%{perl_vendorlib}/Net/Google/Calendar/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.4-1
- Initial package.
