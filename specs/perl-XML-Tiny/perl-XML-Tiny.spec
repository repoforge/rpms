# $Id$
# Authority: dries
# Upstream: David Cantrell <pause$barnyard,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Tiny

Summary: Simple lightweight parser for a subset of XML
Name: perl-XML-Tiny
Version: 2.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Tiny/

Source: http://search.cpan.org/CPAN/authors/id/D/DC/DCANTRELL/XML-Tiny-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Simple lightweight parser for a subset of XML.

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
%doc CHANGES MANIFEST META.yml README
%doc %{_mandir}/man3/XML::Tiny.3pm*
%dir %{perl_vendorlib}/XML/
#%{perl_vendorlib}/XML/Tiny/
%{perl_vendorlib}/XML/Tiny.pm

%changelog
* Thu Jan 14 2010 Christoph Maser <cmr@financial.com> - 2.03-1
- Updated to version 2.03.

* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 2.02-1
- Updated to version 2.02.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 1.11-1
- Updated to release 1.11.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Initial package.
