# $Id$
# Authority: dries
# Upstream: Robin Berjon <robin$knowscape,com>

### EL6 ships with perl-XML-SAX-Writer-0.50-8.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-SAX-Writer

Summary: SAX2 XML Writer
Name: perl-XML-SAX-Writer
Version: 0.52
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-SAX-Writer/

Source: http://www.cpan.org/modules/by-module/XML/XML-SAX-Writer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
SAX2 XML Writer.

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
%{perl_vendorlib}/XML/SAX/Writer.pm
%{perl_vendorlib}/XML/SAX/Writer

%changelog
* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 0.52-1
- Updated to version 0.52.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.50-1
- Updated to release 0.50.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.44-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.44-1
- Initial package.
