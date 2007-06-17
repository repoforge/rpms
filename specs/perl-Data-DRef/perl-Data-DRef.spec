# $Id$
# Authority: dries
# Upstream: Matthew Simon Cavalletto <simonm$cavalletto,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-DRef

Summary: Delimited-key access to complex data structures
Name: perl-Data-DRef
Version: 1999.0206
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-DRef/

Source: http://search.cpan.org/CPAN/authors/id/E/EV/EVO/Data-DRef-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
This module provides delimited-key access to complex data structures.

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
#%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Data/DRef.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1999.0206-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1999.0206-1
- Initial package.
