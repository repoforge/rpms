# $Id$
# Authority: dries
# Upstream: Steve Purkis <spurkis%20%5bat%5d%20quiup_dot_com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name AI-Perceptron

Summary: Example of a node in a neural network
Name: perl-AI-Perceptron
Version: 1.0
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/AI-Perceptron/

Source: http://search.cpan.org/CPAN/authors/id/S/SP/SPURKIS/AI-Perceptron-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-Module-Build

%description
This module is meant to show how a single node of a neural network
works.

Training is done by the *Stochastic Approximation of the
Gradient-Descent* model.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/AI/
%{perl_vendorlib}/AI/Perceptron.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Initial package.
