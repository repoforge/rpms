# $Id$
# Authority: dries
# Upstream: BBC (British Broadcasting Corporation) <cpan$bbc,co,uk>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Pod-Xhtml

Summary: Generate well-formed XHTML documents from POD format documentation
Name: perl-Pod-Xhtml
Version: 1.57
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Pod-Xhtml/

Source: http://search.cpan.org/CPAN/authors/id/B/BB/BBC/Pod-Xhtml-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Generate well-formed XHTML documents from POD format documentation.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
%{_bindir}/pod2xhtml
%{perl_vendorlib}/Pod/Xhtml.pm
%{perl_vendorlib}/Pod/Hyperlink/

%changelog
* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.57-1
- Updated to release 1.57.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.52-1
- Updated to release 1.52.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.51-1
- Updated to release 1.51.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.44-1.2
- Rebuild for Fedora Core 5.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.44-1
- Initial package.
