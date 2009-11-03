# $Id$
# Authority: dag
# Upstream: Tuomas J. Lukka <lukka$iki,fi>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WeakRef

Summary: Perl module that implements an API to the Perl weak references
Name: perl-WeakRef
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WeakRef/

Source: http://www.cpan.org/authors/id/L/LU/LUKKA/WeakRef-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-WeakRef is a Perl module that implements an API to the Perl
weak references.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man3/WeakRef.3pm*
%{perl_vendorarch}/WeakRef.pm
%{perl_vendorarch}/auto/WeakRef/

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
