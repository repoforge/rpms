# $Id$
# Authority: dries
# Upstream: Marc Kerr <coder$stray-toaster,co,uk>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Plucene

Summary: Perl port of the Lucene search engine
Name: perl-Plucene
Version: 1.21
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Plucene/

Source: http://search.cpan.org/CPAN/authors/id/T/TM/TMTM/Plucene-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

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
%makeinstall
%{__rm} -Rf %{buildroot}%{perl_vendorarch} %{buildroot}%{perl_archlib}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Plucene.pm
%{perl_vendorlib}/Plucene/

%changelog
* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.21-1
- Updated to release 1.21.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Updated to release 1.20.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 1.19-1
- Initial package.
