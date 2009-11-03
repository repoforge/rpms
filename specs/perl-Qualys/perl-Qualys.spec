# $Id$
# Authority: dag
# Upstream: Anthony G Persaud <apersaud$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Qualys

Summary: Perl module to connect to the Qualys scanner API
Name: perl-Qualys
Version: 0.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Qualys/

Source: http://www.cpan.org/authors/id/A/AP/APERSAUD/Qualys-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Qualys is a Perl module to connect to the Qualys scanner API.

This package contains the following Perl module:

    Qualys

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Qualys.3pm*
%{perl_vendorlib}/Qualys.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
