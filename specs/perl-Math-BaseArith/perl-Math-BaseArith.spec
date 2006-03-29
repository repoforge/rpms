# $Id$
# Authority: dries
# Upstream: Gary Puckering <jgpuckering$rogers,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-BaseArith

Summary: Mixed-base number representation
Name: perl-Math-BaseArith
Version: 1.00
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-BaseArith/

Source: http://search.cpan.org/CPAN/authors/id/P/PU/PUCKERING/Math-BaseArith-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
The inspiration for this module is a pair of functions in the APL
programming language called encode (a.k.a. "representation") and decode
(a.k.a. base-value). Their principal use is to convert numbers from one
number base to another. Mixed number bases are permitted.

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
%{perl_vendorlib}/Math/BaseArith.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.00-1.2
- Rebuild for Fedora Core 5.

* Mon Apr 04 2005 Dries Verachtert <dries@ulyssis.org> - 1.00-1
- Initial package.
