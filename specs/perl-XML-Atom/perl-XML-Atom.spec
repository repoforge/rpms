# $Id$
# Authority: dries
# Upstream: Tatsuhiko Miyagawa <miyagawa$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Atom

Summary: Implementation of Atom
Name: perl-XML-Atom
Version: 0.23
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Atom/

Source: http://www.cpan.org/modules/by-module/XML/XML-Atom-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl-DateTime
BuildRequires: perl-XML-LibXML
BuildRequires: perl-URI
BuildRequires: perl-XML-XPath
BuildRequires: perl-libwww-perl
BuildRequires: perl-LWP-Authen-Wsse
BuildRequires: perl-Digest-SHA1
BuildRequires: perl(Class::Data::Inheritable)

%description
This module implements the API and feed format of Atom.

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
%{perl_vendorlib}/XML/Atom.pm
%{perl_vendorlib}/XML/Atom/

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.23-1
- Updated to release 0.23.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.19-1
- Updated to release 0.19.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.16-1.2
- Rebuild for Fedora Core 5.

* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.16-1
- Initial package.
