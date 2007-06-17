# $Id$
# Authority: dries
# Upstream: Damian Conway <damian$conway,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Attribute-Handlers-Prospective

Summary: Richer semantics for attribute handlers
Name: perl-Attribute-Handlers-Prospective
Version: 0.01
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Attribute-Handlers-Prospective/

Source: http://search.cpan.org/CPAN/authors/id/D/DC/DCONWAY/Attribute-Handlers-Prospective-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
This module, when inherited by a package, allows that package's class to
define attribute handler subroutines for specific attributes. Variables
and subroutines subsequently defined in that package, or in packages
derived from that package may be given attributes with the same names as
the attribute handler subroutines, which will then be called at the end
of the compilation phase (i.e. in an INIT block).

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
%{perl_vendorlib}/Attribute/Handlers/Prospective.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
