# $Id$
# Authority: dries
# Upstream: &#9786;&#21776;&#23447;&#28450;&#9787; <autrijus$autrijus,org>

### EL6 ships with perl-Locale-Maketext-Simple-0.18-115.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Locale-Maketext-Simple

Summary: Simple interface to Locale::Maketext::Lexicon
Name: perl-Locale-Maketext-Simple
Version: 0.21
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Locale-Maketext-Simple/

Source: http://www.cpan.org/modules/by-module/Locale/Locale-Maketext-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Simple interface to Locale::Maketext::Lexicon.

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
%dir %{perl_vendorlib}/Locale/
%dir %{perl_vendorlib}/Locale/Maketext/
%{perl_vendorlib}/Locale/Maketext/Simple.pm

%changelog
* Tue Sep  8 2009 Christoph Maser <cmr@financial.com> - 0.21-1
- Updated to version 0.21.

* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 0.20-1
- Updated to version 0.20.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.18-1
- Updated to release 0.18.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.12-1.2
- Rebuild for Fedora Core 5.

* Fri Jan  7 2005 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Initial package.

