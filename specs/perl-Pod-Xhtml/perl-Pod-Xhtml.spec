# $Id$
# Authority: dries
# Upstream: BBC (British Broadcasting Corporation) <cpan$bbc,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Pod-Xhtml

Summary: Generate well-formed XHTML documents from POD format documentation
Name: perl-Pod-Xhtml
Version: 1.59
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Pod-Xhtml/

Source: http://www.cpan.org/modules/by-module/Pod/Pod-Xhtml-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Generate well-formed XHTML documents from POD format documentation.

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
%doc COPYING Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man1/pod2xhtml.1*
%doc %{_mandir}/man3/Pod::Hyperlink::BounceURL.3pm*
%doc %{_mandir}/man3/Pod::Xhtml.3pm*
%{_bindir}/pod2xhtml
%dir %{perl_vendorlib}/Pod/
%{perl_vendorlib}/Pod/Hyperlink/
#%{perl_vendorlib}/Pod/Xhtml/
%{perl_vendorlib}/Pod/Xhtml.pm

%changelog
* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 1.59-1
- Updated to release 1.59.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.57-1
- Updated to release 1.57.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.52-1
- Updated to release 1.52.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.51-1
- Updated to release 1.51.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.44-1
- Initial package.
