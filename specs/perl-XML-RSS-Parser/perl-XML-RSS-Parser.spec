# $Id$
# Authority: dries
# Upstream: Timothy Appnel <cpan$timeaoutloud,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-RSS-Parser

Summary: Parser for RSS formats
Name: perl-XML-RSS-Parser
Version: 4.0
Release: 1.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-RSS-Parser/

Source: http://www.cpan.org/modules/by-module/XML/XML-RSS-Parser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
XML::RSS::Parser is an objected-oriented liberal parser for handling
the morass of RSS formats in use.

%prep
%setup -n %{real_name}-4

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/XML/RSS/Parser.pm
%{perl_vendorlib}/XML/RSS/Parser/*

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 4.0-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 4.0-1
- Updated to release 4.0.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 2.15-1
- Initial package.
