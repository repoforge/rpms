# $Id$
# Authority: dag
# Upstream: Adam Spiers <adam$spiers,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-Field-Received

Summary: Mostly RFC822-compliant parser of Received headers
Name: perl-Mail-Field-Received
Version: 0.24
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-Field-Received/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-Field-Received-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Mostly RFC822-compliant parser of Received headers.

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
%doc ChangeLog INSTALL MANIFEST README
%doc %{_mandir}/man3/Mail::Field::Received.3pm*
%dir %{perl_vendorlib}/Mail/
%dir %{perl_vendorlib}/Mail/Field/
#%{perl_vendorlib}/Mail/Field/Received/
%{perl_vendorlib}/Mail/Field/Received.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.24-1
- Initial package. (using DAR)
