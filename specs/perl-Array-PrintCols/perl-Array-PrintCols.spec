# $Id$
# Authority: dries
# Upstream: Alan K. Stebbens <aks$stebbens,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Array-PrintCols

Summary: Print vertically sorted columns
Name: perl-Array-PrintCols
Version: 2.1
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Array-PrintCols/

Source: http://www.cpan.org/modules/by-module/Array/Array-PrintCols-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Array::PrintCols is a Perl 5 module which defines a subroutine to print
arrays of elements in alphabetically, vertically sorted columns.  Optional
arguments can be given to control either the width or number of the columns,
the total width of the output, and the amount of indentation.

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
%{perl_vendorlib}/Array/PrintCols.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.1-1
- Initial package.
