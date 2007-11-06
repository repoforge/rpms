# $Id$
# Authority: dries
# Upstream: T,J, Mather <tjmather$maxmind,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-FillInForm

Summary: Populates HTML Forms with CGI data
Name: perl-HTML-FillInForm
Version: 1.06
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-FillInForm/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-FillInForm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This module automatically inserts data from a previous HTML form into the HTML input and select
tags. It is a subclass of HTML::Parser and uses it to parse the HTML and insert the values into the form
tags.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/HTML/FillInForm.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.06-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.06-1
- Updated to release 1.06.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Updated to release 1.05.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Initial package.
