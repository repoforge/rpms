# $Id$
# Authority: dries
# Upstream: Gurusamy Sarathy <gsar$ActiveState,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Alias

Summary: Performs aliasing services
Name: perl-Alias
Version: 2.32
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Alias/

Source: http://search.cpan.org/CPAN/authors/id/G/GS/GSAR/Alias-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
This module performs aliasing services.
You may find this module useful if you:
   * are tired of dereferencing hash-based object attributes
   * wish perl could make-do with fewer $, -> and {} things
   * are a little scared of using typeglobs
   * want the freedom to put what you want, when you want in
     the symbol table without having to deal with wierd syntax
   * need to use scalar constants in your program since you don't
     trust yourself from changing $PI

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/Alias/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README Todo
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Alias.pm
%{perl_vendorarch}/auto/Alias

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.32-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.32-1
- Initial package.
