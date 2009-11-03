# $Id$
# Authority: dag
# Upstream: Paul Warren <pdw$ex-parrot,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-RFC822-Address

Summary: Perl module for validating email addresses according to RFC822
Name: perl-Mail-RFC822-Address
Version: 0.3
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-RFC822-Address/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-RFC822-Address-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Mail-RFC822-Address is a Perl module for validating email
addresses according to RFC822.

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
%doc Changes INSTALL MANIFEST
%doc %{_mandir}/man3/Mail::RFC822::Address.3pm*
%dir %{perl_vendorlib}/Mail/
%dir %{perl_vendorlib}/Mail/RFC822/
%{perl_vendorlib}/Mail/RFC822/Address.pm

%changelog
* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 0.3-1
- Initial package. (using DAR)
