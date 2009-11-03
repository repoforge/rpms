# $Id$
# Authority: dries
# Upstream: Gary Spivey <spivey$romulus,ncsc,mil>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-EP3

Summary: The Extensible Perl PreProcessor
Name: perl-Text-EP3
Version: 1.10
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-EP3/

Source: http://www.cpan.org/modules/by-module/Text/Text-EP3-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
EP3 is a Perl5 program that preprocesses STDIN or some set of
input files and produces an output file. EP3 only works on input
files and produces output files. It seems to me that if you want
to preprocess arrays or somesuch, you should be using perl. EP3
was first developed to provide a flexible preprocessor for the
Verilog hardware description language. Verilog presents some
problems that were not easily solved by using cpp or m4. I
wanted to be able to use a normal preprocessor, but extend its
functionality. So I wrote EP3 - the Extensible Perl
PreProcessor. The main difference between EP3 and other
preprocessors is its built-in extensibility. Every directive in
EP3 is really a method defined in EP3, one of its submodules, or
embedded in the file that is being processed. By linking the
directive name to the associated methods, other methods could be
added, thus extending the preprocessor.

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
%{_bindir}/ep3
%{perl_vendorlib}/Text/EP3.pm
%{perl_vendorlib}/auto/Text/EP3

%changelog
* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Updated to release 1.10.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.00-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.00-1
- Initial package.
