# $Id$
# Authority: dries
# Upstream: Curtis &quot;Ovid&quot; Poe <ovid$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name TAPx-Parser

Summary: TAPx Parser
Name: perl-TAPx-Parser
Version: 0.41
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/TAPx-Parser/

Source: http://www.cpan.org/authors/id/O/OV/OVID/TAPx-Parser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
A parser for TAP output.

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
%dir %{perl_vendorlib}/TAPx/
%{perl_vendorlib}/TAPx/Parser.pm
%{perl_vendorlib}/TAPx/Parser/

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.41-1
- Updated to release 0.41.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.33-1
- Updated to release 0.33.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.30-1
- Initial package.
