# $Id$
# Authority: dries
# Upstream: Mark Stosberg <mark$summersault,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Application

Summary: Framework for building reusable web-applications
Name: perl-CGI-Application
Version: 4.0_4
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Application/

Source: http://search.cpan.org/CPAN/authors/id/M/MA/MARKSTOS/CGI-Application-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl-HTML-Template

%description
CGI::Application is intended to make it easier to create sophisticated,
reusable web-based applications. This module implements a methodology which,
if followed, will make your web software easier to design, easier to
document, easier to write, and easier to evolve.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/CGI/Application.pm
%{perl_vendorlib}/CGI/Application

%changelog
* Sun Jul 03 2005 Dries Verachtert <dries@ulyssis.org> - 4.01-1
- Updated to release 4.01.
- Added perl-HTML-Template requirement (thanks to Cesar Alba).

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 4.0_4-1
- Updated to release 4.0_4.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 4.0_2-1
- Initial package.
