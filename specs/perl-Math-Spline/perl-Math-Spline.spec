# $Id$
# Authority: dries
# Upstream: John A.R. Williams <J,A,R,Williams$aston,ac,uk>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Spline

Summary: Cubic Spline Interpolation of data
Name: perl-Math-Spline
Version: 0.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Spline/

Source: http://search.cpan.org/CPAN/authors/id/J/JA/JARW/Math-Spline-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This package provides cubic spline interpolation of numeric data. The data 
is passed as references to two arrays containing the x and y ordinates. It 
may be used as an exporter of the numerical functions or, more easily as a 
class module.

%prep
%setup -n %{real_name}-%{version}

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
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Math/Spline.pm

%changelog
* Mon Apr 04 2005 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
