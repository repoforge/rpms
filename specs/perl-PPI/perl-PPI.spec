# $Id$

# Authority: dries
# Upstream: Adam Kennedy <cpan$ali,as>

%define real_name PPI
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Parse and manipulate perl code non-destructively
Name: perl-PPI
Version: 0.902
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PPI/

Source: http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/PPI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-ExtUtils-AutoInstall, perl-File-Slurp
BuildRequires: perl-List-MoreUtils, perl-Clone, perl-Class-Autouse
BuildRequires: perl-Test-ClassAPI

%description
This is an in-development package for parsing, manipulating and saving
perl code, without using the perl interpreter, the B modules, or any
other hacks that use perl's inbuilt grammar.

Please note that is project it intended as a mechanism for working with
perl content, NOT to actually compile and run working perl applications.
Thus, it provides only an approximation of the detail and flexibility
available to the real perl parser, if a quite close approximation.

It has been shown many times that it is impossible to FULLY "parse" Perl
code without also executing it. We do not intend to fully parse it, just
get enough details to analyse it, alter it, and save it back without
losing details like whitespace, comments and other stuff lost when using
the B:: modules.

%prep
%setup -n %{real_name}-%{version}

%build
echo | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/PPI.pm
%{perl_vendorlib}/PPI/*

%changelog
* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.902-1
- Updated to release 0.902.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.840-1
- Updated to release 0.840.

* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> - 0.830-1
- Update to release 0.830.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.824-1
- Initial package.
