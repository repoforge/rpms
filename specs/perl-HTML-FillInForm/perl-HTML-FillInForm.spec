# $Id$

# Authority: dries
# Upstream:

%define real_name HTML-FillInForm
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Populates HTML Forms with CGI data
Name: perl-HTML-FillInForm
Version: 1.04
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-FillInForm/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/HTML-FillInForm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This module automatically inserts data from a previous HTML form into the HTML input and select
tags. It is a subclass of HTML::Parser and uses it to parse the HTML and insert the values into the form
tags.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/HTML/FillInForm.pm
# %{_libdir}/perl5/vendor_perl/*/HTML/FillInForm/*
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Initial package.
