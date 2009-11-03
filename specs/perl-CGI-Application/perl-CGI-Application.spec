# $Id$
# Authority: dries
# Upstream: Jesse Erlbaum <jesse$erlbaum,net>
# Upstream: Mark Stosberg <mark$summersault,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Application

Summary: Framework for building reusable web-applications
Name: perl-CGI-Application
Version: 4.31
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Application/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-Application-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)
# From yaml requires
BuildRequires: perl(CGI)
BuildRequires: perl(Carp)
BuildRequires: perl(Class::ISA)
BuildRequires: perl(HTML::Template)
BuildRequires: perl(Test::More)
Requires: perl-HTML-Template

%description
CGI::Application is intended to make it easier to create sophisticated,
reusable web-based applications. This module implements a methodology which,
if followed, will make your web software easier to design, easier to
document, easier to write, and easier to evolve.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL --installdirs vendor --destdir %{buildroot}
./Build

%install
%{__rm} -rf %{buildroot}
./Build pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ARTISTIC Changes MANIFEST META.yml README
%doc %{_mandir}/man3/CGI::Application.3pm*
%doc %{_mandir}/man3/CGI::Application::*.3pm*
%dir %{perl_vendorlib}/CGI/
%{perl_vendorlib}/CGI/Application/
%{perl_vendorlib}/CGI/Application.pm

%changelog
* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 4.31-1
- Updated to version 4.31.

* Thu Dec 18 2008 Dag Wieers <dag@wieers.com> - 4.20-1
- Updated to release 4.20.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 4.11-1
- Updated to release 4.11.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 4.10-1
- Updated to release 4.10.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 4.06-1
- Updated to release 4.06.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 4.05-1
- Updated to release 4.05.

* Sat Nov 05 2005 Dries Verachtert <dries@ulyssis.org> - 4.04-1
- Updated to release 4.04.

* Sun Jul 03 2005 Dries Verachtert <dries@ulyssis.org> - 4.01-1
- Updated to release 4.01.
- Added perl-HTML-Template requirement (thanks to Cesar Alba).

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 4.0_4-1
- Updated to release 4.0_4.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 4.0_2-1
- Initial package.
