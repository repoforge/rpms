# $Id$
# Authority: dries
# Upstream: Dave Cross <dave$dave,org,uk>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Array-Compare

Summary: Extension for comparing arrays
Name: perl-Array-Compare
Version: 1.13
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Array-Compare/

Source: http://search.cpan.org/CPAN/authors/id/D/DA/DAVECROSS/Array-Compare-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-Module-Build

%description
Array::Compare is a Perl module which allows you to compare two arrays.

It has a number of features which allow you to control the way that the
arrays are compared:

* white space in array elements can be significant or ignored.
* particular columns in the arrays can be ignored.

Additionally you can get a simple true/false return value or the number
of columns which differ or an array containing the indexes of the
differing columns.
   
%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir="%{buildroot}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}
%{__rm} -rf %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Array/Compare.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.13-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.13-1
- Updated to release 1.13.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Initial package.
