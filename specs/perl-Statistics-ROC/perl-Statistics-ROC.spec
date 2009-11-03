# $Id$
# Authority: dries
# Upstream: Hans A. Kestler <hans,kestler$uni-ulm,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Statistics-ROC
%define real_version 0.01

Summary: Receiver-operator-characteristic (ROC) curves with nonparametric confidence bounds
Name: perl-Statistics-ROC
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Statistics-ROC/

Source: http://www.cpan.org/modules/by-module/Statistics/Statistics-ROC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 4:5.8.8
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 4:5.8.8

%description
This code implements a method for constructing nonparametric confidence
for ROC curves described in
  R.A. Hilgers, Distribution-Free Confidence Bounds for ROC Curves,
  Meth Inform Med 1991; 30:96-101
Additionally some auxilliary functions were ported (and corrected) from
Fortran (Applied Statistics, ACM).

A graphical userinterface for drawing and printing these ROC curves is
supplied with the module (roc_ui.pl).

%prep
%setup -n %{real_name}-%{real_version}
%{__perl} -pi -e 's|/usr/local/bin/perl|/usr/bin/perl|g;' *.pl

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Statistics::ROC.3pm*
%dir %{perl_vendorlib}/Statistics/
#%{perl_vendorlib}/Statistics/ROC/
%{perl_vendorlib}/Statistics/ROC.pm
%{perl_vendorlib}/Statistics/roc_ui.pl

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Updated to release 0.04.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
