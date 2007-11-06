# $Id$
# Authority: dries
# Upstream: Kim Ryan <kimryan%20nospam$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-EN-NameParse

Summary: Routines for manipulating a person's name
Name: perl-Lingua-EN-NameParse
Version: 1.23
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-EN-NameParse/

Source: http://search.cpan.org/CPAN/authors/id/K/KI/KIMRYAN/Lingua-EN-NameParse-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This module takes as input a person or persons name in
free format text and attempts to parse it. If successful,
the name is broken down into components.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist
%{__perl} -pi -e 's|/usr/local/bin/perl|%{_bindir}/perl|g;' %{buildroot}%{perl_vendorlib}/Lingua/EN/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Lingua::EN::NameGrammar*
%doc %{_mandir}/man3/Lingua::EN::NameParse*
%{perl_vendorlib}/Lingua/EN/NameParse.pm
%{perl_vendorlib}/Lingua/EN/NameGrammar.pm
#%{perl_vendorlib}/Lingua/EN/demo.pl

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.23-1
- Updated to release 1.23.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.22-2.2
- Rebuild for Fedora Core 5.

* Mon Nov  7 2005 Dries Verachtert <dries@ulyssis.org> - 1.22-2
- Fix the script which tries to use perl in /usr/local.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.22-1
- Updated to release 1.22.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.21-1
- Updated to release 1.21.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Initial package.
