# $Id$
# Authority: shuff
# Upstream: Florian Ragwitz <rafl$debian,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Moose

Summary: Postmodern object system for Perl 5
Name: perl-Moose
Version: 0.93
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Moose/

Source: http://www.cpan.org/authors/id/D/DR/DROLSKY/Moose-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.1
BuildRequires: perl(Carp)
BuildRequires: perl(Class::MOP) >= 0.94
BuildRequires: perl(Data::OptList)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(List::MoreUtils) >= 0.12
#BuildRequires: perl(Scalar::Util) >= 1.19
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Sub::Exporter) >= 0.980
BuildRequires: perl(Sub::Name)
BuildRequires: perl(Task::Weaken)
BuildRequires: perl(Test::Exception) >= 0.27
BuildRequires: perl(Try::Tiny) >= 0.02
#BuildRequires: perl(Test::More) >= 0.77
Requires: perl >= 2:5.8.1

%description
Moose is a Perl module that implements a complete modern object system.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Moose.3pm*
%doc %{_mandir}/man3/Moose::*.3pm*
%doc %{_mandir}/man3/oose.3pm*
%doc %{_mandir}/man3/Test::Moose.3pm*
%{perl_vendorlib}/Moose/
%{perl_vendorlib}/Moose.pm
%{perl_vendorlib}/oose.pm
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/Moose.pm

%changelog
* Tue Dec 01 2009 Steve Huff <shuff@vecna.org> - 0.93-1
- Updated to version 0.93.

* Mon Sep  7 2009 Christoph Maser <cmr@financial.com> - 0.89-2
- Remove version from Scalar::Util dependency

* Mon Sep  7 2009 Christoph Maser <cmr@financial.com> - 0.89-1
- Updated to version 0.89.

* Fri Jul 31 2009 Christoph Maser <cmr@financial.com> - 0.88-1
- Updated to version 0.88.

* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 0.87-1
- Updated to version 0.87.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.86-1
- Updated to version 0.86.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.85-1
- Updated to version 0.85.

* Thu May 28 2009 Christoph Maser <cmr@financial.com> - 0.79-1
- Updated to release 0.79.

* Wed Nov 26 2008 Dag Wieers <dag@wieers.com> - 0.61-1
- Updated to release 0.61.

* Wed Oct 15 2008 Dag Wieers <dag@wieers.com> - 0.59-1
- Updated to release 0.59.

* Thu Aug 21 2008 Dries Verachtert <dries@ulyssis.org> - 0.55-1
- Updated to release 0.55.

* Fri Jul 25 2008 Dries Verachtert <dries@ulyssis.org> - 0.54-1
- Updated to release 0.54.

* Wed Jun 25 2008 Dag Wieers <dag@wieers.com> - 0.50-1
- Updated to release 0.50.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.44-1
- Updated to release 0.44.

* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 0.38-1
- Updated to release 0.38.

* Sat Jan 26 2008 Dag Wieers <dag@wieers.com> - 0.35-1
- Updated to release 0.35.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.34-1
- Updated to release 0.34.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 0.33-1
- Updated to release 0.33.

* Wed Dec 05 2007 Dag Wieers <dag@wieers.com> - 0.32-1
- Updated to release 0.32.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 0.31-1
- Updated to release 0.31.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.30-1
- Updated to release 0.30.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.29-1
- Updated to release 0.29.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.20-1
- Initial package. (using DAR)
