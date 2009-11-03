# $Id$
# Authority: dag
# Upstream: Yasushi Nakajima <nakajima$netstock,co,jp>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Safe-Hole

Summary: Perl module to make a hole to the original main compartment in the Safe compartment
Name: perl-Safe-Hole
Version: 0.10
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Safe-Hole/

Source: http://www.cpan.org/modules/by-module/Safe/Safe-Hole-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Safe-Hole is a Perl module to make a hole to the original main
compartment in the Safe compartment.

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
%doc Changes Copying MANIFEST README
%doc %{_mandir}/man3/Safe::Hole.3pm*
%dir %{perl_vendorarch}/Safe/
%{perl_vendorarch}/Safe/Hole.pm
%dir %{perl_vendorarch}/auto/Safe/
%{perl_vendorarch}/auto/Safe/Hole/

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.10-1
- Initial package. (using DAR)
