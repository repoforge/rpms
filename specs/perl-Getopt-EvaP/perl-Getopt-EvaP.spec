# $Id$
# Authority: dries
# Upstream: Stephen O. Lidie <sol0$Lehigh,EDU>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Getopt-EvaP

Summary: Evaluate Perl command line parameters
Name: perl-Getopt-EvaP
Version: 2.3.5
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Getopt-EvaP/

Source: http://search.cpan.org/CPAN/authors/id/L/LU/LUSOL/Getopt-EvaP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Briefly, EvaP() is a table driven command line argument processor that type
checks values and provides up to three levels of online help on the comamnd
and its parameters.  You provide the Parameter Description Table (PDT), and,
optionally, a help Message Module (MM), and call EvaP() with pointers to this
information, and get in return an option hash with command line values indexed
by argument name.  When users request help, EvaP() uses the PDT and MM to
present the help data and exits, all automatically.

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
%doc README
%doc %{_mandir}/man3/*
%{_bindir}/genpTk
%{perl_vendorlib}/Getopt/EvaP.pm
%{perl_vendorlib}/Getopt/DisU.pl

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.3.5-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.3.5-1
- Initial package.
