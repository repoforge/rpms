# $Id$
# Authority: dries
# Upstream: Yasuhiro Sasama <ysas$nmt,ne,jp>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Bezier-Convert

Summary: Convert cubic and quadratic bezier each other
Name: perl-Math-Bezier-Convert
Version: 0.02
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Bezier-Convert/

Source: http://www.cpan.org/modules/by-module/Math/Math-Bezier-Convert-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

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
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Math/Bezier/Convert.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1.2
- Rebuild for Fedora Core 5.

* Mon Apr 04 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
