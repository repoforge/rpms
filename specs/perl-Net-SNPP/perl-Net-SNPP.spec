# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-SNPP

Summary: Perl Simple Network Pager Protocol Client
Name: perl-Net-SNPP
Version: 1.17
Release: 1.2%{?dist}
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-SNPP/

Source: http://www.cpan.org/modules/by-module/Net/Net-SNPP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
Simple Network Pager Protocol Client.

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
%doc MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Net/SNPP.pm
%{perl_vendorlib}/Net/SNPP/

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.17-1
- Updated to release 1.17.

* Thu Mar 04 2004 Dag Wieers <dag@wieers.com> - 1.16-1
- Initial package. (using DAR)
