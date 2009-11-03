# $Id$
# Authority: dries
# Upstream: Eric Estabrooks <eric$urbanrage,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IMAP-Admin

Summary: Basic IMAP server administration
Name: perl-IMAP-Admin
Version: 1.6.6
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IMAP-Admin/

Source: http://www.cpan.org/modules/by-module/IMAP/IMAP-Admin-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Perl module for basic IMAP server administration.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml examples/
%doc %{_mandir}/man3/IMAP::Admin.3pm*
%dir %{perl_vendorlib}/IMAP/
#%{perl_vendorlib}/IMAP/Admin/
%{perl_vendorlib}/IMAP/Admin.pm

%changelog
* Wed Oct 08 2008 Dag Wieers <dag@wieers.com> - 1.6.6-1
- Updated to release 1.6.6.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.6.4-1
- Initial package.
