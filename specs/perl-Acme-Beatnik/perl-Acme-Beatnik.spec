# $Id$
# Authority: dag
# Upstream: Hendrik Van Belleghem <hendrik,vanbelleghem$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Acme-Beatnik

Summary: Perl module that implements a source filter for the Beatnik language
Name: perl-Acme-Beatnik
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Acme-Beatnik/

Source: http://www.cpan.org/modules/by-module/Acme/Acme-Beatnik-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Acme-Beatnik is a Perl module that implements a source filter for the
Beatnik language.

This package contains the following Perl module:

    Acme::Beatnik

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
%doc %{_mandir}/man3/Acme::Beatnik.3pm*
%dir %{perl_vendorlib}/Acme/
%{perl_vendorlib}/Acme/example.pl
%{perl_vendorlib}/Acme/findwords.pl
%{perl_vendorlib}/Acme/generate.pl
%{perl_vendorlib}/Acme/Beatnik.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
