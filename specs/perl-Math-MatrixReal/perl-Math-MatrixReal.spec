# $Id$
# Authority: dries
# Upstream: Jonathan Leto <jonathan$leto,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-MatrixReal

Summary: Matrix of Reals
Name: perl-Math-MatrixReal
Version: 1.9
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-MatrixReal/

Source: http://search.cpan.org/CPAN/authors/id/L/LE/LETO/Math-MatrixReal-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Implements the data type "matrix of reals" (and consequently also
"vector of reals") which can be used almost like any other basic
Perl type thanks to OPERATOR OVERLOADING.

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
%doc CHANGES CREDITS README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Math/MatrixReal.pm
%{perl_vendorlib}/Math/Kleene.pod
%{perl_vendorlib}/Math/funcs.pl

%changelog
* Tue Apr 05 2005 Dries Verachtert <dries@ulyssis.org> - 1.9-1
- Initial package.
