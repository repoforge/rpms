# $Id$
# Authority: dries
# Upstream: Yasuhiro Sasama <ysas$nmt,ne,jp>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Bezier-Convert

Summary: Convert cubic and quadratic bezier each other
Name: perl-Math-Bezier-Convert
Version: 0.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Bezier-Convert/

Source: http://search.cpan.org/CPAN/authors/id/Y/YS/YSAS/Math-Bezier-Convert-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Math::Bezier::Convert provides functions to convert quadratic bezier to 
cubic, to approximate cubic bezier to quadratic, and to approximate cubic 
and quadratic bezier to polyline.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Math/Bezier/Convert.pm

%changelog
* Mon Apr 04 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
