# $Id$
# Authority: dries
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Mason
%define real_version 1.38

Summary: Web site development and delivery system
Name: perl-HTML-Mason
Version: 1.38
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Mason/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-Mason-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)

%description
Mason is a Perl-based web site development and delivery
system.  Mason allows web pages and sites to be constructed from
shared, reusable building blocks called components. Components contain
a mix of Perl and HTML, and can call each other and pass values back
and forth like subroutines. Components increase modularity and
eliminate repetitive work: common design elements (headers, footers,
menus, logos) can be extracted into their own components where they
need be changed only once to affect the whole site.

%prep
%setup -n %{real_name}-%{real_version}

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
%{_bindir}/mason.pl
%{_bindir}/convert0.*
%{perl_vendorlib}/HTML/Mason.pm
%{perl_vendorlib}/Apache/Mason.pm
%{perl_vendorlib}/Bundle/HTML/Mason.pm
%{perl_vendorlib}/HTML/Mason/

%changelog
* Sun Dec 23 2007 Dries Verachtert <dries@ulyssis.org> - 1.38-1
- Updated to release 1.38.

* Fri Apr 28 2006 Dries Verachtert <dries@ulyssis.org> - 1.3200-1
- Changed the version so it's greater as the previous version 1.3101, 
  informed the author about the problem with these versions for rpms.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.32-1
- Updated to release 1.32.

* Sat Dec 31 2005 Dries Verachtert <dries@ulyssis.org> - 1.3101-1
- Initial package.
