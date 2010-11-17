# $Id$
# Authority: dries
# Upstream: Mark Overmeer <mark$overmeer,net>

### EL6 ships with perl-MIME-Types-1.28-2.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MIME-Types

Summary: Definition of MIME types
Name: perl-MIME-Types
Version: 1.28
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MIME-Types/

Source: http://www.cpan.org/modules/by-module/MIME/MIME-Types-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
A start for a more detailed data-structure to keep knowledge
about various data types are defined by MIME.  Some basic
treatments with mime types are implemented.

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
%doc ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man3/MIME::Type.3pm*
%doc %{_mandir}/man3/MIME::Types.3pm*
%dir %{perl_vendorlib}/MIME/
%{perl_vendorlib}/MIME/Type.pm
%{perl_vendorlib}/MIME/Type.pod
%{perl_vendorlib}/MIME/Types.pm
%{perl_vendorlib}/MIME/Types.pod

%changelog
* Tue Sep  8 2009 Christoph Maser <cmr@financial.com> - 1.28-1
- Updated to version 1.28.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.27-1
- Updated to version 1.27.

* Tue Jun 24 2008 Dag Wieers <dag@wieers.com> - 1.24-1
- Updated to release 1.24.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 1.23-1
- Updated to release 1.23.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.22-1
- Updated to release 1.22.

* Wed Nov 14 2007 Dag Wieers <dag@wieers.com> - 1.21-1
- Updated to release 1.21.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Updated to release 1.20.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.19-1
- Updated to release 1.19.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.18-1
- Updated to release 1.18.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.17-1
- Updated to release 1.17.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Updated to release 1.16.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.15-1
- Updated to release 1.15.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.13-1
- Initial package.
