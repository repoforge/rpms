# $Id$
# Authority: dries
# Upstream: Steve Harris <perl$nullspace,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Merge

Summary: General purpose text/data merging methods
Name: perl-Text-Merge
Version: 0.36
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Merge/

Source: http://www.cpan.org/modules/by-module/Text/Text-Merge-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The Text::Merge module provides a set of methods for merging text display
templates with data sets.  It is extended to include support for
list of items of various types, displayed individually in context.

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
%doc CHANGES README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Text/Merge.pm
%{perl_vendorlib}/Text/Merge
%{perl_vendorlib}/auto/Text/Merge

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.36-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.36-1
- Initial package.
