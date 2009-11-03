# $Id$
# Authority: dag
# Upstream: David Kröber <dk83$gmx,li>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unix-Getrusage

Summary: Perl interface to the Unix getrusage system call
Name: perl-Unix-Getrusage
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unix-Getrusage/

Source: http://www.cpan.org/modules/by-module/Unix/Unix-Getrusage-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Unix-Getrusage is a Perl interface to the Unix getrusage system call.

This package contains the following Perl module:

    Unix::Getrusage

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Unix::Getrusage.3pm*
%dir %{perl_vendorarch}/Unix/
%{perl_vendorarch}/Unix/Getrusage.pm
%dir %{perl_vendorarch}/auto/Unix/
%{perl_vendorarch}/auto/Unix/Getrusage/

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
