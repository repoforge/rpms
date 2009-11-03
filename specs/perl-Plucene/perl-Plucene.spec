# $Id$
# Authority: dries
# Upstream: Marc Kerr <coder$stray-toaster,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Plucene

Summary: Perl port of the Lucene search engine
Name: perl-Plucene
Version: 1.25
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Plucene/

Source: http://www.cpan.org/modules/by-module/Plucene/Plucene-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Slurp) >= 2002.1031
BuildRequires: perl(Test::Harness) >= 2.3

%description
Plucene is a Perl port of the Java Lucene search engine.
(http://jakarta.apache.org/lucene/) In the same way as Lucene, it is not
a standalone application, but a library you can use to index documents
and search for things in them later.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Plucene.3pm*
%doc %{_mandir}/man3/Plucene::*.3pm*
%{perl_vendorlib}/Plucene/
%{perl_vendorlib}/Plucene.pm

%changelog
* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 1.25-1
- Updated to release 1.25.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.24-1
- Updated to release 1.24.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.21-1
- Updated to release 1.21.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Updated to release 1.20.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 1.19-1
- Initial package.
