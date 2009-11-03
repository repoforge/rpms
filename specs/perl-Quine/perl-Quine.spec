# $Id$
# Authority: dag
# Upstream: Jeff Pinyan <japhy,734+CPAN$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Quine

Summary: Perl module for creating quines
Name: perl-Quine
Version: 1.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Quine/

Source: http://www.cpan.org/authors/id/P/PI/PINYAN/Quine-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Quine is a Perl module for creating quines.

This package contains the following Perl module:

    Quine

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
%doc %{_mandir}/man3/Quine.3pm*
%{perl_vendorlib}/Quine.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
