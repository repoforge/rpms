# $Id$
# Authority: dries
# Upstream: Hans A. Kestler <hans,kestler$medizin,uni-ulm,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Statistics-ROC

Summary: Receiver-operator-characteristic (ROC) curves with nonparametric confidence bounds
Name: perl-Statistics-ROC
Version: 0.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Statistics-ROC/

Source: http://search.cpan.org/CPAN/authors/id/H/HA/HAKESTLER/Statistics-ROC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

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
%setup -n %{real_name}-%{version}
%{__perl} -pi -e 's|/usr/local/bin/perl|/usr/bin/perl|g;' *.pl

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Statistics/ROC.pm
%{perl_vendorlib}/Statistics/roc_ui.pl

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
