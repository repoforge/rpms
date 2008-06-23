# $Id$
# Authority: dries
# Upstream: Brian C. Thomas <bct$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Ajax

Summary: Mechanism for AJAX or DHTML based web applications
Name: perl-CGI-Ajax
Version: 0.701
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Ajax/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-Ajax-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Perljax provides a unique mechanism for using perl code
asynchronously from javascript using AJAX to access user-written
perl functions/methods. Perljax unburdens the user from having to
write any javascript, except for having to associate an exported
method with a document-defined event (such as onClick, onKeyUp,
etc). Only in the more advanced implementations of a exported perl
method would a user need to write any javascript. Perljax supports
methods that return single results, or multiple results to the web
page. No other projects that we know of are like Perljax for the
following reasons: 1. Perljax is targeted specifically for perl
development. 2. Perljax shields the user from having to write any
javascript at all (unless they want to).  3. The URL for the HTTP GET
request is automatically generated based on HTML layout and events,
and the page is then dynamically updated.  4. Perljax is not part
of a Content Management System, or some other larger project.


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
%{perl_vendorlib}/CGI/Ajax.pm

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.701-1
- Updated to release 0.701.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.697-1
- Updated to release 0.697.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.695-1
- Updated to release 0.695.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.692-1
- Updated to release 0.692.

* Sun Dec 18 2005 Dries Verachtert <dries@ulyssis.org> - 0.681-1
- Updated to release 0.681.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.67-1
- Initial package.
