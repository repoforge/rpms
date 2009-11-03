# $Id$
# Authority: dries
# Upstream: Devin Carraway <cpan$nospam,devin,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-BasicTemplate

Summary: Simple lexical text/html/etc template parser
Name: perl-Text-BasicTemplate
Version: 2.006.1
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-BasicTemplate/

Source: http://www.cpan.org/modules/by-module/Text/Text-BasicTemplate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is a template parsing module for perl5 and higher.  Originally
written for use with HTML templates, it has proved quite useful for
many kinds of printable-character file parsing.

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
%{perl_vendorlib}/Text/BasicTemplate.pm
%{perl_vendorlib}/auto/Text/BasicTemplate

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.006.1-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.006.1-1
- Initial package.
