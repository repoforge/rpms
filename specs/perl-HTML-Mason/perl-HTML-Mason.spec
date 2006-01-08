# $Id$
# Authority: dries
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Mason

Summary: Web site development and delivery system
Name: perl-HTML-Mason
Version: 1.32
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Mason/

Source: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/HTML-Mason-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-Module-Build

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
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir="%{buildroot}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/HTML/Mason.pm
%{perl_vendorlib}/Apache/Mason.pm
%{perl_vendorlib}/Bundle/HTML/Mason.pm
%{perl_vendorlib}/HTML/Mason/

%changelog
* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.32-1
- Updated to release 1.32.

* Sat Dec 31 2005 Dries Verachtert <dries@ulyssis.org> - 1.3101-1
- Initial package.
