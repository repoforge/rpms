# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Strip

Summary: Perl module to strip HTML-like markup from text.
Name: perl-HTML-Strip
Version: 1.06
Release: 1
License: Artistic (perl) license
Group: Development/Libraries
URL: http://search.cpan.org/dist/HTML-Strip/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-Strip-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.006, perl(ExtUtils::MakeMaker)

%description
This module strips HTML-like markup from text.  It is written in XS,
and thus about five times quicker than using regular expressions for
the same task.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorarch}/HTML/
%{perl_vendorarch}/auto/HTML/

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.06-1
- Updated to release 1.06.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.04-1.2
- Rebuild for Fedora Core 5.

* Sat Feb 12 2005 Dag Wieers <dag@wieers.com> - 1.04-1
- Initial package. (using DAR)
