# $Id$
# Authority: dag
# Upstream: Mark Southern <msouthern$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Jar-Signer

Summary: Perl module to ease the process of creating a signed Jar file
Name: perl-Jar-Signer
Version: 0.1
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Jar-Signer/

Source: http://www.cpan.org/authors/id/M/MS/MSOUTHERN/Jar-Signer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Jar-Signer is a Perl module to ease the process of creating
a signed Jar file.

This package contains the following Perl module:

    Jar::Signer

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
%doc CHANGES MANIFEST README
%doc %{_mandir}/man3/Jar::Signer.3pm*
%dir %{perl_vendorlib}/Jar/
%{perl_vendorlib}/Jar/Signer.pm
%{perl_vendorlib}/Jar/jarsigner.pl

%changelog
* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.1-1
- Initial package. (using DAR)
