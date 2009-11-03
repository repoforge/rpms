# $Id$
# Authority: dag
# Upstream: Tom Phoenix <rootbeer$redcat,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Taint

Summary: Perl module to taint variables
Name: perl-Taint
Version: 0.09
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Taint/

Source: http://www.cpan.org/modules/by-module/Taint/Taint-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Taint is a Perl module to taint variables.

This package contains the following Perl module:

    Taint

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
%doc Changes INSTALL MANIFEST README TODO
%doc %{_mandir}/man3/Taint.3pm*
#%{perl_vendorlib}/Taint/
%{perl_vendorlib}/Taint.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
