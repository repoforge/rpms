# $Id$
# Authority: dag
# Upstream: <xern$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Acme-CramCode

Summary: Perl module to compress your code
Name: perl-Acme-CramCode
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Acme-CramCode/

Source: http://www.cpan.org/modules/by-module/Acme/Acme-CramCode-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Acme-CramCode is a Perl module to compress your code.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Acme::CramCode.3pm*
%dir %{perl_vendorlib}/Acme/
%{perl_vendorlib}/Acme/CramCode.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
