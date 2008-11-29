# $Id$
# Authority: dries
# Upstream: Benjamin Trott <cpan$stupidfool,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Atom

Summary: Atom API and Feed Support
Name: perl-XML-Atom
Version: 0.32
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Atom/

Source: http://www.cpan.org/modules/by-module/XML/XML-Atom-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl-libwww-perl
BuildRequires: perl(Class::Data::Inheritable)
BuildRequires: perl(DateTime)
BuildRequires: perl(Digest::SHA1)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(LWP::Authen::Wsse)
BuildRequires: perl(URI)
BuildRequires: perl(XML::LibXML) >= 1.64
BuildRequires: perl(XML::LibXML)
BuildRequires: perl(XML::XPath)

%description
Atom API and Feed Support.

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
%doc %{_mandir}/man3/XML::Atom.3pm*
%doc %{_mandir}/man3/XML::Atom::*.3pm*
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/Atom/
%{perl_vendorlib}/XML/Atom.pm

%changelog
* Wed Nov 26 2008 Dag Wieers <dag@wieers.com> - 0.32-1
- Updated to release 0.32.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 0.28-1
- Updated to release 0.28.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.23-1
- Updated to release 0.23.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.19-1
- Updated to release 0.19.

* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.16-1
- Initial package.
