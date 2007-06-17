# $Id$
# Authority: dries
# Upstream: Tatsuhiko Miyagawa <miyagawa$gmail,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Attribute-Protected

Summary: Implements proctected methods with attributes
Name: perl-Attribute-Protected
Version: 0.03
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Attribute-Protected/

Source: http://search.cpan.org/CPAN/authors/id/M/MI/MIYAGAWA/Attribute-Protected-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
Attribute::Protected implements something like public / private /
protected methods in C++ or Java.

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
%{perl_vendorlib}/Attribute/Protected.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.03-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
